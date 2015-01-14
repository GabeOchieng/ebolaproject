# Python 2.7
import unittest

import ebolaopt.StochCalc.StochLib as StochLib

class TestStochCalc(unittest.TestCase):

    def test1(self):
        """Testing StochCalc solver without interventions."""
        t_interventions = 255
        k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                               t_interventions, OutputFileName, num_threads)
        print "Test 1: StochCalc runs successfully without interventions."

    def test2(self):
       """Testing StochCalc solver with interventions."""
       t_interventions = 150
       k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                              t_interventions, OutputFileName, num_threads)
       print "Test 2: StochCalc runs successfully with interventions."

    def test3(self):
        """Testing that interventions decrease the number of deaths."""
        t_interventions_1 = 255
        t_interventions_2 = 150
        k_1 = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                                 t_interventions_1, OutputFileName, num_threads)
        k_2 = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                                 t_interventions_2, OutputFileName, num_threads)
        self.assertLess(k_2, k_1)
        print "Test 3: Applying interventions decreases total deaths."

    def test4(self):
        """Testing StochCalc solver in parallel with 4 threads."""
        t_interventions = 255
        num_threads = 4
        k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                               t_interventions, OutputFileName, num_threads)
        print "Test 4: StochCalc runs successfully in parallel with 4 threads."

    def test5(self):
        """Testing that deaths increase as time of  interventions increases."""
        t_interventions = [10, 30, 50, 70, 90, 150, 200]
        k_list = []
        for t_int in t_interventions:
            k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                                   t_int, OutputFileName, num_threads)
            k_list.append(k)
        for i in range(0, len(k_list)-1):
            self.assertLess(k_list[i], k_list[i+1])
        print "Test 5: Deaths increase as time of first interventions increases."

    def test6(self):
        """Testing for speedup in parallel."""
        import time
        StochParams.set("Trajectories", 100)
        t_interventions = 255
        num_threads = [1, 2]
        t_list = []
        for n in num_threads:
            t0 = time.time()
            k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                                   t_interventions, OutputFileName, n)
            t1 = time.time()
            t_list.append(t1 - t0)
        for i in range(0, len(t_list)-1):
            self.assertGreater(t_list[i], t_list[i+1])
        print "Test 6: Code experiences speedup in parallel."

if __name__ == '__main__':
    StochParams = StochLib.pyStochParams()
    ModelParams = StochLib.pyModelParams()
    Interventions = StochLib.pyModelParams()
    OutputFileName = "NONE"
    num_threads = 1

    StochParams.set("N_samples", 50)
    StochParams.set("Trajectories", 30)
    StochParams.set("I_init", 3)
    StochParams.set("S_init", 199997)
    StochParams.set("H_init", 0)
    StochParams.set("F_init", 0)
    StochParams.set("R_init", 0)
    StochParams.set("E_init", 0)
    StochParams.set("t_final", 250.0)
    
    ModelParams.set("beta_I", 0.16)
    ModelParams.set("beta_H", 0.062)
    ModelParams.set("beta_F", 0.489)
    ModelParams.set("alpha", 1./12.)
    ModelParams.set("gamma_h", 1./3.24)
    ModelParams.set("gamma_f", 1./2.01)
    ModelParams.set("gamma_i", 1./15.)
    ModelParams.set("gamma_d", 1./13.31)
    ModelParams.set("theta_1", 0.197)
    ModelParams.set("delta_1", 0.5)
    ModelParams.set("delta_2", 0.5)
    
    Interventions.set("beta_I", 0.16)
    Interventions.set("beta_H", 0.)
    Interventions.set("beta_F", 0.489)
    Interventions.set("alpha", 1./12.)
    Interventions.set("gamma_h", 1./3.24)
    Interventions.set("gamma_f", 1./2.01)
    Interventions.set("gamma_i", 1./15.)
    Interventions.set("gamma_d", 1./13.31)
    Interventions.set("theta_1", 1.)
    Interventions.set("delta_1", 0.5)
    Interventions.set("delta_2", 0.)
    
    unittest.main()
