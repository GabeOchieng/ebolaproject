Functions
=========

calc_interventions
^^^^^^^^^^^^^^^^^^
::

	Source Code: tools.py

|	Returns a *ModelParams* object. Calculates the values for the interventions to use in the analysis based on the parameters called for computation. Constraint information is taken from *MyConstraints* and *OrigParams* is an instance of *StochLib.ModelParams* that is taken to generate ModifiedParams.
|
|	Input Arguments:
|		*alloc* = an array containing specified values for the resource allocation to be implemented
|		*OrigParams* = *ModelParams* object holding parameters before interventions are applied to the simulation model
|		*MyConstraints* = *Constraints* object holding constraints information
|
|	Output:   
|		*ModifiedParams* = new *ModelParams* object holding parameters after interventions are applied to the simulation model


calc_needed_resources
^^^^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

|	Returns an array listing of needed_resources. The function checks to make sure that the total given is not so large that optimization is pointless.
|	Arguments:
|
|	Input Arguments:
|		*MyConstraints* = *Constraints* object holding constraints information
|		*OrigParams* = *ModelParams* object holding parameters before interventions are applied to the simulation model
|	    
|	Output:
|	    *needed_resources* = array of resource allocation


constraints_help
^^^^^^^^^^^^^^^^^^
::

	Source Code: constraints.py

Prints the intervention options. Describes the meanings of the parameters applied. Takes no arguments.


fit_params
^^^^^^^^^^
::

	Source Code: modelfit.py

|	Returns an object containing the list of parameters for a specific country.
|
|	Input Arguments:
|		*data_file* = data file of cases vs. time for various countries
|		*country* = specified country based on Ebola data, 
|		*N* = value, size of the total population of susceptible persons
|
|	Keyword Arguments:
|		*plot_fit* = False (Default), plots data fitting figure in window
|			       = True, plotting option is ignored

	
get_data_path
^^^^^^^^^^^^^
::

	Source Code: __init__.py

|	Returns the *path* directory of the built-in data. It is used to generate the *path* directory of the constraints and cases default files.
|
|	Input Arguments:
|		*path* = name of the file in the data directory
|
|	Output: 
|		*path* = full path of the data file
 

parse_data
^^^^^^^^^^
::

	Source Code: modelfit.py

|	Returns an array listing of the day and cases associated with that particular day for a specific country. The function takes the directory listing of the file path of the raw data csv file and extracts the number of cases versus time for a given country. Requirement: country name should match the string in the .csv file.
|	
|	Input Arguments:
|		*filename* = input file with country string header, must be in .csv format
|		*country* = specified country based on Ebola data
|	
|	Outputs:
|		*days* = array listing for the specific day containing data on the number of cases
|		*cases* = array listing containing the number of cases reported


plot_output
^^^^^^^^^^^
::

	Source Code: plot.py

|	Generates a figure plot in a window. Data from the simulations run for the optimized option with interventions and the no intervention simulation is plotted for comparison.
|
|	Keyword Arguments:
|		*out_noiv_file* = output file: no interventions applied, *format=.csv*
|		*out_iv_file* = output file: interventions applied, *format=.csv*
|		*figure_file* = output figure file, *format = .png*


print_heading
^^^^^^^^^^^^^
::

	Source Code: tools.py

|	Prints the header line saying what the interventions are.
|
|	Input Argument:
|		*MyConstraints* = *Constraints* object holding constraints parameters


print_output
^^^^^^^^^^^^
::

	Source Code: tools.py

|	Prints a formatted output display to the screen for the runs displaying the resource allocation and costs.
|
|	Input Arguments:
|		*alloc* = an array containing specified values for the resource allocation implemented
|		*cost* = value, number of deaths
|
| 	Keyword Arguments:
|		*linenum* = empty string (Default), line number printing is ignored
|			      = number string, prints line numbers for the table output display on the screen


optimize
^^^^^^^^
::

	Source Code: __init__.py

