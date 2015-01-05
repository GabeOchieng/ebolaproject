# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt.optimizer import Optimizer

class TestOpt(unittest.TestCase):
    
    def xtest_times(self):
        """Test that as t_intervention increases, cost increases."""
        tempfilename = 'temp_ebolaopt.csv'
        def write_constraints(time):
            # Write a constraints file
            with open(tempfilename, 'wb') as csvfile:
                w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
                w.writerow(['total', '10000'])
                w.writerow(['time', str(int(time))])
                w.writerow(['beta_H', '60', '-0.01'])
                w.writerow(['delta_2', '500', '-0.05'])
                w.writerow(['theta_1', '200', '0.01'])
        
        times = [50, 100, 150, 200, 250]
        last_cost = 0
        for time in times:
            print "Intervention time = " + str(time)
            write_constraints(time)
            myopt = Optimizer(constraints_file=tempfilename) # Create a new optimizer object
            myopt.initialize_model() # Do the deterministic fitting
            myopt.initialize_stoch_solver() # Initialize stochastic model
            optimum, cost = myopt.run_optimization(disp=True) # Calculate!
            self.assertLessEqual(last_cost, cost)
            last_cost = cost
        
        # Cleanup: remove constraints file
        subprocess.call("rm %s" % tempfilename, shell=True)
    
    def test_costs(self):
        """Test that as cost of an intervention increases, cost increases."""
        tempfilename = 'temp_ebolaopt.csv'
        def write_constraints(cost):
            # Write a constraints file
            with open(tempfilename, 'wb') as csvfile:
                w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
                w.writerow(['total', '10000'])
                w.writerow(['time', '150'])
                w.writerow(['beta_H', str(cost), '-0.01'])
                w.writerow(['delta_2', '500', '-0.05'])
                w.writerow(['theta_1', '200', '0.01'])
        
        betaHcosts = [0.01, 10, 100, 1000]
        last_cost = 0
        for betaHcost in betaHcosts:
            print "beta_H cost = " + str(betaHcost)
            write_constraints(betaHcost)
            myopt = Optimizer(constraints_file=tempfilename) # Create a new optimizer object
            myopt.initialize_model() # Do the deterministic fitting
            myopt.initialize_stoch_solver() # Initialize stochastic model
            optimum, cost = myopt.run_optimization(disp=True) # Calculate!
            #self.assertLessEqual(last_cost, cost)
            last_cost = cost
        
        # Cleanup: remove constraints file
        subprocess.call("rm %s" % tempfilename, shell=True)

if __name__ == '__main__':
    unittest.main()
