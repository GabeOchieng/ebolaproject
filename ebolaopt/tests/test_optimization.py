# Python2.7
import unittest

class TestOpt(unittest.TestCase):
    
    def test1(self):
        from ebolaopt import optimize
        optimize()

    def test2(self):
        from ebolaopt import run_simulation
        run_simulation([1, 0, 0])

    def test3(self):
        from ebolaopt import setup_model, optimize_with_setup, run_simulation_with_setup
        params = setup_model()
        run_simulation_with_setup([1, 0, 0], params, figure_file="try1.png")
        optimize_with_setup(params, figure_file="opt.png")

if __name__ == '__main__':
    unittest.main()
