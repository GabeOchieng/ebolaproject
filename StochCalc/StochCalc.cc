#include "StochCalc.h"
#include "StochParams.h"
#include "ModelParams.h"
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <random>
#include <math.h>

float StochCalc(StochParams *myStochParams, ModelParams *myModel,
                ModelParams *interventions, float t_interventions,
                std::string OutputFileName) {
  FILE * outFile;

  int Trajectories;
  double beta_I, beta_H, beta_F, alpha, gamma_h, theta_1, gamma_dh;
  double delta_1, delta_2, gamma_f, gamma_i, gamma_d, gamma_ih;
  int S_init, E_init, I_init, H_init, F_init, R_init;
  int S, E, I, H, F, R, N;
  double t = 0.0;
  double t_final;
  int N_samples;
  double total_deaths = 0;  // Total number of deaths.

  /* Parameter Definitions. */
  N_samples = myStochParams->N_samples;
  t_final = myStochParams->t_final;
  Trajectories = myStochParams->Trajectories;
  I_init = myStochParams->I_init;
  S_init = myStochParams->S_init;
  H_init = myStochParams->H_init;
  F_init = myStochParams->F_init;
  R_init = myStochParams->R_init;
  E_init = myStochParams->E_init;

  /* Stochastic rate parameters. */
  beta_I = myModel->beta_I;
  beta_H = myModel->beta_H;
  beta_F = myModel->beta_F;
  alpha = myModel->alpha;
  gamma_h = myModel->gamma_h;
  theta_1 = myModel->theta_1;
  delta_1 = myModel->delta_1;
  delta_2 = myModel->delta_2;
  gamma_f = myModel->gamma_f;
  gamma_i = myModel->gamma_i;
  gamma_d = myModel->gamma_d;

  /* Initialize arrays to store the compartment values at the sample
     times and arrays to store the average and standard deviations
     of the compartment values across the different trajectories.*/
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

  double S_sigma[N_samples+1];
  double E_sigma[N_samples+1];
  double I_sigma[N_samples+1];
  double H_sigma[N_samples+1];
  double F_sigma[N_samples+1];
  double R_sigma[N_samples+1];

  /* Total population. */
  N = S_init + E_init + I_init + H_init + F_init + R_init;

  gamma_ih = 1 / (1 / gamma_i - 1 / gamma_h);
  gamma_dh = 1 / (1 / gamma_d - 1 / gamma_h);

  /* Initialize the time array. */
  for (int i = 0; i < N_samples+1; ++i) {
    t_array[i] = i * t_final / (double)N_samples;
  }

  /* Initialize the compartmental model arrays. Averages and Standard
     deviations are initialized to zero and updated recursively. The
     current array values are initialized to -1 for purposes of
     sampling over time. */
  for (int i = 0; i < N_samples+1; ++i) {
    S_array[i] = E_array[i] = I_array[i] = H_array[i] = F_array[i] = \
      R_array[i] = -1;
    S_avg[i] = E_avg[i] = I_avg[i] = H_avg[i] = F_avg[i] = R_avg[i] = 0;
    S_sigma[i] = E_sigma[i] = I_sigma[i] = H_sigma[i] = F_sigma[i] = \
      R_sigma[i] = 0;
  }

  /* Initialize a random number generator and a uniform distribution. */
  std::default_random_engine generator;
  std::uniform_real_distribution<double> uni_dist(0.0, 1.0);

  /* Begin the stochastic solver. Each trajectory represents one
     possible outcome of the epidemic. */
  for (int i = 1; i <= Trajectories; ++i) {
    S = S_init;
    E = E_init;
    I = I_init;
    H = H_init;
    F = F_init;
    R = R_init;

    /* Reinitialize the arrays storing the compartmental models to -1
       for time-sampling purposes. */
    for (int k = 0; k < N_samples+1; ++k) {
      S_array[k] = E_array[k] = I_array[k] = H_array[k] = F_array[k] =  \
        R_array[k] = -1;
    }

    /* Initialize the first element of each array to the initial values. */
    S_array[0] = S_init;
    E_array[0] = E_init;
    I_array[0] = I_init;
    H_array[0] = H_init;
    F_array[0] = F_init;
    R_array[0] = R_init;

    /* Step forward through the reactions until the final time is reached. */
    while (t < t_final) {

      if (t > t_interventions) {
        /* Activate the interventions. */
        beta_I = interventions->beta_I;
        beta_H = interventions->beta_H;
        beta_F = interventions->beta_F;
        alpha = interventions->alpha;
        gamma_h = interventions->gamma_h;
        theta_1 = interventions->theta_1;
        delta_1 = interventions->delta_1;
        delta_2 = interventions->delta_2;
        gamma_f = interventions->gamma_f;
        gamma_i = interventions->gamma_i;
        gamma_d = interventions->gamma_d;
      }

      /* Total reaction rate. */
      double R_tot;

      /* Probability that the next reaction will be a certain reaction. */
      double prob_1, prob_2, prob_3, prob_4, prob_5, prob_6, prob_7, prob_8;
      
      R_tot = (beta_I*S*I + beta_H*S*H + beta_F*S*F)/N + alpha*E +  \
        gamma_h*theta_1*I + gamma_dh*delta_2*H + gamma_f*F +            \
        gamma_i*(1 - theta_1)*(1 - delta_1)*I + delta_1*(1 - theta_1)*gamma_d * \
        I + gamma_ih*(1 - delta_2)*H;

      /* If the total reaction rate is greater than zero (reactions are still
         occurring), calculate the propabilites that determine what the next
         reaction will be. */
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
      
      /* Initialize an exponential distribution with mean one over the total
         reaction rate. */
      std::exponential_distribution<double> exp_dist(R_tot);
      
      /* Choose the time step as a random number from the exponential 
         distribution. */
      double delta_t = exp_dist(generator);

      /* When the reaction rate goes to zero (no more reactions are occurring),
         delta_t becomes zero. We must have a positive time step so that the
         solution keeps proceeding. */
      if (delta_t == 0) {
        delta_t = 1.0;
      }

      /* Choose a random number from the uniform distribution to determine which
         reaction occurs next. */
      double rand_num = uni_dist(generator);

      /* Step forward the reaction. Using the random number and the probabilities
         that the next reaction will be a certain reaction, the reaction that
         actually occurs is selected. */

      /*Reaction 1 (S -> E) */
      if (rand_num < prob_1 && R_tot > 0) {
        --S;
        ++E;
      }
      /* Reaction 2 (E -> I) */
      else if (rand_num < prob_1 + prob_2 && R_tot > 0) {
        --E; 
        ++I;
      }
      /* Reaction 3 (I -> H) */
      else if (rand_num < prob_1 + prob_2 + prob_3 && R_tot > 0) {
        --I; 
        ++H;
      }
      /* Reaction 4 (H -> F) */
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 && R_tot > 0) {
        total_deaths += 1; // Increment number of deaths.
        --H;
        ++F;
      }
      /* Reaction 5 (F -> R) */
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 && \
               R_tot > 0) {
        --F; 
        ++R;
      }
      /* Reaction 6 (I -> R) */
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 + \
               prob_6 && R_tot > 0) {
        --I; 
        ++R;
      }
      /* Reaction 7 (I -> F) */
      else if (rand_num < prob_1 + prob_2 + prob_3 + prob_4 + prob_5 + prob_6 \
               + prob_7 && R_tot > 0) {
        total_deaths += 1; // Increment number of deaths.
        --I; 
        ++F;
      }
      /* Reaction 8 (H -> R) */
      else if (R_tot > 0) {
        --H; 
        ++R;
      }
      
      /* Update the time. */
      t += delta_t;

      /* Store the current compartment values in the appropriate bins
         in the arrays. */
      for (int k = 0; k < N_samples; ++k) {
        if (t > t_array[k] && t < t_array[k+1]) {
          S_array[k+1] = S;
          E_array[k+1] = E;
          I_array[k+1] = I;
          H_array[k+1] = H;
          F_array[k+1] = F;
          R_array[k+1] = R;
        }
      }
    }
    t = 0;

    /* If some of the bins are empty after the sampling, populate them
       with the previous bins values. */
    for (int k = 1; k < N_samples+1; ++k) {
      if (S_array[k] == -1) {
        S_array[k] = S_array[k-1];
        E_array[k] = E_array[k-1];
        I_array[k] = I_array[k-1];
        H_array[k] = H_array[k-1];
        F_array[k] = F_array[k-1];
        R_array[k] = R_array[k-1];
      }
    }

    /* Calculate the average values of the number of people in each
       compartment over time, averaged over all of the trajectories. */
    for (int j = 0; j < N_samples+1; ++j) {
      S_avg[j] = (S_avg[j] * (i - 1) + S_array[j]) / i;
      E_avg[j] = (E_avg[j] * (i - 1) + E_array[j]) / i;
      I_avg[j] = (I_avg[j] * (i - 1) + I_array[j]) / i;
      H_avg[j] = (H_avg[j] * (i - 1) + H_array[j]) / i;
      F_avg[j] = (F_avg[j] * (i - 1) + F_array[j]) / i;
      R_avg[j] = (R_avg[j] * (i - 1) + R_array[j]) / i;
    }

    /* Calculate the standard deviations in two passes. */
    for (int j = 0; j < N_samples+1; ++j) {
      S_sigma[j] += (S_array[j] - S_avg[j]) * (S_array[j] - S_avg[j]);
      E_sigma[j] += (E_array[j] - E_avg[j]) * (E_array[j] - E_avg[j]);
      I_sigma[j] += (I_array[j] - I_avg[j]) * (I_array[j] - I_avg[j]);
      H_sigma[j] += (H_array[j] - H_avg[j]) * (H_array[j] - H_avg[j]);
      F_sigma[j] += (F_array[j] - F_avg[j]) * (F_array[j] - F_avg[j]);
      R_sigma[j] += (R_array[j] - R_avg[j]) * (R_array[j] - R_avg[j]);
    }

    for (int j = 0; j < N_samples+1; ++j) {
      S_sigma[j] = pow(S_sigma[j] / N_samples, 0.5);
      E_sigma[j] = pow(E_sigma[j] / N_samples, 0.5);
      I_sigma[j] = pow(I_sigma[j] / N_samples, 0.5);
      H_sigma[j] = pow(H_sigma[j] / N_samples, 0.5);
      F_sigma[j] = pow(F_sigma[j] / N_samples, 0.5);
      R_sigma[j] = pow(R_sigma[j] / N_samples, 0.5);
    }
  }

  /* Calculate the average total deaths per trajectory. */
  total_deaths = total_deaths / Trajectories;

  /* Check for desired user output file. */
  if (OutputFileName != "NONE") {
    outFile = fopen (OutputFileName.c_str(), "w");

    /* Print results to the output file. */
    fprintf(outFile, "t (days), S(avg), E(avg), I(avg), H(avg), F(avg), R(avg)\n");
    for (int i = 0; i < N_samples; ++i) {
      fprintf(outFile, "%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n", t_array[i], \
              S_avg[i], E_avg[i], I_avg[i], H_avg[i], F_avg[i], R_avg[i]);
    }
    
    fprintf(outFile,"\n");
    
    fprintf(outFile, "t (days), S(std dev), E(std dev), I(std dev), H(std dev), "
            "F(std dev), R(std dev)\n");
    for (int i = 0; i < N_samples; ++i) {
      fprintf(outFile, "%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n", t_array[i], \
              S_sigma[i], E_sigma[i], I_sigma[i], H_sigma[i], F_sigma[i], \
              R_sigma[i]);
    }

    fclose(outFile);
  }

  return total_deaths;
}
