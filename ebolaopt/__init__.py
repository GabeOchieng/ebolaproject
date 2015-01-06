# Wrapper functions for convenient user interface.

import numpy
from ebolaopt.optimizer import Optimizer
import StochCalc.StochLib as StochLib
from ebolaopt.modelfit import fit_params

from ebolaopt.constraints import constraints_help
from ebolaopt.plot import plot_output

def optimize(plot=True, out_figure="epidemic.png", **kwds):
    """This method runs the data fitting, optimization, printing, and plotting."""

    def filter_kwds(kwd_names):
        kwds_subset = {}
        for key in kwd_names:
            if kwds.has_key(key):
                kwds_subset[key] = kwds[key]
        return kwds_subset
    
    opt_kwds = ['data_file', 'constraints_file', 'country']
    model_kwds = ['plot_fit']
    stoch_kwds = ['N_samples', 'trajectories', 't_final', 'I_init', 'S_init', \
                  'valid_interventions', 'epidemic_file_no_iv']
    run_kwds = ['disp', 'epidemic_file_opt_iv']
    myopt = Optimizer(**filter_kwds(opt_kwds)) # Create a new optimizer object
    myopt.initialize_model(**filter_kwds(model_kwds)) # Do the deterministic fitting
    myopt.initialize_stoch_solver(**filter_kwds(stoch_kwds)) # Initialize stochastic model
    optimum, cost = myopt.run_optimization(**filter_kwds(run_kwds)) # Calculate!

    #XXX Inelegant, fix me?
    if plot:
        if 'epidemic_file_no_iv' in kwds:
            epidemic_file_no_iv=kwds['epidemic_file_no_iv']
        else:
            epidemic_file_no_iv="epidemic_no_iv.csv"
        if 'epidemic_file_opt_iv' in kwds:
            epidemic_file_opt_iv=kwds['epidemic_file_opt_iv']
        else:
            epidemic_file_opt_iv="epidemic_opt_iv.csv"
        plot_output(epidemic_file_no_iv=epidemic_file_no_iv, \
                     epidemic_file_opt_iv=epidemic_file_opt_iv, \
                     out_figure=out_figure)

    return optimum, cost

def fit_data(data_file, country, N, plot_fit=False):
    """Only fit the raw epidemic trajectory data."""
    OrigParams = fit_params(data_file, country, N, plot_fit=plot_fit)
    print repr(OrigParams)
    return OrigParams