# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt import fit_data

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test optimize user interface."""
        fit_data("ebolaopt/data/case_counts.csv", "Liberia", 10000)

if __name__ == '__main__':
    unittest.main()
