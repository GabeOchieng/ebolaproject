# Python2.7
import numpy
import StochCalc.StochLib as StochLib

class CostFunction:
    """This is what we want to minimize. Callable object."""
    
    def __init__(self, StochParams, OrigParams, Constraints):
        # Objects for passing into stochastic calculator
        self.StochParams = StochParams
        self.OrigParams = OrigParams
        self.Constraints = Constraints
        
        # Unfortunately copy.deepcopy doesn't work with cython, so manually
        # copy OrigParams to ModifiedParams.
        self.ModifiedParams = StochLib.pyModelParams()
        for method in dir(self.OrigParams):
            if method[:3] == 'get':
                methodname = method[3:]
                val = eval("self.OrigParams.get%s()" % methodname)
                eval("self.ModifiedParams.set%s(%f)" % (methodname, val))
    
    def __call__(self, resource_alloc):
        """Convert resource allocation to model parameters and run simulation.
            Input is array representing resource allocation, 
            output is a scalar number representing cost (e.g. cases/deaths)."""
        self.calc_interventions(resource_alloc)
        cost = StochLib.StochCalc(self.StochParams, self.OrigParams, self.ModifiedParams,
                               self.Constraints.t_interventions, "NONE")
        return cost

    def calc_interventions(self, resource_alloc):
        """Calculate the ModifiedParams that correspond to resource_alloc. """
        total = self.Constraints.total
        for i, param in enumerate(self.Constraints.interventions):
            cost, effect = self.Constraints.interventions[param]
            difference = effect*resource_alloc[i]*total/cost
            method_name = param[0].upper() + param[1:]
            newval = eval("self.OrigParams.get%s()" % method_name) + difference
            # Fractions must stay between 0 and 1, and times must not be negative
            #XXX So far only consider fractions
            if newval < 0:
                newval = 0
            if newval > 1:
                newval = 1.
            eval("self.ModifiedParams.set%s(%f)" % (method_name, newval))


