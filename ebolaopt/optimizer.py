# Python2.7
import scipy.optimize
import numpy
from ebolaopt.cost_function import CostFunction
from ebolaopt.constraints import Constraints
import ebolaopt.StochCalc.StochLib as StochLib

##############
#XXX Placeholder function for now for Yile's code, which should be imported
def fit_params(data, plot=False):
    OrigParams = StochLib.pyModelParams()
    OrigParams.set("beta_I", 0.16)
    OrigParams.set("beta_H", 0.062)
    OrigParams.set("beta_F", 0.489)
    OrigParams.set("alpha", 1./12.)
    OrigParams.set("gamma_h", 1./3.24)
    OrigParams.set("gamma_f", 1./2.01)
    OrigParams.set("gamma_i", 1./15.)
    OrigParams.set("gamma_d", 1./13.31)
    OrigParams.set("theta_1", 0.197)
    OrigParams.set("delta_1", 0.5)
    OrigParams.set("delta_2", 0.5)
    return OrigParams
##############

class Optimizer:
    """The optimization wrapper class."""

    def __init__(self, data_file=None, constraints_file=None, country="Liberia"):
        """Initialize optimizer object and parse input files."""
        # Use default values if none are provided
        if data_file is None:
            self.data_file = "ebolaopt/data/default_data.txt"
        else:
            self.data_file = data_file
        
        # Create constraints object
        self.Constraints = Constraints(constraints_file)

    def initialize_model(self, plot=False):
        """Fit the deterministic model parameters."""
        self.OrigParams = fit_params(self.data_file, plot=plot)
        self.need_opt, self.needed_resources = self.Constraints.check_total(self.OrigParams)
    
    def initialize_stoch_solver(self, N_samples=200, trajectories=10, \
                               t_final=250., I_init=3, S_init=199997, \
                                epidemic_file_no_iv="epidemic_no_iv.csv", **kwds):
        """Initialize stochastic calculation parameters."""
        self.StochParams = StochLib.pyStochParams()
        self.StochParams.set("N_samples", N_samples)
        self.StochParams.set("Trajectories", trajectories)
        self.StochParams.set("I_init", I_init)
        self.StochParams.set("S_init", S_init)
        self.StochParams.set("H_init", 0)
        self.StochParams.set("F_init", 0)
        self.StochParams.set("R_init", 0)
        self.StochParams.set("E_init", 0)
        self.StochParams.set("t_final", t_final)
        
        # First run one simulation with no interventions and store to text file
        #XXX Hackish! Fix me!!!
        actual_t_interventions = self.Constraints.t_interventions
        self.Constraints.t_interventions = t_final + 1
        costfunc_object = CostFunction(self.StochParams, self.OrigParams, \
                                       self.Constraints)
        n = len(self.Constraints.interventions.keys())
        self.deaths_before = costfunc_object(numpy.ones(n)*1./float(n), epidemic_file=epidemic_file_no_iv)
        self.Constraints.t_interventions = actual_t_interventions
        
        # If the intervention time is after t_final, do not run optimization
        if self.Constraints.t_interventions >= t_final:
            print "WARNING: Intervention time is greater than final time. \
No optimization will be performed."
            self.need_opt = False
            self.needed_resources = None

        # Filter valid interventions
        if 'valid_interventions' in kwds:
            self.Constraints.filter_interventions(kwds['valid_interventions'])

    def run_optimization(self, disp=False, epidemic_file_opt_iv="epidemic_opt_iv.csv"):
        """Call the Scipy optimization function. Returns both the optimal
        resource allocation and its cost."""
        
        if 'StochParams' not in dir(self):
            print "Please run initialize_stoch_solver() first. Aborting."
            return
        if 'OrigParams' not in dir(self):
            print "Please run initialize_model() first. Aborting."
            return
        
        self.costfunc_object = CostFunction(self.StochParams, self.OrigParams, \
                                       self.Constraints, disp=disp)
        n = len(self.Constraints.interventions.keys())
        
        x0 = numpy.ones(n)*1./float(n) # Start by distributing resources uniformly
        if self.need_opt:
            maxiter = 500 # XXX Arbitrary?
        else:
            if self.needed_resources is not None:
                x0 = self.needed_resources/self.Constraints.total
            maxiter = 1 # Just run it once

#        self.costfunc_object([1, 0, 0])
#        self.costfunc_object([0, 1, 0])
#        self.costfunc_object([0, 0, 1])
#        self.costfunc_object([0, 0, 0])
#        self.costfunc_object([1, 1, 1])

        constraints = [{'type':'ineq', 'fun': lambda x: 1.-numpy.sum(x)}]
        for i in range(n):
            constraints.append({'type':'ineq', 'fun': lambda x: x[i]})
        
        options = {'maxiter':maxiter, 'disp':False}

        result = scipy.optimize.minimize(self.costfunc_object, x0, method='COBYLA',\
                    constraints=constraints, options=options)
        self.xmin = result['x']

        self.final_cost = self.costfunc_object(self.xmin, epidemic_file=epidemic_file_opt_iv)

        # Always print the optimum
        print "Optimal resource allocation and cost:"
        self.print_output(self.xmin, self.final_cost)
        
        return self.xmin, self.final_cost
    
    def print_constraints(self):
        """Print out what the resource constraints are."""
        self.Constraints.represent()
    
    def print_output(self, resource_alloc, final_cost):
        """Pretty print an allocation and its associated cost."""
        self.costfunc_object.print_heading()
        self.costfunc_object.print_output(resource_alloc, final_cost)
    
    def print_log(self):
        """Print a log of the optimization allocations and costs."""
        self.costfunc_object.print_heading()
        for i, info in enumerate(self.costfunc_object.log_list):
            self.costfunc_object.print_output(info[0], info[1], linenum=str(i))

    def clear_log(self):
        """Clear the optimization log."""
        self.costfunc_object.log_list = []

    def plot_output(self):
        """Do plotting."""
        # Sandra's part goes here
        return



