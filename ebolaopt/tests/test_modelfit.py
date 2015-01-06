# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt import fit_data

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test Different Countries"""
        fit_data("ebolaopt/data/case_counts.csv", "Liberia", 1e7, plot_fit = False)
        fit_data("ebolaopt/data/case_counts.csv", "Sierra Leone", 1e7, plot_fit = False)
    def test2(self):
        """Test Plots."""
        fit_data("ebolaopt/data/case_counts.csv", "Sierra Leone", 1e7, plot_fit = True)
if __name__ == '__main__':
    unittest.main()
