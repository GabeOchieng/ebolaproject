# Python2.7
import numpy
import ebolaopt.StochCalc.StochLib as StochLib
from ebolaopt.tools import print_heading, print_output, calc_interventions

class CostFunction:
    """This is what we want to minimize. Callable object."""
    
    def __init__(self, OrigParams, StochParams, MyConstraints, disp=False):
        self.StochParams = StochParams
        self.OrigParams = OrigParams
        self.MyConstraints = MyConstraints
        self.disp = disp
        self.log_list = []
        self.log_n = 0
        
        if disp:
            print "Performing optimization:"
            print_heading(self.MyConstraints)
    
    def __call__(self, alloc, out_file="NONE"):
        ModifiedParams = calc_interventions(alloc, self.OrigParams, self.MyConstraints)
        
        cost = StochLib.StochCalc(self.StochParams, self.OrigParams, ModifiedParams,
                               self.MyConstraints.t_interventions, out_file, 1)
                               
        if self.disp:
            print_output(alloc, cost, str(self.log_n))
        
        self.log_list.append((alloc, cost))
        self.log_n += 1
        return cost

    def clear_log(self):
        self.log_list = []
        self.log_n = 0


