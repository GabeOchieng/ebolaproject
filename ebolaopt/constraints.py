# Python2.7
import numpy
import csv
import copy

class Constraints:
    """Object to hold optimization parameters: total resources, 
        resource costs and effects, and time to start interventions."""

    def __init__(self, filename):
        # First insert default values
        self.total = 10000
        self.t_interventions = 200
        self.all_interventions = {'beta_H': (60., -0.01), \
                              'delta_2': (500., -0.05), \
                              'theta_1': (200., 0.01)}
                                  
        if filename:
            # Parse the input file
            with open(filename, 'rb') as csvfile:
                datareader = csv.reader(csvfile)
                # Iterate over rows
                for row in datareader:
                    if row[0].lower() == "total":
                        self.total = float(row[1])
                        if self.total <= 0:
                            raise Exception("total must be positive.")
                    elif row[0].lower() == "time":
                        self.t_interventions = float(row[1])
                        if self.t_interventions < 0:
                            raise Exception("time must be at least zero.")
                    elif row[0] in self.all_interventions.keys():
                        cost = float(row[1])
                        if cost < 0:
                            print "WARNING: cost is negative"
                        effect = float(row[2])
                        self.all_interventions[row[0]] = (cost, effect)
                    else:
                        print "WARNING: Ignoring unrecognized input %s in %s." % (row, filename)
    
        # By default, allow all interventions to be used
        self.interventions = copy.deepcopy(self.all_interventions)

    def filter_interventions(self, interventions):
        self.interventions = {}
        for intervention in interventions:
            self.interventions[intervention] = self.all_interventions[intervention]

def constraints_help():
    meanings = {"theta_1":("contact tracing", \
                           "fraction of infected cases diagnosed and hospitalized"), \
        "beta_H":("PPE", "contact rate for hospitalized cases"), \
        "delta_2":("drug","fatality rate of hospitalized patients")}
    s = "{0:<10}{1:<17}{2:<40}\n".format("Variable", "Intervention", "Effect")
    s += "-"*60 + "\n"
    for var in meanings.keys():
        s += "{0:<10}{1:<17}{2:<40}\n".format(var, meanings[var][0], meanings[var][1])
    print s

def setup_constraints(filename, valid_interventions):
    MyConstraints = Constraints(filename)
    
    if valid_interventions.lower() != 'all':
        MyConstraints.filter_interventions(valid_interventions)
    
    return MyConstraints


