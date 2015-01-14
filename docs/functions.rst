Functions
===============

calc_interventions
^^^^^^^^^^^^^^^^^^
::

	Source Code: tools.py

Returns the ModifiedParams results taken from the StochCalc.ModelParamList . Calculates the values for the interventions to use in the analysis based on the parameters called for computation. Constraint information is taken from MyConstraints and OrigParams in StochLib.pyModelParams() is taken to generate ModifiedParams. Parameters used are "theta_1", "delta_1", "delta_2" which correspond to xxx.
	alloc = values
	OrigParams = list of parameters
MyConstraints = keyword

check_total
^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

Returns an array listing of needed_resources. The function checks to make sure that the total given is not so large that optimization is pointless.
	total = value, must be less than 100,000.
needed_resources = array listing of parameters for optimization
	OrigParams = list of parameters
MyConstraints = keyword


constraints_help
^^^^^^^^^^^^^^^^^^
::

	Source Code: constraints.py

Returns the parameters used. A help file to describe the meanings of the parameters applied, the allowable range of values for each constraint and acceptable formatting. Takes no arguments.
"theta_1" = "fraction of infected cases diagnosed and hospitalized", value < 10
"beta_H" = "contact rate for hospitalized cases", 1 < value < 17
"delta_2" = "fatality rate of hospitalized patients", 2 < value < 40


fit_params
^^^^^^^^^^^
::

	Source Code: modelfit.py

Returns an array listing containing the list of parameter for a specific country. 
		N= array listing of parameters from Legrand paper, values must be float
days = array listing for the specific day containing data on the number of cases
	cases = array listing containing the number of cases reported

	
get_data_path
^^^^^^^^^^^
::

	Source Code: __init__.py

Returns the path directory. The data_file_default and constraints_file_default are also generated for their respective directories.
	path = directory listing of the files
 
 
Commands from modelfit.py:
LLode(x):
Returns OrigParams. The parameters are first initialized using guesses of the values. The guessed values are then fit with the data, integrated, and then the error of the initial guesses are minimized. Optimal parameters are then generated for use in the computation after the process is iterated until the error is below one percent. All parameter definitions are consistent with the Legrand paper.
N= array listing of parameters from Legrand paper, values must be float
OrigParams = list of parameters


parse_data
^^^^^^^^^^^
::

	Source Code: modelfit.py

Returns an array listing of the day and cases associated with that particular day for s specific country. The function takes the directory listing of the file path of the raw data csv file and extracts the number of cases versus time for a given country. Requirement: country name should match the string in the .csv file.
	filename = input file with country string header, must be in .csv format
	days = array listing for the specific day containing data on the number of cases
	cases = array listing containing the number of cases reported

plot_output
^^^^^^^^^^^
::

	Source Code: plot.py

Returns a figure plot in a window. Data from the simulations run for the optimized option with interventions and the no intervention simulation is plotted for comparison.
out_noiv_file= output file: no interventions, format=.csv
out_iv_file= output file: interventions applied, format=.csv
plot=False (Default)
	= True (generates the plot profile in a pop-out window)
figure_file = output figure file, format = .png


print_heading
^^^^^^^^^^^
::

	Source Code: tools.py

Prints the constraint values used for the interventions applied. 
MyConstraints = keyword


print_output
^^^^^^^^^^^^
::

	Source Code: tools.py

Makes an array from the alloc given from the interventions allocation percentages and cost associated with each allocation. The number of lines printed to the output is based on the value of linenum.
	alloc = values
	cost = values
	linenum = “” (Default, prints all lines)
		= number (Prints until that line number is reached) 

optimize
^^^^^^^^^^^^
::

	Source Code: __init__.py

Returns optimized final_cost with applied to the model. A optimization analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied. Generated values are sent to the output files.
alloc = values
params = array listing of OrigParams, StochParams, MyConstraints
OrigParams = list of parameters
MyConstraints = keyword
	StochParams = list of parameters from the stochastic analysis
	out_noiv_file= output file: no interventions, format=.csv
out_iv_file= output file: interventions applied, format=.csv
n_threads=1 (Number of processors to use, OpenMP Parallelization)
disp=False (Default)
	= True (generates the plot profile in a pop-out window)
figure_file = output figure file, format = .png
plot=False (Default)
	= True (generates the plot profile in a pop-out window)


	
optimize_with_setup
^^^^^^^^^^^^
::

	Source Code: __init__.py

Returns the optimized final_cost and resource allocation associated with the final_cost.  This function computes the final_cost values after optimization has been performed based on the parameters given from setup_model.
	params = array listing of OrigParams, StochParams, MyConstraints
OrigParams = list of parameters
MyConstraints = keyword
	StochParams = list of parameters from the stochastic analysis
	out_noiv_file= output file: no interventions, format=.csv
out_iv_file= output file: interventions applied, format=.csv
n_threads=1 (Number of processors to use, OpenMP Parallelization)
disp=False (Default)
	= True (generates the plot profile in a pop-out window)
figure_file = output figure file, format = .png


SIRode
^^^^^^^^^^^^
::

	Source Code: modelfit.py

Returns an interpolated value based on the specific fit ordinary differential equation (ODE) equation. The ODE equation is then integrated to generate discrete values for the time series data taken from the array listing file containing days and cases. All parameters listed for this equation are consistent with the parameters used in the Legrand paper.
N= array listing of parameters from Legrand paper, values must be float


run_no_interventions
^^^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

Returns cost when there have been no interventions applied to the model.  A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied.
	alloc = values
cost = value
	OrigParams = list of parameters
MyConstraints = keyword
StochParams = list of parameters from the stochastic analysis
n_threads=1 (Number of processors to use, OpenMP Parallelization)
out_file = “NONE” (Default), other option generates and output text file
t_interventions = value, must be at least zero


