Graphical User Interface (GUI) Option
=======================================
The class objects used for the Ebola Disease modelling were created to store data parameters. These objects support both attribute references and instantiation (valid attribute names, data attributes and methods).


Constraints
^^^^^^^^^^^^^^^
::

	Source Code: constraints.py

|	An object to hold optimization parameters: total resources, resource costs and effects, and time to start interventions.
|
|	Inputs:
|		*filename* = name of constraints input file with parameters to be parsed, *format: .csv*
|
|	Attributes:
|		*total* = value, total budget based on the number of resources to allocate
|		*t_interventions* = value, time before/after *t_final*  for simulations with/without interventions applied respectively
|		*all_interventions* = dictionary of interventions listing the associated cost and effects


CostFunction
^^^^^^^^^^^^^^^
::

	Source Code: cost_function.py

|	A callable object that must be minimized as part of the optimization computation based on the interventions, associated costs, and resource allocation.  Displays a print out of resource allocation and cost in real-time computation if disp=True.
|
|	Attributes:
|		*OrigParams* = parameters before interventions are applied to the simulation model
|		*StochParams* = object containing parameters for stochastic modelling
|		*MyConstraints* = *Constraints* object holding intervention information
|		*disp* = False (Default)
|			   = True, prints the allocation and cost at each step of the optimization
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*n* = number assigned to each step during the printout generation
|
|	Inputs:
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|		*out_file* = “NONE” (Default), other option generates and output text file
|
|	Output:    
|		*cost* = value, cumulative deaths resulting from the given resource allocation


ModelParams
^^^^^^^^^^^^^^^
::

	Source Code: ModelParams.h

|	An object containing a list of parameters from the Ebola modelling data in *Legrand, J. et al (2006)* based on the country chosen for running the simulation. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|
|	Attributes:
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
^^^^^^^^^^^ 
::

	Source Code: StochParams.h

|	An object containing a list of parameters for stochastic modelling. The parameters defined are consistent with the parameters defined in *Legrand, J. et al (2006)*.
|
|	Attributes:
|		int *N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		int *Trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		int *I_init* = value; initial values for the number of infectious cases in the community
|		int *S_init* = value; initial values for the number of susceptible individuals
|		int *H_init* = value; initial values for the number of hospitalized cases
|		int *F_init* = value; initial values for the number of cases who are dead but not yet buried
|		int *R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		int *E_init* = value; initial values for the number of exposed individuals
|		double *t_final* = value; limit of time series data calculated in days