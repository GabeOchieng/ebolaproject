# Python2.7
import numpy

##############
#XXX Placeholder function for now for stochastic calculation
# Later, import Jesse's code through cython
def stoch_calc(orig_params, modified_params, final_time):
    cases = modified_params[0] + modified_params[1] - modified_params[2]
    return cases
#############

class CostFunction:
    """This is what we want to minimize. Callable object."""
    
    def __init__(self, final_time, orig_params, resources_dict):
        self.final_time = final_time
        self.orig_params = orig_params
        self.costs = numpy.array([x[0] for x in resources_dict["interventions"].values()])
        self.effects = numpy.array([x[1] for x in resources_dict["interventions"].values()])
        self.total = resources_dict["total"]
        return
    
    def __call__(self, resource_alloc):
        """Run stochastic simulation and apply metric to results.
            Input is array, output is a scalar number. 
            Note: resource_alloc has dimension n_resource_types - 1 due to
            constraint that the sum of all the fractions must equal 1."""
        modified_params = self.calc_interventions(resource_alloc)
        output_data = stoch_calc(self.orig_params, modified_params, self.final_time)
        cost = self._metric(output_data)
        return cost
    
    def _metric(self, output_data):
        """Perhaps do some additional calculation on stoch_calc output."""
        return output_data # For now, just give back what was put in

    def calc_interventions(self, resource_alloc):
        """Given orig_params = initial parameters (fixed),
            x = fraction of budget per intervention, B = total budget (fixed),
            costs = cost of each intervention (fixed)."""
        units_iv = resource_alloc*self.total/self.costs
        modified_params = self.orig_params + self.effects*units_iv
        return modified_params


