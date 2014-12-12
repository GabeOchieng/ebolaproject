# Python2.7
import unittest
import numpy

from ebolaopt.optimizer import Optimizer

class TestOpt(unittest.TestCase):
    
    def test_scipy_optimize1(self):
        import scipy.optimize
        # Test below is taken from the scipy.optimize source code
        # objective function
        def fun(x, r=[4, 2, 4, 2, 1]):
            """ Objective function """
            return numpy.exp(x[0]) * (r[0] * x[0]**2 + r[1] * x[1]**2 +
                                r[2] * x[0] * x[1] + r[3] * x[1] +
                                r[4])
        # bounds
        bnds = numpy.array([[-numpy.inf]*2, [numpy.inf]*2]).T
        bnds[:, 0] = [0.1, 0.2]
        # constraints
        def feqcon(x, b=1):
            """ Equality constraint """
            return numpy.array([x[0]**2 + x[1] - b])
        def jeqcon(x, b=1):
            """ Jacobian of equality constraint """
            return numpy.array([[2*x[0], 1]])
        def fieqcon(x, c=10):
            """ Inequality constraint """
            return numpy.array([x[0] * x[1] + c])
        def jieqcon(x, c=10):
            """ Jacobian of Inequality constraint """
            return numpy.array([[1, 1]])
        # constraints dictionaries
        cons = ({'type': 'eq', 'fun': feqcon, 'jac': jeqcon, 'args': (1, )},
                {'type': 'ineq', 'fun': fieqcon, 'jac': jieqcon, 'args': (10,)})
        # Bounds constraint problem
        x, f = scipy.optimize.fmin_slsqp(fun, numpy.array([-1, 1]), bounds=bnds, disp=0,
                          full_output=True)[:2]
        numpy.testing.assert_almost_equal(numpy.array(x), numpy.array([0.1,  0.2]))
        # Equality and inequality constraints problem
        x, f = scipy.optimize.fmin_slsqp(fun, numpy.array([-1, 1]),
                          f_eqcons=feqcon, fprime_eqcons=jeqcon,
                          f_ieqcons=fieqcon, fprime_ieqcons=jieqcon,
                          disp=0, full_output=True)[:2]
        numpy.testing.assert_almost_equal(numpy.array(x), numpy.array([-0.75287901,  0.4331732]))


    def test_optimization(self):
        """Test the overall optimization."""
        data_file = "ebolaopt/data/ebola-case-counts-and-deaths-fro.csv"
        resources_file = "ebolaopt/data/resources.csv"
        myopt = Optimizer(data_file=data_file, resources_file=resources_file) # Create a new optimizer object
        myopt.initialize_model() # Do the deterministic fitting
        optimum = myopt.run_optimization(100) # Calculate!
        #XXX To do: Check that the answer makes sense?

if __name__ == '__main__':
    unittest.main()
