# Python2.7
import numpy
import ebolaopt.StochCalc as StochCalc
import StochCalc.StochLib as StochLib

def print_heading(MyConstraints):
    print "\t" + "\t".join(MyConstraints.interventions.keys()) + "\t" + "deaths"

def print_output(alloc, cost, linenum=""):
    percentages = 100.*numpy.array(alloc)
    linenum = str(linenum)
    print linenum + "\t" + "\t".join(["%.2f%%" % x for x in percentages]) + "\t%.2f" % cost

def calc_interventions(alloc, OrigParams, MyConstraints):
    fraction_params = ["theta_1", "delta_1", "delta_2"]
    
    # Unfortunately copy.deepcopy doesn't work with cython, so manually
    # copy OrigParams to ModifiedParams.
    ModifiedParams = StochLib.pyModelParams()
    for varname in StochCalc.ModelParamList:
        val = OrigParams.get(varname)
        ModifiedParams.set(varname, val)

    total = MyConstraints.total
    for i, param in enumerate(MyConstraints.interventions):
        cost, effect = MyConstraints.interventions[param]
        difference = effect*alloc[i]*total/cost
        newval = OrigParams.get(param) + difference
        # Fractions must stay between 0 and 1, and times must not be negative
        if newval < 0:
            newval = 0
        if param in fraction_params:
            if newval > 1:
                newval = 1.
        ModifiedParams.set(param, newval)

    return ModifiedParams

