#ifndef STOCHPARAMS_H
#define STOCHPARAMS_H
 
class StochParams { 
public:
  int N_samples, Trajectories;
  int I_init, S_init, H_init, F_init, R_init, E_init;
  double t_final;

  StochParams();
  ~StochParams();
};
#endif
