# Python2.7
import unittest
import numpy

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Testing warning if the prevention time is after the final time."""
        from ebolaopt import optimize
        print "A warning should print and no optimization should be run:"
        alloc, cost = optimize(plot=False, plot_fit=False, t_final=30)
        self.assertLessEqual(numpy.sum(alloc), 1.)
    
    def test2(self):
        """Testing warning if too much resource is present."""
        from ebolaopt import optimize
        from ebolaopt import get_data_path
        print "A warning should print and no optimization should be run:"
        alloc, cost = optimize(plot=False, plot_fit=False, constraints_file=get_data_path("constraints_test.csv"))
        self.assertLessEqual(numpy.sum(alloc), 1.)
    
    def test3(self):
        """Testing different countries"""
        from ebolaopt import optimize
        alloc, cost = optimize(plot=False, plot_fit=False, country = "Sierra Leone",trajectories=10)
        self.assertLessEqual(numpy.sum(alloc), 1.)
        alloc, cost = optimize(plot=False, plot_fit=False, country = "Liberia", trajectories=10)
        self.assertLessEqual(numpy.sum(alloc), 1.)

    def test4(self):
        """Boundary test for resource allocation"""
        from ebolaopt import run_simulation
        cost = run_simulation([1, 0, 0], plot=False, plot_fit=False)
        self.assertGreaterEqual(cost, 0.)
        cost = run_simulation([0, 1, 0], plot=False, plot_fit=False)
        self.assertGreaterEqual(cost, 0.)
        cost = run_simulation([0, 0, 1], plot=False, plot_fit=False)
        self.assertGreaterEqual(cost, 0.)

    def test5(self):
        """Testing Parallelization"""
        from ebolaopt import optimize
        alloc, cost = optimize(plot=False, plot_fit=False, country = "Sierra Leone",trajectories=10, n_threads = 4)
        self.assertLessEqual(numpy.sum(alloc), 1)

    def test6(self):
        """Testing that setup works and optimization helps. """
        from ebolaopt import setup_model, optimize_with_setup, run_simulation_with_setup
        params = setup_model(plot_fit=True)
        cost_before = run_simulation_with_setup([1, 0, 0], params, figure_file="try1.png", plot=True)
        alloc, cost_opt = optimize_with_setup(params, figure_file="opt.png", plot=True)
        self.assertGreaterEqual(cost_before, cost_opt)

    def test7(self):
        """Testing specification of valid interventions. """
        from ebolaopt import optimize
        alloc, cost = optimize(plot=False, plot_fit=False, \
                               valid_interventions=["beta_H", "theta_1"])
        self.assertEqual(len(alloc), 2)

if __name__ == '__main__':
    unittest.main()
