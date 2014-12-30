# Python2.7
import numpy
import csv

class Constraints:
    """Object to hold optimization parameters: total resources, 
        resource costs and effects, and time to start interventions."""

    def __init__(self, filename):
        # First insert default values
        self.total = 5000
        self.t_interventions = 100
        self.interventions = {'beta_H': (100.0, -0.0001), \
                              'delta_2': (500.0, -1e-05), \
                              'theta_1': (2.0, 0.0001)}
                                  
        if filename:
            # Parse the input file
            with open(filename, 'rb') as csvfile:
                datareader = csv.reader(csvfile)
                # Iterate over rows
                for row in datareader:
                    if row[0].lower() == "total":
                        self.total = float(row[1])
                    elif row[0].lower() == "time":
                        self.t_interventions = float(row[1])
                    elif row[0] in self.interventions.keys():
                        self.interventions[row[0]] = (float(row[1]), float(row[2]))
                    else:
                        print "WARNING: Ignoring unrecognized input in %s." % filename
    
        return

    def check_total(self, OrigParams):
        """Check that the total is not so large that optimization is pointless."""
        needed_resources = []
        for param in self.interventions:
            cost, effects = self.interventions[param]
            method_name = param[0].upper() + param[1:]
            origval = eval("OrigParams.get%s()" % method_name)
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


