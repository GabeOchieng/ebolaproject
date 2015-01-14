# Python2.7
import unittest
import os

from ebolaopt.modelfit import fit_params

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test Different Countries"""
        from ebolaopt import get_data_path
        
        params = fit_params(get_data_path("case_counts.csv"), "Liberia", 1e7, plot_fit = False)
        print repr(params)
        params = fit_params(get_data_path("case_counts.csv"), "Sierra Leone", 1e7, plot_fit = False)
        print repr(params)
    
    def test2(self):
        """Test Plots."""
        from ebolaopt import get_data_path
        
        params = fit_params(get_data_path("case_counts.csv"), "Sierra Leone", 1e7, plot_fit = True)
        print repr(params)

if __name__ == '__main__':
    unittest.main()
