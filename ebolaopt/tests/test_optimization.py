# Python2.7
import unittest

class TestOpt(unittest.TestCase):
    
    def test1(self):
        """Testing warning if  the prevention time is after the final time."""
        from ebolaopt import optimize
        optimize(plot=False, plot_fit=False, t_final= 30)

    def test2(self):
        """Testing warning if too much resource is present."""
        from ebolaopt import optimize
        optimize(plot=False, plot_fit=False, constraints_file="ebolaopt/data/constraints_test.csv")
    
    def test3(self):
        """Testing different countries"""
        from ebolaopt import optimize
        optimize(plot=False, plot_fit=False, country = "Sierra Leone",trajectories=10)
        optimize(plot=False, plot_fit=False, country = "Liberia", trajectories=10)

    def test4(self):
        """Boundary test for resource allocation"""
        from ebolaopt import run_simulation
        run_simulation([1, 0, 0], plot=False, plot_fit=False)
        run_simulation([0, 1, 0], plot=False, plot_fit=False)
        run_simulation([0, 0, 1], plot=False, plot_fit=False)

    
    def test5(self):
        """Testing Parallelization"""
        from ebolaopt import optimize
        optimize(plot=False, plot_fit=False, country = "Sierra Leone",trajectories=10, n_threads = 4)      

    def test6(self):
        from ebolaopt import setup_model, optimize_with_setup, run_simulation_with_setup
        params = setup_model(plot_fit=True)
        run_simulation_with_setup([1, 0, 0], params, figure_file="try1.png", plot=True)
        optimize_with_setup(params, figure_file="opt.png", plot=True)

if __name__ == '__main__':
    unittest.main()
