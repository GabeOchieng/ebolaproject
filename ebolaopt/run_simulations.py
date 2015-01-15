# Python2.7
import numpy
import ebolaopt.StochCalc.StochLib as StochLib
from ebolaopt.cost_function import CostFunction
from ebolaopt.tools import print_heading, print_output, calc_interventions
from scipy.optimize import minimize

def calc_needed_resources(MyConstraints, OrigParams):
    """Calculate maximum needed resources to max out the interventions."""
    needed_resources = []
    for param in MyConstraints.interventions:
        cost, effects = MyConstraints.interventions[param]
        origval = OrigParams.get(param)
        # NOTE: This only considers beta_H, delta_2, and theta_1
        if param == 'beta_H' or param == 'delta_2':
            needed = -origval/effects*cost
        if param == 'theta_1':
            needed = (1.-origval)/effects*cost
        needed_resources.append(needed)
    needed_resources = numpy.array(needed_resources)
    return needed_resources

#XXX Move this into StochCalc?
def setup_stoch_params(N_samples, trajectories, t_final, N, I_init, \
                       H_init, F_init, R_init, E_init):
    """Generate a StochParams object instance."""
    StochParams = StochLib.pyStochParams()
    StochParams.set("N_samples", N_samples)
    StochParams.set("Trajectories", trajectories)
    StochParams.set("I_init", I_init)
    StochParams.set("S_init", N - I_init)
    StochParams.set("H_init", H_init)
    StochParams.set("F_init", F_init)
    StochParams.set("R_init", R_init)
    StochParams.set("E_init", E_init)
    StochParams.set("t_final", t_final)
    return StochParams

def run_no_interventions(OrigParams, StochParams, out_file, n_threads=1):
    """Run the simulations once with no interventions."""
    t_interventions = StochParams.get('t_final') + 1
    cost = StochLib.StochCalc(StochParams, OrigParams, OrigParams,
                              t_interventions, out_file, n_threads)
    return cost

def run_with_interventions(alloc, OrigParams, StochParams, MyConstraints, \
                           out_file, n_threads=1):
    """Run the simulations once with the specified interventions."""
    ModifiedParams = calc_interventions(alloc, OrigParams, MyConstraints)
    cost = StochLib.StochCalc(StochParams, OrigParams, ModifiedParams,
                              MyConstraints.t_interventions, out_file, n_threads)
    print_heading(MyConstraints)
    print_output(alloc, cost)
    return cost

def run_optimization(OrigParams, StochParams, MyConstraints, disp, out_file, \
                     n_threads=1):
    """Run the resource allocation optimization."""
    # Check to make sure intervention time is less than final time
    if MyConstraints.t_interventions >= StochParams.get('t_final'):
        print "WARNING: Intervention time is greater than final time. \
No optimization will be performed."
        cost = run_no_interventions(OrigParams, StochParams, out_file=out_file)
        return None, cost
    
    # Check to make sure there aren't too many resources
    needed_resources = calc_needed_resources(MyConstraints, OrigParams)
    if MyConstraints.total >= numpy.sum(needed_resources):
        print """WARNING: There are enough resources to maximize all interventions.
No optimization will be performed."""
        alloc = needed_resources/MyConstraints.total
        final_cost = run_with_interventions(alloc, OrigParams, StochParams, MyConstraints, out_file=out_file)
        return alloc, final_cost
    
    # Run optimization if necessary
    costfunc_object = CostFunction(OrigParams, StochParams, MyConstraints, \
                                   disp=disp, n_threads=n_threads)
    
    n = len(MyConstraints.interventions.keys())
    x0 = numpy.ones(n)*1./float(n) # Start by distributing resources uniformly
    
    constraints = [{'type':'ineq', 'fun': lambda x: 1.-numpy.sum(x)}]
    for i in range(n):
        constraints.append({'type':'ineq', 'fun': lambda x: x[i]})
    options = {'disp':False}
    
    result = minimize(costfunc_object, x0, method='COBYLA',\
                      constraints=constraints, options=options)
    xmin = result['x']

    # One last evaluation of the optimum
    final_cost = costfunc_object(xmin, out_file=out_file)
     
    # Always print the optimum
    print "Optimal resource allocation and cost:"
    print_heading(MyConstraints)
    print_output(xmin, final_cost)
    return xmin, final_cost