run_optimization
^^^^^^^^^^^^
::

	Source Code: run_simulations.py

Returns the optimized final_cost and resource allocation associated with the final_cost.  This function computes the final_cost values after optimization has been performed based on the parameters given from StochParams. Error handling is performed for values that do not correspond to cases where optimization is not needed.
alloc = values
	cost = value
	final_cost = value generated after optimization is performed if needed
OrigParams = list of parameters
MyConstraints = keyword
disp=False (Default)
	= True (generates the plot profile in a pop-out window)
	StochParams = list of parameters from the stochastic analysis
n_threads=1 (Number of processors to use, OpenMP Parallelization)
out_file = “NONE” (Default), other option generates and output text file
t_interventions = value, must be at least zero


run_simulation
^^^^^^^^^^^^
::

	Source Code: __init__.py
  
Returns final_cost with/without interventions applied to the model based on an updated params listing. A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied. A figure plot for the trends when interventions have been applied compared to when interventions are not applied is generated. The figure is then saved to an output file.
alloc = values
params = array listing of OrigParams, StochParams, MyConstraints
OrigParams = list of parameters
MyConstraints = keyword
	StochParams = list of parameters from the stochastic analysis
	out_noiv_file= output file: no interventions, format=.csv
out_iv_file= output file: interventions applied, format=.csv
n_threads=1 (Number of processors to use, OpenMP Parallelization)
plot=False (Default)
	= True (generates the plot profile in a pop-out window)
figure_file = output figure file, format = .png


run_simulation_with_setup
^^^^^^^^^^^^^^^^^^^^^^^^^
::

	Source Code: __init__.py
  
|	Returns final_cost with/without interventions applied to the model. A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied. A figure plot for the trends when interventions have been applied compared to when interventions are not applied is generated. The figure is then saved to an output file.
|		alloc = values
|		params = array listing of OrigParams, StochParams, MyConstraints
|		OrigParams = list of parameters
|		MyConstraints = keyword
|		StochParams = list of parameters from the stochastic analysis
|		out_noiv_file= output file: no interventions, format=.csv
|		out_iv_file= output file: interventions applied, format=.csv
|		n_threads=1 (Number of processors to use, OpenMP Parallelization)
|		plot=False (Default)
|			= True (generates the plot profile in a pop-out window)
|		figure_file = output figure file, format = .png


run_with_interventions
^^^^^^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py
  
|	Returns *cost* when interventions have been applied to the model. A stochastic analysis is then performed using the input arguments given and the result generated is the cost associated with a specific intervention applied. An array printout of *MyConstraints* and resource allocation with cost values are generated for output into *out_file*.
|
|	Inputs:
|		*alloc* = an array list containing specified values for the resource allocation to be implemented
|		*OrigParams* = list of parameters before interventions are applied to the simulation model
|		*StochParams* = object containing a list of parameters for stochastic modelling
|		*MyConstraints* = constraints object in a file of praters generated from the *Constraints* object
|		*n_threads* = 1 (Default), Number of processors to use, OpenMP Parallelization
|		*out_file* = “NONE” (Default), other option generates and output text file
|
|	Output:    		
|		*cost* = value, cost associated with improving an intervention with no optimization applied


setup_constraints
^^^^^^^^^^^^^^^^^^
::

	Source Code: constraints.py
  
|	Returns all the *MyConstraints* object to be used for subsequent analysis. It checks to make sure that valid constraints are selected and used as input for the analysis.
|
|	Inputs:
|		*filename* = input file (constraints_file_default) to parse the parameters, *format: .csv*
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: eg. ["theta_1", "delta_2"]
|
|	Output:    		
|		*MyConstraints* = constraints object in a file of praters generated from the *Constraints* object


setup_model
^^^^^^^^^^^^
::

	Source Code: __init__.py

|	Returns *params*, a tuple of selected parameters specific to the country option selected. The Ebola model chosen is then used for the deterministic and stochastic simulation.
|
|	Inputs:
|		*data_file* = default data file used to find the path directory
|		*plot_fit* = True (Default), plots data fitting figure in window
|			       = False, plotting option is ignored
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		*constraints_file* = default constraints file used to find the path directory
|		*N* = value, size of the total population of susceptible persons
|		*valid_interventions* = array listing of all interventions applicable, Default = ‘all’; other options: eg. ["theta_1", "delta_2"]
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*country* = specified country based on Ebola data, Default = “Sierra Leone”
|				  = other options: “Liberia”, “Guinea”
|		*t_final* = value; limit of time series data calculated in days|
|
|	Output:    		
|		*params* = a tuple of selected Ebola objects specific to the *country* option selected


setup_stoch_params
^^^^^^^^^^^^^^^^^^
::

	Source Code: run_simulations.py

|	Returns an object *StochParams*. This function initializes the parameters for optimization run from the Stochpy library of parameters generated from the stochastic computation previously done. All paramaters defined here are consistent with the *Legrand, J. et al (2006)* paper.
|
|	Inputs:
|		*N_samples* = value; number of times to sample the stochastic run to query results for generating the output
|		*Trajectories* = value; number of times the stoachstic simulation is run for a consistency and stability
|		*I_init* = value; initial values for the number of infectious cases in the community
|		*S_init* = value; initial values for the number of susceptible individuals
|		*H_init* = value; initial values for the number of hospitalized cases
|		*F_init* = value; initial values for the number of cases who are dead but not yet buried
|		*R_init* = value; initial values for the number of individuals removed from the chain of transmission
|		*E_init* = value; initial values for the number of exposed individuals
|		*t_final* = value; limit of time series data calculated in days|
|
|	Output:    		
|		*StochParams* = object containing a list of parameters for stochastic modelling
