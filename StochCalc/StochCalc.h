#ifndef STOCHCALC_H
#define STOCHCALC_H

#include "StochParams.h"
#include "ModelParams.h"
#include <string>

float StochCalc(StochParams *myStochParams, ModelParams *myModel,
                ModelParams *interventions, float t_interventions,
                std::string OutputFileName);

#endif
