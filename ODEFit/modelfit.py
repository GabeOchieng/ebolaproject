# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:12:38 2014

@author: yile
"""
from scipy.optimize import minimize
from scipy import integrate
import pylab as py
import numpy as np
import csv

#####Getting the Data: Days and Cumulative Infected Cases####
a = []
b = []
ifile  = open('country.csv',"rb")
reader = csv.reader(ifile)

rownum = 0
for row in reader:
    if  rownum == 0:   
        header = row
    else: 
        if row[4] != '':
            a.append(row[1])
            b.append(row[4])
    
    rownum += 1


ifile.close()

py.clf()
a.reverse()
b.reverse()
a = map(int, a)
b = map(int, b)
days = np.array(a)
days = days - days[0]
cases = np.array(b)

##Setting Up Parameters 

N = 470000.
betaI = 0.128
betaH = 0.08
betaF = 0.111
alpha = 1./10
gammah = 1./4.12
gammadh = 1./6.26
gammaf = 1./4.50
gammai = 1./20.00
gammad = 1./10.38
gammaih =  1./15.88
theta1 = 0.197
delta1 = 0.75
delta2 = 0.75


#####Inputing the Model 
####N[0] is S; N[1] is E; N[2] is I; N[3] is H; N[4] is F, N[5] is R
def SIRode(P, t, N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2):
    return(
    -1/N*(betaI*P[0]*P[2]+betaH*P[0]*P[3]+betaF*P[0]*P[4]) ,    
    +1/N*(betaI*P[0]*P[2]+betaH*P[0]*P[3]+betaF*P[0]*P[4]) - alpha*P[1] ,
    +alpha*P[1] - (gammah*theta1 + gammai*(1-theta1)*(1-delta1) + gammad*(1-theta1)*delta1) * P[2] ,
    +gammah*theta1*P[2] - (gammadh*delta2+gammaih*(1-delta2))*P[3] ,
    +gammad*(1-theta1)*delta1*P[2]+gammadh*delta2*P[3]-gammaf*P[4],
    +gammai*(1-theta1)*(1-delta1)*P[2]+gammaih*(1-delta2)*P[3]+gammaf*P[4]
    )
    
# Set initial conditions
P = [N-3, 0, 3, 0, 0, 0]

# Run the ode
Nt = integrate.odeint(SIRode, P, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))

# Get the second column of data corresponding to I
INt = [row[2] for row in Nt]

py.clf()
py.plot(days, cases, 'o')
py.plot(days, INt)
py.show()



###Model Fitting

def LLode(x):
    
    N = 470000.
#    betaI = 0.128
#    betaH = 0.08
#    betaF = 0.111
#    alpha = 1./10
    betaI = x[0]
    betaH = x[1]
    betaF = x[2]
    alpha = x[3]
    gammah = x[4]
    gammadh = x[5]
    gammaf = x[6]
    gammai = x[7]
    gammad = x[8]
#    gammah = 1./4.12
#    gammadh = 1./6.26
#    gammaf = 1./4.50
#    gammai = 1./20.00
#    gammad = 1./10.38
    gammaih =  1./15.88
    theta1 = 0.197
    delta1 = 0.75
    delta2 = 0.75

    P0 = [N-6, 0, 6, 0, 0, 0]
    Nt = integrate.odeint(SIRode, P0, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))

    INt = [row[2] for row in Nt]

    difference = cases - INt

    LL = np.dot(difference, difference)

    return LL

x0 = [betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad]


###constraints
cons = (    {'type': 'ineq', 'fun': lambda x: x[0]},
         {'type': 'ineq', 'fun': lambda x: x[1]},
         {'type': 'ineq', 'fun': lambda x: x[2]},
        {'type': 'ineq', 'fun': lambda x: x[3]},
{'type': 'ineq', 'fun': lambda x: x[4]}, 
{'type': 'ineq', 'fun': lambda x: x[5]}, 
{'type': 'ineq', 'fun': lambda x: x[6]}, 
{'type': 'ineq', 'fun': lambda x: x[7]}, 
{'type': 'ineq', 'fun': lambda x: x[8]},          
          )

results = minimize(LLode, x0,constraints=cons, method='COBYLA', options={'tol': 1e-8})


print results.x

estParams = results.x

betaI = estParams[0]
betaH = estParams[1]
betaF = estParams[2]
alpha = estParams[3]
gammah = estParams[4]
gammadh = estParams[5]
gammaf = estParams[6]
gammai = estParams[7]
gammad = estParams[8]

Nt = integrate.odeint(SIRode, P, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))

INt = [row[2] for row in Nt]
#
py.clf()
py.plot(days, cases, 'o')
py.plot(days, INt)
py.show()