|	Returns optimized *final_cost* with interventions applied to the model. A combined optimized analysis (using **optimize_with_setup** and **setup_model**) is then performed and the generated values are sent to the output files.
|
|	Keywords Arguments:
|		*disp* = True (Default), prints every step of the optimization
|			   = False
|		*out_noiv_file* = output file: no interventions applied, *format=.csv*
|		*out_iv_file* = output file: interventions applied, *format=.csv*
|		*figure_file* = output figure file, *format = .png*
|		*plot* = True (Default), generates the final plot in a pop-out window
|			   = False
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*data_file* = data file of cases vs. time for various countries
|		*plot_fit* = True (Default), plots data fitting figure in window
|			       = False, plotting option is ignored
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*trajectories* = value; number of times the stoachstic simulation is run for consistency and stability
|		*constraints_file* = constraints filename of a csv file with total budget and intervention time and costs
|		*N* = value, size of the total population of susceptible persons
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: eg. ["theta_1", "delta_2"]
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*S_init* = value; initial values for the number of susceptible individuals
|		*H_init* = value; initial values for the number of hospitalized cases
|		*F_init* = value; initial values for the number of cases who are dead but not yet buried
|		*R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		*E_init* = value; initial values for the number of exposed individuals
|		*country* = specified country based on Ebola data, Default = “Sierra Leone”
|				  = other options: “Liberia”, “Guinea”
|		*t_final* = value; limit of time series data calculated in days
|
|	Output:    		
|		*final_cost* = value, death metric of associated cost (number of dead people) after optimized simulation

	
optimize_with_setup
^^^^^^^^^^^^^^^^^^^
::

	Source Code: __init__.py

|	Returns the *xmin* and *final_cost*.  This function computes the *final_cost* values after optimization has been performed based on the parameters given from setup_model.
|
|	Input Arguments:
|		*alloc* = an array containing specified values for the resource allocation implemented
|		*params* = a tuple of selected Ebola parameter objects specific to the *country* option selected
|
|	Keyword Arguments:
|		*disp* = True (Default), prints every step of the optimization
|			   = False
|		*out_noiv_file* = output file: no interventions applied, *format=.csv*
|		*out_iv_file* = output file: interventions applied, *format=.csv*
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*plot* = True (Default), generates the final plot in a pop-out window
|			   = False
|		*figure_file* = output figure file, *format = .png*
|
|	Output:    		
|		*xmin* = value, optimized resource allocation/distribution
|		*final_cost* = value, death metric of associated cost (number of dead people) after optimized simulation


run_no_interventions
^^^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

|	Returns *cost* when there have been no interventions applied to the model.  A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied.
|
|	Input Arguments:
|		*OrigParams* = object of parameters before interventions are applied to the simulation model
|		*StochParams* = object containing parameters for stochastic modelling
|		*out_file* = name of simulation output file
|
|	Keyword Argument:
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|
|	Output:    		
|		*cost* = value, death metric of associated cost (number of dead people) after optimized simulation


run_optimization
^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

|	Returns the optimized *final_cost* and resource allocation associated with the *final_cost*.  This function computes the *final_cost* values after optimization has been performed based on the parameters given from *StochParams*. Error handling is performed for values that correspond to cases where optimization is not needed.
|
|	Input Arguments:
|		*OrigParams* = object of parameters before interventions are applied to the simulation model
|		*StochParams* = object containing a list of parameters for stochastic modelling
|		*MyConstraints* = constraints object in a file of praters generated from the *Constraints* object
|		*disp* = True or False, whether to generates the plot profile in a pop-out window
|		*out_file* = name of simulation output file
|
|	Keyword Argument:
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|
|	Output:    		
|		*final_cost* = value, death metric for computing associated cost (number of dead people) after optimized simulation 



run_simulation
^^^^^^^^^^^^^^
::

	Source Code: __init__.py
  
|	Returns *final_cost* with/without interventions applied to the model based on an updated params listing. A combined optimized stochastic analysis (using **run_simulation_with_setup** and **setup_model**) is then performed using the input arguments given and specific intervention applied. A figure plot for the trends when interventions have been applied compared to when interventions are not applied is generated. The figure is then saved to an output file.
|
|	Input Arguments:
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|
|	Keyword Arguments:
|		*out_noiv_file* = "out_noiv.csv" (Default). Output file: no interventions applied, *format=.csv*
|		*out_iv_file* = "out_iv.csv" (Default). Output file: interventions applied, *format=.csv*
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*plot* = True (Default), generates the plot profile in a pop-out window
|			   = False
|		*figure_file* = output figure file, *format = .png*
|		*data_file* = data file of cases vs. time for various countries
|		*plot_fit* = True (Default), plots data fitting figure in window
|			       = False, plotting option is ignored
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*trajectories* = value; number of times the stoachstic simulation is run for consistency and stability
|		*constraints_file* = constraints filename of a csv file with total budget and intervention time and costs
|		*N* = value, size of the total population of susceptible persons
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: eg. ["theta_1", "delta_2"]
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*S_init* = value; initial values for the number of susceptible individuals
|		*H_init* = value; initial values for the number of hospitalized cases
|		*F_init* = value; initial values for the number of cases who are dead but not yet buried
|		*R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		*E_init* = value; initial values for the number of exposed individuals
|		*country* = specified country based on Ebola data, Default = “Sierra Leone”
|				  = other options: “Liberia”, “Guinea”
|		*t_final* = value; limit of time series data calculated in days
|
|	Output:    		
|		*final_cost* = value, death metric of associated cost (number of dead people) after optimized simulation


