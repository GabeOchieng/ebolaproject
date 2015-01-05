# Wrapper functions for convenient user interface.

import numpy
from ebolaopt.optimizer import Optimizer
import StochCalc.StochLib as StochLib
from ebolaopt.modelfit import fit_params

def optimize(**kwds):
    """This method runs the data fitting and optimization."""
    #XXX How to handle keywords better?
    def filter_kwds(kwd_names):
        kwds_subset = {}
        for key in kwd_names:
            if kwds.has_key(key):
                kwds_subset[key] = kwds[key]
        return kwds_subset
    
    opt_kwds = ['data_file', 'constraints_file', 'country']
    stoch_kwds = ['N_samples', 'trajectories', 't_final', 'I_init', 'S_init']
    run_kwds = ['disp']
    myopt = Optimizer(**filter_kwds(opt_kwds)) # Create a new optimizer object
    myopt.initialize_model() # Do the deterministic fitting
    myopt.initialize_stoch_solver(**filter_kwds(stoch_kwds)) # Initialize stochastic model
    optimum, cost = myopt.run_optimization(**filter_kwds(run_kwds)) # Calculate!
    return optimum, cost

#def run_simulation(StochParams, OrigParams, Constraints, resource_alloc, disp=False):
#    """Only run the simulation for a given set of model parameters."""
#    return
#
def fit_data(data_file, country, N, plot=False):
    """Only fit the raw epidemic trajectory data."""
    OrigParams = fit_params(data_file, country, N, plot=False)
    
    return
#
#def analyze_output():
#    """Do additional output analysis."""
#    return
