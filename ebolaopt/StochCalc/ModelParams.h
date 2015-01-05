#ifndef MODELPARAMS_H
#define MODELPARAMS_H
 
class ModelParams { 
public: 
  double beta_I, beta_H, beta_F, alpha, gamma_h, theta_1;
  double delta_1, delta_2, gamma_f, gamma_i, gamma_d;

  ModelParams();
  ~ModelParams();
};
#endif
