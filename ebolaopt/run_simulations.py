# Python2.7
import numpy
import ebolaopt.StochCalc.StochLib as StochLib
from ebolaopt.cost_function import CostFunction
from ebolaopt.tools import print_heading, print_output, calc_interventions
import scipy.optimize

def check_total(MyConstraints, OrigParams):
    """Check that the total is not so large that optimization is pointless."""
    needed_resources = []
    for param in MyConstraints.interventions:
        cost, effects = MyConstraints.interventions[param]
        origval = OrigParams.get(param)
        #XXX This only considers beta_H, delta_2, and theta_1
        if param == 'beta_H' or param == 'delta_2':
            needed = -origval/effects*cost
        if param == 'theta_1':
            needed = (1.-origval)/effects*cost
        needed_resources.append(needed)
    needed_resources = numpy.array(needed_resources)
    
    # Compare total needed with total resources given as constraint
    total_needed = numpy.sum(needed_resources)
    need_opt = True
    if MyConstraints.total > total_needed:
        need_opt = False
    return need_opt, needed_resources

#XXX Move this into StochCalc?
def setup_stoch_params(N_samples, trajectories, t_final, N, I_init):
    StochParams = StochLib.pyStochParams()
    StochParams.set("N_samples", N_samples)
    StochParams.set("Trajectories", trajectories)
    StochParams.set("I_init", I_init)
    StochParams.set("S_init", N - I_init)
    StochParams.set("H_init", 0)
    StochParams.set("F_init", 0)
    StochParams.set("R_init", 0)
    StochParams.set("E_init", 0)
    StochParams.set("t_final", t_final)
    return StochParams

def run_no_interventions(OrigParams, StochParams, out_file):
    t_interventions = StochParams.get('t_final') + 1
    cost = StochLib.StochCalc(StochParams, OrigParams, OrigParams,
                              t_interventions, out_file, 1)
    return cost

def run_with_interventions(alloc, OrigParams, StochParams, MyConstraints, out_file):
    ModifiedParams = calc_interventions(alloc, OrigParams, MyConstraints)
    cost = StochLib.StochCalc(StochParams, OrigParams, ModifiedParams,
                              MyConstraints.t_interventions, out_file, 1)
    print_heading(MyConstraints)
    print_output(alloc, cost)
    return cost

def run_optimization(OrigParams, StochParams, MyConstraints, disp, out_file):
    # Check to make sure intervention time is less than final time
    if MyConstraints.t_interventions >= StochParams.get('t_final'):
        print "WARNING: Intervention time is greater than final time. \
No optimization will be performed."
        cost = run_no_interventions(OrigParams, StochParams, out_file=out_file)
        return None, cost
    
    # Check to make sure there aren't too many resources
    need_opt, needed_resources = check_total(MyConstraints, OrigParams)
    
    # Run optimization if necessary. Otherwise, just run it once
    if need_opt:
        costfunc_object = CostFunction(OrigParams, StochParams, MyConstraints, disp=disp)
        
        n = len(MyConstraints.interventions.keys())
        x0 = numpy.ones(n)*1./float(n) # Start by distributing resources uniformly
        
        constraints = [{'type':'ineq', 'fun': lambda x: 1.-numpy.sum(x)}]
        for i in range(n):
            constraints.append({'type':'ineq', 'fun': lambda x: x[i]})
        options = {'disp':False}
        
        result = scipy.optimize.minimize(costfunc_object, x0, method='COBYLA',\
                                         constraints=constraints, options=options)
        xmin = result['x']

        # One last evaluation of the optimum
        final_cost = costfunc_object(xmin, out_file=out_file)
         
        # Always print the optimum
        print "Optimal resource allocation and cost:"
        print_output(xmin, final_cost)
    else:
        print """WARNING: There are enough resources to maximize all interventions.
No optimization will be performed."""
        final_cost = run_with_interventions(needed_resources, OrigParams, StochParams, MyConstraints, out_file=out_file)
        xmin = needed_resources

    return xmin, final_cost


