# Python2.7
import unittest
import numpy
import csv
import subprocess

from ebolaopt import optimize

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Test optimize user interface."""
        optimize(disp=True)

if __name__ == '__main__':
    unittest.main()
