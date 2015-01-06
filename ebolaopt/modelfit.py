# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:12:38 2014

@author: yile
"""
from scipy.optimize import minimize
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv
import ebolaopt.StochCalc.StochLib as StochLib

#####Getting the Data: Days and Cumulative Infected Cases####
def parse_data(filename, country):
    """Given the file path of the raw data csv file, extract the number of cases
        vs. time for a given country. country name should match string in csv file.
        """
    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile)
        # First row
        firstrow = datareader.next()
        if country in firstrow is False:
            raise ValueError("Please enter a valid country name.")
        col_ind = firstrow.index(country)
        
        cases = []
        days = []
        # Iterate over subsequent rows
        for row in datareader:
            if len(row) > 1:
                count = row[col_ind]
                if count: # If it is not empty
                    count = int(count)
                    # Convert date to an integer representing days
                    day = int(datetime.datetime.strptime(row[0], '%Y-%m-%d').strftime('%j'))
                    days.append(day)
                    cases.append(count)
        days = np.array(days)
        cases = np.array(cases)
    
    return days, cases

def fit_params(data_file, country, N, plot=False):
    #Ensure F to be a float
    N=float(N)    
    #reading file data for a given country
    days, cases = parse_data(data_file, country)
    ##Setting Up Initial Conditions for Parameters 
    betaI = 0.128
    betaH = 0.08
    betaF = 0.111
    alpha = 1./10
    #gammah = 1./4.12
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
    
    P = [N, 10, 0, 0, 0, 0]
    Nt = integrate.odeint(SIRode, P, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))
    
    NI = [row[2] for row in Nt]
    NH = [row[3] for row in Nt]
    NF = [row[4] for row in Nt]
    NR = [row[5] for row in Nt]
    
    NI = np.array(NI)
    NH = np.array(NH)
    NF = np.array(NF)
    NR = np.array(NR)
    
    if plot:
        plt.clf()
        plt.plot(days, cases, 'o',label = 'Data')
        plt.plot(days, NI+NH+NF+NR,'r--',label = 'Before Optimization')
        
    ###Model Fitting
    
    def LLode(x):
        
        betaI = x[0]
        betaH = x[1]
        betaF = x[2]
        alpha = x[3]
        gammah = x[4]
        gammadh = x[5]
        gammaf = x[6]
        gammai = x[7]
        gammad = x[8]
        gammaih = x[9]
        theta1 = x[10]
        delta1 = x[11]
        delta2 = x[12]
    
        Nt = integrate.odeint(SIRode, P, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))
    
        NI = [row[2] for row in Nt]
        NH = [row[3] for row in Nt]
        NF = [row[4] for row in Nt]
        NR = [row[5] for row in Nt]
         
        NI = np.array(NI)
        NH = np.array(NH)
        NF = np.array(NF)
        NR = np.array(NR)
        difference = cases - (NI + NH + NF + NR)
    
        LL = np.dot(difference, difference)
    
        return LL
    
    
    x0 = [betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2]
    
    
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
    {'type': 'ineq', 'fun': lambda x: x[9]}, 
    {'type': 'ineq', 'fun': lambda x: x[10]}, 
     {'type': 'ineq', 'fun': lambda x: -x[10]+1}, 
    {'type': 'ineq', 'fun': lambda x: x[11]}, 
     {'type': 'ineq', 'fun': lambda x: -x[11]+1}, 
    {'type': 'ineq', 'fun': lambda x: x[12]},  
     {'type': 'ineq', 'fun': lambda x: -x[12]+1},       
              )
    
    results = minimize(LLode, x0,constraints=cons, method='COBYLA')
    
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
    gammaih = estParams[9]
    theta1 = estParams[10]
    delta1 = estParams[11]
    delta2 = estParams[12]
    
    Nt = integrate.odeint(SIRode, P, days, args=(N, betaI, betaH, betaF, alpha, gammah, gammadh, gammaf, gammai, gammad, gammaih, theta1, delta1, delta2))
    
    NI = [row[2] for row in Nt]
    NH = [row[3] for row in Nt]
    NF = [row[4] for row in Nt]
    NR = [row[5] for row in Nt]
    
    NI = np.array(NI)
    NH = np.array(NH)
    NF = np.array(NF)
    NR = np.array(NR)
    
    if plot:
        plt.plot(days, NI+NH+NF+NR,'k',label = 'After Optimization')
        plt.legend()
        plt.title('Model Parameter Fitting')
        plt.xlabel('Time (Days)')
        plt.ylabel('Cumulative Infections ')
        plt.show()
    
    OrigParams = StochLib.pyModelParams()
    OrigParams.set("beta_I", estParams[0])
    OrigParams.set("beta_H", estParams[1])
    OrigParams.set("beta_F", estParams[2])
    OrigParams.set("alpha", estParams[3])
    OrigParams.set("gamma_h", estParams[4])
    OrigParams.set("gamma_f", estParams[6])
    OrigParams.set("gamma_i", estParams[7])
    OrigParams.set("gamma_d", estParams[8])
    OrigParams.set("theta_1", estParams[10])
    OrigParams.set("delta_1", estParams[11])
    OrigParams.set("delta_2", estParams[12])
    return OrigParams
