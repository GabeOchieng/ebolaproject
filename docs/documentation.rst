Documentation
===============

Functions
------------

print_heading(MyConstraints):
^^^^^^^^^^^^^^^

Class Objects
--------------

cost_function:
^^^^^^^^^^^^^^^


Constraints(filename)
^^^^^^^^^^^^^^^^^^^^^^^


ModelParams
^^^^^^^^^^^^^^^
Source Code: *ModelParams.h*

|	Returns an array of parameters from the Ebola modelling data in *Legrand, J. et al (2006)*. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|		double *beta_I* = value; transmission coefficient in the community
|		double *beta_H* = value; transmission coefficient at the hospital
|		double *beta_F* = value; transmission coefficient during funerals
|		double *alpha* = value; the inverse of the mean duration of the incubation period
|		double *gamma_h* = value; the mean duration from symptom onset to hospitalization
|		double *theta_1* = value; the percentage of infectious cases are hospitalized
|		double *delta_1* = value; ratio 1 computed in order that the overall case-fatality ratio is *delta*
|		double *delta_2* = value; ratio 2 computed in order that the overall case-fatality ratio is *delta*
|		double *gamma_f* = value; the mean duration from death to burial
|		double *gamma_i* = value; the mean duration of the infectious period for survivors
|		double *gamma_d* = value; the mean duration from hospitalization to death



StochParams
^^^^^^^^^^^^^^^
Source Code: *StochParams.h*

|	Returns an object containing a list of parameters for stochastic modelling. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|		int *N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		int *Trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		int *I_init* = value; initial values for the number of infectious cases in the community
|		int *S_init* = value; initial values for the number of susceptible individuals
|		int *H_init* = value; initial values for the number of hospitalized cases
|		int *F_init* = value; initial values for the number of cases who are dead but not yet buried
|		int *R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		int *E_init* = value; initial values for the number of exposed individuals
|		double *t_final* = value; limit of time series data calculated in days




ModelParams:
^^^^^^^^^^^^^



StochCalc:
^^^^^^^^^^^^^