run_simulation_with_setup
^^^^^^^^^^^^^^^^^^^^^^^^^
::

	Source Code: __init__.py
  
|	Returns *final_cost* with/without interventions applied to the model. An optimized stochastic analysis is then performed using the input arguments given and the result is generated. A figure plot for the trends when interventions have been applied compared to when interventions are not applied is generated. The figure is then saved to an output file.
|
|	Input Arguments:
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|		*params* = tuple of parameters (the output from *setup_model*)
|
|	Keyword Arguments:
|		*out_noiv_file* = "out_noiv.csv" (Default). Output file: no interventions applied, *format=.csv*
|		*out_iv_file* = "out_iv.csv" (Default). Output file: interventions applied, *format=.csv*
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*plot* = True (Default), generates the plot profile in a pop-out window
|			   = False
|		*figure_file* = output figure file, *format = .png*
|
|	Output:    		
|		*final_cost* = value, death metric for computing associated cost (number of dead people) after optimized simulation 


run_with_interventions
^^^^^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py
  
|	Returns *cost* when interventions have been applied to the model. A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied. An array printout of *MyConstraints* and resource allocation with cost values are generated for output into *out_file*.
|
|	Input Arguments:
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|		*OrigParams* = list of parameters before interventions are applied to the simulation model
|		*StochParams* = object containing a list of parameters for stochastic modelling
|		*MyConstraints* = constraints object in a file of praters generated from the *Constraints* object
|		*out_file* = name of simulation output file
|
|	Keyword Argument:
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|
|	Output:    		
|		*cost* = value, death metric of associated cost (number of dead people) after optimized simulation


setup_constraints
^^^^^^^^^^^^^^^^^
::

	Source Code: constraints.py
  
|	Returns an *MyConstraints* object to be used for subsequent analysis. Filters constraints with the *valid_interventions* keyword so that optimization is only run over the specified valid interventions.
|
|	Input Arguments:
|		*filename* = input file with parameters to be parsed, *format: .csv*
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: e.g. ["theta_1", "delta_2"]
|
|	Output:    		
|		*MyConstraints* = *Constraints* object holding the relevant parameters


setup_model
^^^^^^^^^^^
::

	Source Code: __init__.py

|	Returns *params*, a tuple of selected parameters specific to the country option selected. The Ebola model chosen is then used for the deterministic and stochastic simulation.
|
|	Keyword Arguments:
|		*data_file* = data file of cases vs. time for various countries
|		*plot_fit* = True (Default), plots data fitting figure in window
|			       = False, plotting option is ignored
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*trajectories* = value; number of times the stoachstic simulation is run for consistency and stability
|		*constraints_file* = constraints filename of a csv file with total budget and intervention time and costs
|		*N* = value, size of the total population of susceptible persons
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: eg. ["theta_1", "delta_2"]
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*S_init* = value; initial values for the number of susceptible individuals
|		*H_init* = value; initial values for the number of hospitalized cases
|		*F_init* = value; initial values for the number of cases who are dead but not yet buried
|		*R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		*E_init* = value; initial values for the number of exposed individuals
|		*country* = specified country based on Ebola data, Default = “Sierra Leone”
|				  = other options: “Liberia”, “Guinea”
|		*t_final* = value; limit of time series data calculated in days
|
|	Output:    		
|		*params* = a tuple of selected Ebola parameter objects specific to the *country* option selected


setup_stoch_params
^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

|	Returns an object *StochParams*. This function initializes the parameters for optimization run from the Stochpy library of parameters generated from the stochastic computation previously done. All paramaters defined here are consistent with the *Legrand, J. et al (2006)* paper.
|
|	Input Arguments:
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*Trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*S_init* = value; initial values for the number of susceptible individuals
|		*H_init* = value; initial values for the number of hospitalized cases
|		*F_init* = value; initial values for the number of cases who are dead but not yet buried
|		*R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		*E_init* = value; initial values for the number of exposed individuals
|		*t_final* = value; limit of time series data calculated in days
|
|	Output:    		
|		*StochParams* = object containing parameters for stochastic modelling
