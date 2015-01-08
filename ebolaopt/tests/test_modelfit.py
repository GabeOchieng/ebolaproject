# Python2.7
import unittest

from ebolaopt.modelfit import fit_params

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test Different Countries"""
        params = fit_params("ebolaopt/data/case_counts.csv", "Liberia", 1e7, plot_fit = False)
        print repr(params)
        params = fit_params("ebolaopt/data/case_counts.csv", "Sierra Leone", 1e7, plot_fit = False)
        print repr(params)
    
    def test2(self):
        """Test Plots."""
        params = fit_params("ebolaopt/data/case_counts.csv", "Sierra Leone", 1e7, plot_fit = True)
        print repr(params)

if __name__ == '__main__':
    unittest.main()
