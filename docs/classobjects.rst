Class Objects
===============
The class objects used for the Ebola Disease modelling were created to store data parameters. These objects support both attribute references and instantiation (valid attribute names, data attributes and methods).


Constraints
^^^^^^^^^^^^^^^
::

	Source Code: constraints.py

|	A callable object to hold optimization parameters: total resources, resource costs and effects, and time to start interventions.
|
|	Inputs:
|		*filename* = input file (constraints_file_default) to parse the parameters, format: .csv
|		*total* = value, total budget based on the number of resources to allocate
|		*cost* = value, cost associated with improving an intervention with no optimization applied
|		*t_interventions* = value, time before/after *t_final*  for simulations with/without interventions applied respectively
|		*all_interventions* = dictionary of keyword listing and the associated cost and effects


CostFunction
^^^^^^^^^^^^^^^
::

	Source Code: const_function.py

|	Returns a display of print out of resource allocation and cost in real-time computation if disp=True. A callable object that must be minimized as part of the optimization computation based on the interventions, associated costs, and resource allocation.  
|
|	Inputs:
|		*OrigParams* = list of parameters before interventions are applied to the simulation model
|		*StochParams* = object containing a list of parameters for stochastic modelling
|		*MyConstraints* = constraints object in a file of praters generated from the *Constraints* object
|		*disp* = False (Default)
|			   = True, generates the plot profile in a pop-out window
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|		*out_file* = “NONE” (Default), other option generates and output text file     
|		*n* = number assigned to each step during the printout generation   
|
|	Output:    
|		*cost* = value, cost associated with improving an intervention with no optimization applied               


ModelParams
^^^^^^^^^^^^^^^
::

	Source Code: ModelParams.h

|	Returns object containing a list of parameters from the Ebola modelling data in *Legrand, J. et al (2006)* based on the country chosen for running the simulation. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|
|	Inputs:
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


StochCalc
^^^^^^^^^^^
::

	Source Code: StochCalc.h

|	Returns an output file, *OutputFileName* ,  with the Ebola modelling paramters defined. All number values returned are in the *float* format. An output file output is generated with the *StochParams*, *ModelParams*, and *t_interventions* array listing.
|
|	Inputs:
|		*StochParams* = object containing a list of parameters for stochastic modelling
|		*ModelParams* = object containing a list of parameters from the Ebola modelling data for a specific country chosen
|		float *t_interventions* = value, time before/after *t_final*  for simulations with/without interventions applied respectively
|		string (int *nthreads*) = string, number of processors to use for OpenMP Parallelization
|
|	Output:    
|		string *OutputFileName* = output filename, *format: .txt*

StochParams
^^^^^^^^^^^ 
::

	Source Code: StochParams.h

|	Returns an object containing a list of parameters for stochastic modelling. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|
|	Inputs:
|		int *N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		int *Trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		int *I_init* = value; initial values for the number of infectious cases in the community
|		int *S_init* = value; initial values for the number of susceptible individuals
|		int *H_init* = value; initial values for the number of hospitalized cases
|		int *F_init* = value; initial values for the number of cases who are dead but not yet buried
|		int *R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		int *E_init* = value; initial values for the number of exposed individuals
|		double *t_final* = value; limit of time series data calculated in days