# Python2.7
import scipy.optimize
import numpy
from ebolaopt.parse_input import parse_data, parse_resources
from ebolaopt.cost_function import CostFunction

# Intervention parameters: convert from array to dict
def params_array2dict(params_array):
    var_names = ['beta_H', 'delta_2', 'theta_1']
    var_names.sort() # dict keys and values are sorted
    params_dict = {}
    for i, val in enumerate(params_array):
        params_dict[var_names[i]] = val
    return params_dict

# Intervention parameters: convert from dict to array
def params_dict2array(params_dict):
    return numpy.array(params_dict.values())

##############
#XXX Placeholder function for now for Yile's code, which should be imported
def fit_params(data):
    orig_params = {'beta_H': 0.062, 'delta_2': 0.5, 'theta_1': 0.197}
    return params_dict2array(orig_params)
##############

# Default values
default_data = numpy.loadtxt("ebolaopt/data/default_data.txt")
default_resources = {'total': 5000.0, 'interventions': {'beta_H': (100.0, -0.0001), 'delta_2': (500.0, -1e-05), 'theta_1': (2.0, 0.0001)}}

class Optimizer:
    """This is the main overall wrapper class."""

    def __init__(self, data_file=None, resources_file=None, country="Liberia"):
        """Initialize optimizer object and parse input files."""
        # Use default values if none are provided
        if data_file is None:
            self.data = default_data
        else:
            self.data = parse_data(data_file, country)
        
        if resources_file is None:
            self.resources_dict = default_resources
        else:
            self.resources_dict = parse_resources(resources_file)

        return

    def initialize_model(self):
        """Fit the deterministic model parameters."""
        self.orig_params = fit_params(self.data) #XXX first time self.orig_params is defined
        return

    def run_optimization(self, final_time):
        """Call the Scipy optimization function."""
        #XXX Need to warn if self.orig_params is not initialized
        costfunc_object = CostFunction(final_time, self.orig_params, self.resources_dict)
        n = len(self.resources_dict["interventions"].keys())
        x0 = numpy.ones(n)*1./float(n) # Start by distributing resources uniformly
        
        # Set up constraints
        eqcons = [lambda x: numpy.sum(x) - 1.]
        def ineq_maker(index):
            return lambda x: x[index]
        ieqcons = [ineq_maker(i) for i in range(n)]
        xmin = scipy.optimize.fmin_slsqp(costfunc_object, x0, eqcons=eqcons, ieqcons=ieqcons, disp=0)
        return xmin

    def plot_optimum(self):
        """Do plotting."""
        # Sandra's part goes here
        return



