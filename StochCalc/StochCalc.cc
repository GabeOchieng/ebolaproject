#include <stdio.h>
#include <stdlib.h>
#include <random>
#include <math.h>

int main() {
  int Trajectories = 100;

  double beta_I, beta_H, beta_F, alpha, gamma_h, theta_1, gamma_dh, delta_1;
  double delta_2, gamma_f, gamma_i, gamma_d, gamma_ih;
  int S_init, E_init, I_init, H_init, F_init, R_init;
  int S, E, I, H, F, R, N;
  double t = 0.0;
  double t_final = 50.0;
  int N_samples = 50;
  int counter;

  double t_array [N_samples+1];
  int S_array [N_samples+1];
  int E_array [N_samples+1];
  int I_array [N_samples+1];
  int H_array [N_samples+1];
  int F_array [N_samples+1];
  int R_array [N_samples+1];

  double S_avg [N_samples+1];
  double E_avg [N_samples+1];
  double I_avg [N_samples+1];
  double H_avg [N_samples+1];
  double F_avg [N_samples+1];
  double R_avg [N_samples+1];

  N = 200000;

  I_init = 1;
  S_init = N - I_init;
  H_init = 0;
  F_init = 0;
  R_init = 0;
  E_init = 0;

  for (int i = 0; i < N_samples+1; ++i) {
    t_array[i] = i * t_final / (double)N_samples;
    printf("t_array[%i] = %f\n", i, t_array[i]);
  }

  for (int i = 0; i < N_samples+1; ++i) {
    S_avg[i] = 0;
    E_avg[i] = 0;
    I_avg[i] = 0;
    H_avg[i] = 0;
    F_avg[i] = 0;
    R_avg[i] = 0;
  }

  beta_I = 0.084;
  beta_H = 0.0017143;
  beta_F = 0.066;
  alpha = 0.142857;
  gamma_h = 0.2;
  theta_1 = 0.67;
  gamma_dh = 0.3;
  delta_1 = 0.8;
  delta_2 = 0.8;
  gamma_f = 0.5;
  gamma_i = 0.1;
  gamma_d = 0.104167;
  gamma_ih = 0.3;

  std::default_random_engine generator;
  std::uniform_real_distribution<double> uni_dist(0.0, 1.0);

  for (int i = 1; i <= Trajectories; ++i) {
    printf("Trajectory = %i\n", i);
    S = S_init;
    E = E_init;
    I = I_init;
    H = H_init;
    F = F_init;
    R = R_init;

    S_array[0] = S_init;
    E_array[0] = E_init;
    I_array[0] = I_init;
    H_array[0] = H_init;
    F_array[0] = F_init;
    R_array[0] = R_init;

    counter = 1;
    //printf("%i, %i, %i, %i, %i, %i\n", S, E, I, H, F, R);
    while (t < t_final) {
      //printf("%i, %i, %i, %i, %i, %i\n", S, E, I, H, F, R);

      double R_tot;
      double prob_1, prob_2, prob_3, prob_4, prob_5, prob_6, prob_7, prob_8;
      
      R_tot = (beta_I*S*I + beta_H*S*H + beta_F*S*F)/N + alpha*E +  \
        gamma_h*theta_1*I + gamma_dh*delta_2*H + gamma_f*F +            \
        gamma_i*(1 - theta_1)*(1 - delta_1)*I + delta_1*(1 - theta_1)*gamma_d * \
        I + gamma_ih*(1 - delta_2)*H;

      if (R_tot > 0) {
        prob_1 = (beta_I*S*I + beta_H*S*H + beta_F*S*F) / (N*R_tot);
        prob_2 = alpha * E / R_tot;
        prob_3 = gamma_h * theta_1 * I / R_tot;
        prob_4 = gamma_dh * delta_2 * H / R_tot;
        prob_5 = gamma_f * F / R_tot;
        prob_6 = gamma_i * (1 - theta_1) * (1 - delta_1) * I / R_tot;
        prob_7 = delta_1 * (1 - theta_1) * gamma_d * I / R_tot;
        prob_8 = gamma_ih * (1 - delta_2) * H / R_tot;
      }
      else {
        prob_1 = prob_2 = prob_3 = prob_4 = prob_5 = prob_6 = prob_7 = prob_8 = 0;
      }
      
      std::exponential_distribution<double> exp_dist(1/R_tot);
      
      double delta_t = exp_dist(generator);
      if (delta_t == 0) {
        delta_t = 1.0;
      }
      //printf("delta_t = %f\n", delta_t);
      double rand_num = uni_dist(generator);

      // Reaction 1
      if (rand_num < prob_1 && R_tot > 0) {
        --S;
        ++E;
      }
      // Reaction 2
      else if (rand_num < prob_1 + prob_2 && R_tot > 0) {
        --E;
        ++I;
      }
      // Reaction 3
      else if (rand_num < prob_1 + prob_2 + prob_3 && R_tot > 0) {
        --I;
        ++H;
      }
      // Reaction 4
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 && R_tot > 0) {
        --H;
        ++F;
      }
      // Reaction 5
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 && \
               R_tot > 0) {
        --F;
        ++R;
      }
      // Reaction 6
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 + prob_6 && \
               R_tot > 0) {
        --I;
        ++R;
      }
      // Reaction 7
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 + prob_6 \
               + prob_7 && R_tot > 0) {
        --I;
        ++F;
      }
      // Reaction 8
      else if (R_tot > 0) {
        --H;
        ++R;
      }
      
      t += delta_t;
      // at this point I have the new time and the new state of the system.

      if (t < t_array[counter]) {
        S_array[counter] = S;
        E_array[counter] = E;
        I_array[counter] = I;
        H_array[counter] = H;
        F_array[counter] = F;
        R_array[counter] = R;
        //printf("Just assigned R_array[%i] = %i\n", counter, R_array[counter]);
        //printf("S_array[%i] = %i, t = %f, t_array[%i] = %f\n", counter, S_array[counter], t, t_array[counter]);
      }
      else {
        counter += 1;
      }
      if (counter > N_samples+1)
        break;
      //printf("%i, %i, %i, %i, %i, %i\n", S, E, I, H, F, R);
    }
    t = 0;

    for (int j = 0; j < N_samples+1; ++j) {
      printf("S[%i] = %i, E = %i, I = %i, H = %i, F = %i, R = %i\n", j, S_array[j], E_array[j], I_array[j], H_array[j], F_array[j], R_array[j]);
      S_avg[j] = (S_avg[j] * (i - 1) + S_array[j]) / i;
      E_avg[j] = (E_avg[j] * (i - 1) + E_array[j]) / i;
      I_avg[j] = (I_avg[j] * (i - 1) + I_array[j]) / i;
      H_avg[j] = (H_avg[j] * (i - 1) + H_array[j]) / i;
      F_avg[j] = (F_avg[j] * (i - 1) + F_array[j]) / i;
      R_avg[j] = (R_avg[j] * (i - 1) + R_array[j]) / i;
    }
  }

  for (int i = 0; i < N_samples; ++i) {
    printf("%f %f %f %f %f %f\n", S_avg[i], E_avg[i], I_avg[i], H_avg[i], F_avg[i], R_avg[i]);
  }
  return 0;
}
