# distutils: Language = c++
# distutils: sources = Rectangle.cpp

from libcpp.string cimport string

cdef extern from "ModelParams.h":
    cdef cppclass ModelParams:
        ModelParams()
        double beta_I, beta_H, beta_F, alpha, gamma_h, theta_1
        double delta_1, delta_2, gamma_f, gamma_i, gamma_d

cdef extern from "StochParams.h":
    cdef cppclass StochParams:
        StochParams()
        int N_samples, Trajectories
        int I_init, S_init, H_init, F_init, R_init, E_init
        double t_final

cdef class pyModelParams:
    cdef ModelParams* thisptr # hold a C++ instance

    def __cinit__(self):
        self.thisptr = new ModelParams()

    def __dealloc__(self):
        del self.thisptr

    def set(self, var, val):
        if var == "beta_I":
            self.thisptr.beta_I = val
        elif var == "beta_H":
            self.thisptr.beta_H = val
        elif var == "beta_F":
            self.thisptr.beta_F = val
        elif var == "alpha":
            self.thisptr.alpha = val
        elif var == "gamma_h":
            self.thisptr.gamma_h = val
        elif var == "gamma_f":
            self.thisptr.gamma_f = val
        elif var == "gamma_i":
            self.thisptr.gamma_i = val
        elif var == "gamma_d":
            self.thisptr.gamma_d = val
        elif var == "theta_1":
            self.thisptr.theta_1 = val
        elif var == "delta_1":
            self.thisptr.delta_1 = val
        elif var == "delta_2":
            self.thisptr.delta_2 = val

    def get(self, var):
        if var == "beta_I":
            return self.thisptr.beta_I
        elif var == "beta_H":
            return self.thisptr.beta_H
        elif var == "beta_F":
            return self.thisptr.beta_F
        elif var == "alpha":
            return self.thisptr.alpha
        elif var == "gamma_h":
            return self.thisptr.gamma_h
        elif var == "gamma_f":
            return self.thisptr.gamma_f
        elif var == "gamma_i":
            return self.thisptr.gamma_i
        elif var == "gamma_d":
            return self.thisptr.gamma_d
        elif var == "theta_1":
            return self.thisptr.theta_1
        elif var == "delta_1":
            return self.thisptr.delta_1
        elif var == "delta_2":
            return self.thisptr.delta_2
            
    def __repr__(self):
        output = "beta_I = %.2f" % self.thisptr.beta_I
        output += "\nbeta_H = %.2f" % self.thisptr.beta_H
        output += "\nbeta_F = %.2f" % self.thisptr.beta_F
        output += "\nalpha = %.2f" % self.thisptr.alpha
        output += "\ngamma_h = %.2f" % self.thisptr.gamma_h
        output += "\ngamma_f = %.2f" % self.thisptr.gamma_f
        output += "\ngamma_i = %.2f" % self.thisptr.gamma_i
        output += "\ngamma_d = %.2f" % self.thisptr.gamma_d
        output += "\ntheta_1 = %.2f" % self.thisptr.theta_1
        output += "\ndelta_1 = %.2f" % self.thisptr.delta_1
        output += "\ndelta_2 = %.2f" % self.thisptr.delta_2
        return output

cdef class pyStochParams:
    cdef StochParams* thisptr # hold a c++ instance

    def __cinit__(self):
        self.thisptr = new StochParams()

    def __dealloc__(self):
        del self.thisptr

    def set(self, var, val):
        if var == "N_samples":
            self.thisptr.N_samples = val
        elif var == "Trajectories":
            self.thisptr.Trajectories = val
        elif var == "I_init":
            self.thisptr.I_init = val
        elif var == "S_init":
            self.thisptr.S_init = val
        elif var == "H_init":
            self.thisptr.H_init = val
        elif var == "F_init":
            self.thisptr.F_init = val
        elif var == "R_init":
            self.thisptr.R_init = val
        elif var == "E_init":
            self.thisptr.E_init = val
        elif var == "t_final":
            self.thisptr.t_final = val

    def get(self, var):
        if var == "N_samples":
            return self.thisptr.N_samples
        elif var == "Trajectories":
            return self.thisptr.Trajectories
        elif var == "I_init":
            return self.thisptr.I_init
        elif var == "S_init":
            return self.thisptr.S_init
        elif var == "H_init":
            return self.thisptr.H_init
        elif var == "F_init":
            return self.thisptr.F_init
        elif var == "R_init":
            return self.thisptr.R_init
        elif var == "E_init":
            return self.thisptr.E_init
        elif var == "t_final":
            return self.thisptr.t_final

cdef extern from "StochCalc.h":
    float c_StochCalc "StochCalc" (StochParams *myStochParams,
                                   ModelParams *myModel, ModelParams *interventions,
                                   float t_interventions, string OutputFileName)

def StochCalc(pyStochParams myStochParams, pyModelParams myModel,
              pyModelParams interventions, float t_interventions,
              string OutputFileName):
    return c_StochCalc(myStochParams.thisptr, myModel.thisptr,
                       interventions.thisptr, t_interventions, OutputFileName)