# Python2.7
from ebolaopt.modelfit import fit_params
from ebolaopt.constraints import setup_constraints
from ebolaopt.run_simulations import run_no_interventions, run_optimization, \
    run_with_interventions, setup_stoch_params
from ebolaopt.plot import plot_output
import os

# For installation, get actual path to data
# http://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location
def get_data_path(path):
    root_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(root_path, 'data', path)

data_file_default = get_data_path('case_counts.csv')
constraints_file_default = get_data_path('constraints.csv')

def setup_model(data_file=data_file_default, constraints_file=constraints_file_default, \
          plot_fit=True, N_samples=200, trajectories=20, t_final=250., \
          N=200000, I_init=3, valid_interventions='all', country="Sierra Leone"):
    OrigParams = fit_params(data_file, country, N, plot_fit=plot_fit)
    StochParams = setup_stoch_params(N_samples, trajectories, t_final, N, I_init)
    MyConstraints = setup_constraints(constraints_file, valid_interventions)
    params = (OrigParams, StochParams, MyConstraints)
    return params

######################

def optimize_with_setup(params, disp=True, out_noiv_file="out_noiv.csv", \
                        out_iv_file="out.csv", figure_file="out.png", plot=True, \
                        n_threads=1):
    OrigParams, StochParams, MyConstraints = params
    cost_noiv = run_no_interventions(OrigParams, StochParams, out_noiv_file, \
                                     n_threads=n_threads)
    xmin, final_cost = run_optimization(OrigParams, StochParams, MyConstraints, \
                                        disp, out_iv_file, n_threads=n_threads)
    if plot:
        plot_output(out_noiv_file, out_iv_file, figure_file)
    return xmin, final_cost

def run_simulation_with_setup(alloc, params, out_noiv_file="out_noiv.csv", \
                        out_iv_file="out.csv", figure_file="out.png", plot=True, \
                        n_threads=1):
    OrigParams, StochParams, MyConstraints = params
    cost_noiv = run_no_interventions(OrigParams, StochParams, out_noiv_file, \
                                     n_threads=n_threads)
    final_cost = run_with_interventions(alloc, OrigParams, StochParams, \
                                MyConstraints, out_iv_file, n_threads=n_threads)
    if plot:
        plot_output(out_noiv_file, out_iv_file, figure_file)
    return final_cost

######################

def optimize(disp=True, out_noiv_file="out_noiv.csv", \
             out_iv_file="out.csv", figure_file="out.png", plot=True, \
             n_threads=1, **kwds):
    params = setup_model(**kwds)
    xmin, final_cost = optimize_with_setup(params, disp=disp, out_noiv_file=out_noiv_file, \
                        out_iv_file=out_iv_file, figure_file=figure_file, plot=plot, \
                        n_threads=n_threads)
    return xmin, final_cost

def run_simulation(alloc, disp=True, out_noiv_file="out_noiv.csv", \
                   out_iv_file="out.csv", figure_file="out.png", plot=True, \
                   n_threads=1, **kwds):
    params = setup_model(**kwds)
    final_cost = run_simulation_with_setup(alloc, params, out_noiv_file=out_noiv_file, \
                                    out_iv_file=out_iv_file, figure_file=figure_file, \
                                    plot=plot, n_threads=n_threads)
    return final_cost



