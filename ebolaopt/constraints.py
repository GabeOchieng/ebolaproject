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
            # TODO: check inputs
            with open(filename, 'rb') as csvfile:
                datareader = csv.reader(csvfile)
                # Iterate over rows
                for row in datareader:
                    if row[0].lower() == "total":
                        self.total = float(row[1])
                    elif row[0].lower() == "time":
                        self.t_interventions = float(row[1])
                    else:
                        self.interventions[row[0]] = (float(row[1]), float(row[2]))
    
        return

    def check_total(self, OrigParams):
        """Check that the total is not so large that optimization is pointless."""
        # Calculate the total necessary to max out each intervention parameter
        total_needed = 0.
        for param in self.interventions:
            #XXX There's probably a more efficient way to do this
            cost, effects = self.interventions[param]
            method_name = param[0].upper() + param[1:]
            origval = eval("OrigParams.get%s()" % method_name)
            if param == 'beta_H' or param == 'delta_2':
                total_needed += -origval/effects*cost
            if param == 'theta_1':
                total_needed += (1.-origval)/effects*cost
        if self.total > total_needed:
            print "Warning! There are extra resources. The resources \
                    needed for each intervention are: and their effects are:"
            #XXX Finish this! set maxfun=1 in optimization?
        return


