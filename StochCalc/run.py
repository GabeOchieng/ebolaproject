#!/usr/bin/env python

import StochLib

StochParams = StochLib.pyStochParams()
ModelParams = StochLib.pyModelParams()
Interventions = StochLib.pyModelParams()
t_interventions = 50    # The day the interventions start.
OutputFileName = "NONE"  # Filename for output. "NONE" gives no file.

# StochParams holds the parameters needed for the stochastic
# solver. Initialize like this:
StochParams.set("N_samples", 200)
StochParams.set("Trajectories", 10)
StochParams.set("I_init", 3)
StochParams.set("S_init", 199997)
StochParams.set("H_init", 0)
StochParams.set("F_init", 0)
StochParams.set("R_init", 0)
StochParams.set("E_init", 0)
StochParams.set("t_final", 250.0)

# ModelParams holds the parameters needed for the model.
# These are the values used when the solver starts.
ModelParams.set("beta_I", 0.084)
ModelParams.set("beta_H", 0.11342857)
ModelParams.set("beta_F", 1.0932857)
ModelParams.set("alpha", 0.142857)
ModelParams.set("gamma_h", 0.2)
ModelParams.set("gamma_f", 0.5)
ModelParams.set("gamma_i", 0.1)
ModelParams.set("gamma_d", 0.104167)
ModelParams.set("theta_1", 0.67)
ModelParams.set("delta_1", 0.8)
ModelParams.set("delta_2", 0.8)

# Interventions is another pyModelParams object. It holds
# the values of the model parameters after interventions.
Interventions.set("beta_I", 0.084)
Interventions.set("beta_H", 0.03)
Interventions.set("beta_F", 0.15)
Interventions.set("alpha", 0.142857)
Interventions.set("gamma_h", 0.2)
Interventions.set("gamma_f", 0.5)
Interventions.set("gamma_i", 0.1)
Interventions.set("gamma_d", 0.104167)
Interventions.set("theta_1", 0.67)
Interventions.set("delta_1", 0.8)
Interventions.set("delta_2", 0.8)

# Run the solver. StochLib.StochCalc returns the estimated
# total number of deaths.
k = StochLib.StochCalc(StochParams, ModelParams, Interventions,
                       t_interventions, OutputFileName)

print "The total number of deaths is: " + repr(k)
