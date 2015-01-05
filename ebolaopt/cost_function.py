# Python2.7
import numpy
import StochCalc
import ebolaopt.StochCalc.StochLib as StochLib

class CostFunction:
    """This is what we want to minimize. Callable object."""
    
    def __init__(self, StochParams, OrigParams, Constraints, disp=False):
        # Objects for passing into stochastic calculator
        self.StochParams = StochParams
        self.OrigParams = OrigParams
        self.Constraints = Constraints
        self.disp = disp
        self.log_list = []
        self.log_n = 0
        
        if disp:
            print "Performing optimization:"
            self.print_heading()
        
        # Unfortunately copy.deepcopy doesn't work with cython, so manually
        # copy OrigParams to ModifiedParams.
        self.ModifiedParams = StochLib.pyModelParams()
        for varname in StochCalc.ModelParamList:
            val = self.OrigParams.get(varname)
            self.ModifiedParams.set(varname, val)
    
    def __call__(self, resource_alloc):
        """Convert resource allocation to model parameters and run simulation.
            Input is array representing resource allocation, 
            output is a scalar number representing cost (e.g. deaths)."""
        self.calc_interventions(resource_alloc)
        cost = StochLib.StochCalc(self.StochParams, self.OrigParams, self.ModifiedParams,
                               self.Constraints.t_interventions, "NONE")
        if self.disp:
            self.print_output(resource_alloc, cost, str(self.log_n))
        
        self.log_list.append((resource_alloc, cost))
        self.log_n += 1
        return cost

    def calc_interventions(self, resource_alloc):
        """Calculate the ModifiedParams that correspond to resource_alloc. """
        fraction_params = ["beta_I", "beta_H", "beta_F", "theta_1", "delta_1", \
                           "delta_2"]
        
        total = self.Constraints.total
        for i, param in enumerate(self.Constraints.interventions):
            cost, effect = self.Constraints.interventions[param]
            difference = effect*resource_alloc[i]*total/cost
            newval = self.OrigParams.get(param) + difference
            # Fractions must stay between 0 and 1, and times must not be negative
            if newval < 0:
                newval = 0
            if param in fraction_params:
                if newval > 1:
                    newval = 1.
            self.ModifiedParams.set(param, newval)

    def print_heading(self):
        print "\t" + "\t".join(self.Constraints.interventions.keys()) + "\t" + "deaths"

    def print_output(self, resource_alloc, cost, linenum=""):
        percentages = 100.*numpy.array(resource_alloc)
        print linenum + "\t" + "\t".join(["%.2f%%" % x for x in percentages]) + "\t%.2f" % cost



