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

    def setBeta_I(self, val):
        self.thisptr.beta_I = val

    def setBeta_H(self, val):
        self.thisptr.beta_H = val
    
    def setBeta_F(self, val):
        self.thisptr.beta_F = val

    def setAlpha(self, val):
        self.thisptr.alpha = val

    def setGamma_h(self, val):
        self.thisptr.gamma_h = val

    def setGamma_f(self, val):
        self.thisptr.gamma_f = val

    def setGamma_i(self, val):
        self.thisptr.gamma_i = val

    def setGamma_d(self, val):
        self.thisptr.gamma_d = val

    def setTheta_1(self, val):
        self.thisptr.theta_1 = val

    def setDelta_1(self, val):
        self.thisptr.delta_1 = val

    def setDelta_2(self, val):
        self.thisptr.delta_2 = val

cdef class pyStochParams:
    cdef StochParams* thisptr # hold a c++ instance

    def __cinit__(self):
        self.thisptr = new StochParams()

    def __dealloc__(self):
        del self.thisptr

    def setN_samples(self, val):
        self.thisptr.N_samples = val

    def setTrajectories(self, val):
        self.thisptr.Trajectories = val

    def setI_init(self, val):
        self.thisptr.I_init = val

    def setS_init(self, val):
        self.thisptr.S_init = val

    def setH_init(self, val):
        self.thisptr.H_init = val

    def setF_init(self, val):
        self.thisptr.F_init = val

    def setR_init(self, val):
        self.thisptr.R_init = val

    def setE_init(self, val):
        self.thisptr.E_init = val

    def setT_final(self, val):
        self.thisptr.t_final = val

cdef extern from "StochCalc.h":
    float c_StochCalc "StochCalc" (StochParams *myStochParams,
                                   ModelParams *myModel, ModelParams *interventions,
                                   float t_interventions, string OutputFileName)

def StochCalc(pyStochParams myStochParams, pyModelParams myModel,
              pyModelParams interventions, float t_interventions,
              string OutputFileName):
    return c_StochCalc(myStochParams.thisptr, myModel.thisptr,
                       interventions.thisptr, t_interventions, OutputFileName)