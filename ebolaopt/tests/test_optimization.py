# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt.optimizer import Optimizer

class TestOpt(unittest.TestCase):
    
    def test_optimization(self):
        """Test the overall optimization."""
        data_file = "ebolaopt/data/case_counts.csv"
        constraints_file = "ebolaopt/data/constraints.csv"
        myopt = Optimizer(data_file=data_file, constraints_file=constraints_file) # Create a new optimizer object
        myopt.initialize_model() # Do the deterministic fitting
        myopt.initialize_stoch_solver() # Initialize stochastic model
        optimum = myopt.run_optimization() # Calculate!
        myopt.represent_allocation(optimum) # Show final result
        # Check that sum of fractions is less than or equal to 1
        self.assertLessEqual(numpy.sum(optimum), 1)

    def test_extra_resources(self):
        """Test what happens when there are too many resources."""
        data_file = "ebolaopt/data/case_counts.csv"
        # Write a constraints file
        tempfilename = 'temp_ebolaopt.csv'
        with open(tempfilename, 'wb') as csvfile:
            w = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            w.writerow(['total', '1000000'])
            w.writerow(['time', '200'])
            w.writerow(['beta_H', '60', '-0.01'])
            w.writerow(['delta_2', '500', '-0.05'])
            w.writerow(['theta_1', '200', '0.01'])
        myopt = Optimizer(data_file=data_file, constraints_file=tempfilename) # Create a new optimizer object
        myopt.initialize_model() # Do the deterministic fitting
        myopt.initialize_stoch_solver() # Initialize stochastic model
        optimum = myopt.run_optimization() # Calculate!
        myopt.represent_allocation(optimum) # Show final result
        # Check that sum of fractions is less than or equal to 1
        self.assertLessEqual(numpy.sum(optimum), 1)

        # Cleanup: remove constraints file
        subprocess.call("rm %s" % tempfilename, shell=True)

if __name__ == '__main__':
    unittest.main()
