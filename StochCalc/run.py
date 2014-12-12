#!/usr/bin/env python

import StochLib

StochParams = StochLib.pyStochParams()
ModelParams = StochLib.pyModelParams()
Interventions = StochLib.pyModelParams()
t_interventions = 300    # The day the interventions start.
OutputFileName = "NONE"  # Filename for output. "NONE" gives no file.

# StochParams holds the parameters needed for the stochastic
# solver. Initialize like this:
StochParams.setN_samples(200)
StochParams.setTrajectories(10)
StochParams.setI_init(3)
StochParams.setS_init(199997)
StochParams.setH_init(0)
StochParams.setF_init(0)
StochParams.setR_init(0)
StochParams.setE_init(0)
StochParams.setT_final(250.0)

# ModelParams holds the parameters needed for the model.
# These are the values used when the solver starts.
ModelParams.setBeta_I(0.084)
ModelParams.setBeta_H(0.11342857)
ModelParams.setBeta_F(1.0932857)
ModelParams.setAlpha(0.142857)
ModelParams.setGamma_h(0.2)
ModelParams.setGamma_f(0.5)
ModelParams.setGamma_i(0.1)
ModelParams.setGamma_d(0.104167)
ModelParams.setTheta_1(0.67)
ModelParams.setDelta_1(0.8)
ModelParams.setDelta_2(0.8)

# Interventions is another pyModelParams object. It holds
# the values of the model parameters after interventions.
Interventions.setBeta_I(0.084)
Interventions.setBeta_H(0.03)
Interventions.setBeta_F(0.15)
Interventions.setAlpha(0.142857)
Interventions.setGamma_h(0.2)
Interventions.setGamma_f(0.5)
Interventions.setGamma_i(0.1)
Interventions.setGamma_d(0.104167)
Interventions.setTheta_1(0.67)
Interventions.setDelta_1(0.8)
Interventions.setDelta_2(0.8)

# Run the solver. StochLib.StochCalc returns the estimated
# total number of deaths.
k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                       t_interventions, OutputFileName)

print "The total number of deaths is: " + repr(k)
