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
    
        return

    def check_total(self, OrigParams):
        """Check that the total is not so large that optimization is pointless."""
        needed_resources = []
        for param in self.interventions:
            cost, effects = self.interventions[param]
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
        if self.total > total_needed:
            print """WARNING: There are enough resources to maximize all interventions.
No optimization will be performed."""
            need_opt = False
        return need_opt, needed_resources

    def represent(self):
        """Pretty print what the resource constraints actually mean."""
        print "Resource constraints: \n"
        meanings = {"theta_1":("contact tracing", \
                    "fraction of infected cases diagnosed and hospitalized"), \
                    "beta_H":("PPE", "contact rate for hospitalized cases"), \
                    "delta_2":("drug","survival rate of hospitalized patients")}
        for param in self.interventions:
            interpretation, definition = meanings[param]
            cost, effect = self.interventions[param]
            print interpretation + " costs %.2f" % cost + \
                  " and affects " + definition + " by %.2f" % effect + "\n"

    def filter_interventions(self, interventions):
        """Only allow some interventions to be used."""
        self.interventions = {}
        for intervention in interventions:
            self.interventions[intervention] = self.all_interventions[intervention]
        return


