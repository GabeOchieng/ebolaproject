# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt import optimize

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test optimize user interface."""
        optimize(data_file="data/case_counts.csv", \
                  constraints_file="data/constraints.csv", \
                  country="Liberia", disp=True, plot=True)

    def test2(self):
        """Test specifying only a subset of interventions."""
        optimize(data_file="data/case_counts.csv", \
                 constraints_file="data/constraints.csv", \
                 country="Liberia", disp=True, valid_interventions=['theta_1', 'beta_H'])

if __name__ == '__main__':
    unittest.main()
