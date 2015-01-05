# Wrapper functions for convenient user interface.

import numpy
from ebolaopt.optimizer import Optimizer
import StochCalc.StochLib as StochLib
from ebolaopt.modelfit import fit_params

def optimize(plot=True, **kwds):
    """This method runs the data fitting, optimization, printing, and plotting.
    
    Keyword arguments:
        data_file -- path to raw data csv file 
        constraints_file --
        FINISH THIS"""

    def filter_kwds(kwd_names):
        kwds_subset = {}
        for key in kwd_names:
            if kwds.has_key(key):
                kwds_subset[key] = kwds[key]
        return kwds_subset
    
    opt_kwds = ['data_file', 'constraints_file', 'country']
    stoch_kwds = ['N_samples', 'trajectories', 't_final', 'I_init', 'S_init', \
                  'valid_interventions', 'epidemic_file_no_iv']
    run_kwds = ['disp', 'epidemic_file_opt_iv']
    myopt = Optimizer(**filter_kwds(opt_kwds)) # Create a new optimizer object
    myopt.initialize_model() # Do the deterministic fitting
    myopt.initialize_stoch_solver(**filter_kwds(stoch_kwds)) # Initialize stochastic model
    optimum, cost = myopt.run_optimization(**filter_kwds(run_kwds)) # Calculate!

    if plot:
        myopt.plot_output()

    return optimum, cost


def fit_data(data_file, country, N, plot=False):
    """Only fit the raw epidemic trajectory data."""
    OrigParams = fit_params(data_file, country, N, plot=False)
    print repr(OrigParams)
    return OrigParams