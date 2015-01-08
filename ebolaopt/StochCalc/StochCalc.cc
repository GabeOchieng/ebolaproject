#include "StochCalc.h"
#include "StochParams.h"
#include "ModelParams.h"
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <random>
#include <math.h>
#include <omp.h>

float StochCalc(StochParams *myStochParams, ModelParams *myModel,
                ModelParams *interventions, float t_interventions,
                std::string OutputFileName, int nthreads) {
  FILE * outFile;

  int Trajectories;
  double beta_I, beta_H, beta_F, alpha, gamma_h, theta_1, gamma_dh;
  double delta_1, delta_2, gamma_f, gamma_i, gamma_d, gamma_ih;
  int S_init, E_init, I_init, H_init, F_init, R_init;
  int S, E, I, H, F, R, N;
  double t = 0.0;
  double t_final;
  int N_samples;
  double total_deaths[nthreads];  // Total number of deaths.

  for (int i = 0; i < nthreads; ++i) {
    total_deaths[i] = 0;
  }

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
  double t_array [N_samples+1][nthreads];
  int S_array [N_samples+1][nthreads];
  int E_array [N_samples+1][nthreads];
  int I_array [N_samples+1][nthreads];
  int H_array [N_samples+1][nthreads];
  int F_array [N_samples+1][nthreads];
  int R_array [N_samples+1][nthreads];

  double S_avg [N_samples+1][nthreads];
  double E_avg [N_samples+1][nthreads];
  double I_avg [N_samples+1][nthreads];
  double H_avg [N_samples+1][nthreads];
  double F_avg [N_samples+1][nthreads];
  double R_avg [N_samples+1][nthreads];

  double S_avg_true [N_samples+1];
  double E_avg_true [N_samples+1];
  double I_avg_true [N_samples+1];
  double H_avg_true [N_samples+1];
  double F_avg_true [N_samples+1];
  double R_avg_true [N_samples+1];

  double S_sigma[N_samples+1][nthreads];
  double E_sigma[N_samples+1][nthreads];
  double I_sigma[N_samples+1][nthreads];
  double H_sigma[N_samples+1][nthreads];
  double F_sigma[N_samples+1][nthreads];
  double R_sigma[N_samples+1][nthreads];

  /* Total population. */
  N = S_init + E_init + I_init + H_init + F_init + R_init;

  gamma_ih = 1 / (1 / gamma_i - 1 / gamma_h);
  gamma_dh = 1 / (1 / gamma_d - 1 / gamma_h);

  /* Initialize the time array. */
  for (int i = 0; i < N_samples+1; ++i) {
    for (int j = 0; j < nthreads; ++j) {
      t_array[i][j] = i * t_final / (double)N_samples;
    }
  }

  /* Initialize the compartmental model arrays. Averages and Standard
     deviations are initialized to zero and updated recursively. The
     current array values are initialized to -1 for purposes of
     sampling over time. */
  for (int i = 0; i < N_samples+1; ++i) {
    for (int j = 0; j < nthreads; ++j) {
      S_array[i][j] = E_array[i][j] = I_array[i][j] = H_array[i][j] = \
	F_array[i][j] = R_array[i][j] = -1;
      S_avg[i][j] = E_avg[i][j] = I_avg[i][j] = H_avg[i][j] = F_avg[i][j] = \
	R_avg[i][j] = 0;
      S_sigma[i][j] = E_sigma[i][j] = I_sigma[i][j] = H_sigma[i][j] = \
	F_sigma[i][j] = R_sigma[i][j] = 0;
    }
    S_avg_true[i] = E_avg_true[i] = I_avg_true[i] = H_avg_true[i] = \
      F_avg_true[i] = R_avg_true[i] = 0;
  }

  /* Initialize a random number generator and a uniform distribution. */
  std::default_random_engine generator;
  std::uniform_real_distribution<double> uni_dist(0.0, 1.0);

  int chunk = Trajectories / nthreads;

  // Initialize the parallel environment.
#pragma omp parallel num_threads(nthreads) default(shared) \
  private(S, E, I, H, F, R, t, beta_I, beta_H, beta_F, alpha, \
  gamma_h, theta_1, delta_1, delta_2, gamma_f, gamma_i, gamma_d)
{
  int tid = omp_get_thread_num();
  // Begin the parallel for loop.
#pragma omp for schedule(static, chunk) nowait

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
      S_array[k][tid] = E_array[k][tid] = I_array[k][tid] = H_array[k][tid] = \
	F_array[k][tid] = R_array[k][tid] = -1;
    }

    /* Initialize the first element of each array to the initial values. */
    S_array[0][tid] = S_init;
    E_array[0][tid] = E_init;
    I_array[0][tid] = I_init;
    H_array[0][tid] = H_init;
    F_array[0][tid] = F_init;
    R_array[0][tid] = R_init;

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
      else {
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
        total_deaths[tid] += 1; // Increment number of deaths.
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
        total_deaths[tid] += 1; // Increment number of deaths.
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
        if (t > t_array[k][tid] && t < t_array[k+1][tid]) {
          S_array[k+1][tid] = S;
          E_array[k+1][tid] = E;
          I_array[k+1][tid] = I;
          H_array[k+1][tid] = H;
          F_array[k+1][tid] = F;
          R_array[k+1][tid] = R;
        }
      }
    }
    t = 0;

    /* If some of the bins are empty after the sampling, populate them
       with the previous bins values. */
    for (int k = 1; k < N_samples+1; ++k) {
      if (S_array[k][tid] == -1) {
        S_array[k][tid] = S_array[k-1][tid];
        E_array[k][tid] = E_array[k-1][tid];
        I_array[k][tid] = I_array[k-1][tid];
        H_array[k][tid] = H_array[k-1][tid];
        F_array[k][tid] = F_array[k-1][tid];
        R_array[k][tid] = R_array[k-1][tid];
      }
    }

    /* Calculate the average values of the number of people in each
       compartment over time, averaged over all of the trajectories. */
    for (int j = 0; j < N_samples+1; ++j) {
      int k = i - tid * chunk;
      S_avg[j][tid] = (S_avg[j][tid] * (k - 1) + S_array[j][tid]) / k;
      E_avg[j][tid] = (E_avg[j][tid] * (k - 1) + E_array[j][tid]) / k;
      I_avg[j][tid] = (I_avg[j][tid] * (k - 1) + I_array[j][tid]) / k;
      H_avg[j][tid] = (H_avg[j][tid] * (k - 1) + H_array[j][tid]) / k;
      F_avg[j][tid] = (F_avg[j][tid] * (k - 1) + F_array[j][tid]) / k;
      R_avg[j][tid] = (R_avg[j][tid] * (k - 1) + R_array[j][tid]) / k;
    }

    /* Calculate the standard deviations in two passes. */
    for (int j = 0; j < N_samples+1; ++j) {
      S_sigma[j][tid] += (S_array[j][tid] - S_avg[j][tid]) * (S_array[j][tid] - S_avg[j][tid]);
      E_sigma[j][tid] += (E_array[j][tid] - E_avg[j][tid]) * (E_array[j][tid] - E_avg[j][tid]);
      I_sigma[j][tid] += (I_array[j][tid] - I_avg[j][tid]) * (I_array[j][tid] - I_avg[j][tid]);
      H_sigma[j][tid] += (H_array[j][tid] - H_avg[j][tid]) * (H_array[j][tid] - H_avg[j][tid]);
      F_sigma[j][tid] += (F_array[j][tid] - F_avg[j][tid]) * (F_array[j][tid] - F_avg[j][tid]);
      R_sigma[j][tid] += (R_array[j][tid] - R_avg[j][tid]) * (R_array[j][tid] - R_avg[j][tid]);
    }
  }

  for (int j = 0; j < N_samples+1; ++j) {
    S_sigma[j][tid] = pow(S_sigma[j][tid] / (chunk - 1), 0.5);
    E_sigma[j][tid] = pow(E_sigma[j][tid] / (chunk - 1), 0.5);
    I_sigma[j][tid] = pow(I_sigma[j][tid] / (chunk - 1), 0.5);
    H_sigma[j][tid] = pow(H_sigma[j][tid] / (chunk - 1), 0.5);
    F_sigma[j][tid] = pow(F_sigma[j][tid] / (chunk - 1), 0.5);
    R_sigma[j][tid] = pow(R_sigma[j][tid] / (chunk - 1), 0.5);
  }
 }

/* Find the total average from all the threads. */
 for (int j = 0; j < N_samples+1; ++j) {
   for (int k = 0; k < nthreads; ++k) {
     S_avg_true[j] += S_avg[j][k];
     E_avg_true[j] += E_avg[j][k];
     I_avg_true[j] += I_avg[j][k];
     H_avg_true[j] += H_avg[j][k];
     F_avg_true[j] += F_avg[j][k];
     R_avg_true[j] += R_avg[j][k];
   }
   S_avg_true[j] = S_avg_true[j] / nthreads;
   E_avg_true[j] = E_avg_true[j] / nthreads;
   I_avg_true[j] = I_avg_true[j] / nthreads;
   H_avg_true[j] = H_avg_true[j] / nthreads;
   F_avg_true[j] = F_avg_true[j] / nthreads;
   R_avg_true[j] = R_avg_true[j] / nthreads;
 }

 /* Error Sum of Squares */
 double S_ESS [N_samples+1];
 double E_ESS [N_samples+1];
 double I_ESS [N_samples+1];
 double H_ESS [N_samples+1];
 double F_ESS [N_samples+1];
 double R_ESS [N_samples+1];

 /* Total Group Sum of Squares */
 double S_TGSS [N_samples+1];
 double E_TGSS [N_samples+1];
 double I_TGSS [N_samples+1];
 double H_TGSS [N_samples+1];
 double F_TGSS [N_samples+1];
 double R_TGSS [N_samples+1];

 /* Standard Deviations */
 double S_std_dev [N_samples+1];
 double E_std_dev [N_samples+1];
 double I_std_dev [N_samples+1];
 double H_std_dev [N_samples+1];
 double F_std_dev [N_samples+1];
 double R_std_dev [N_samples+1];

 /* Initialize the sum of squares and standard deviations. */
 for (int i = 0; i < N_samples+1; ++i) {
   S_ESS[i] = E_ESS[i] = I_ESS[i] = H_ESS[i] = F_ESS[i] = R_ESS[i] = 0;
   S_TGSS[i] = E_TGSS[i] = I_TGSS[i] = H_TGSS[i] = F_TGSS[i] = \
     R_TGSS[i] = 0;
   S_std_dev[i] = E_std_dev[i] = I_std_dev[i] = H_std_dev[i] = \
     F_std_dev[i] = R_std_dev[i] = 0;
 }

 /* Calculate the Sum of Squares and standard deviations. */
 for (int i = 0; i < N_samples+1; ++i) {
   for (int j = 0; j < nthreads; ++j) {
     S_ESS[i] += S_sigma[i][j] * S_sigma[i][j] * (chunk - 1);
     E_ESS[i] += E_sigma[i][j] * E_sigma[i][j] * (chunk - 1);
     I_ESS[i] += I_sigma[i][j] * I_sigma[i][j] * (chunk - 1);
     H_ESS[i] += H_sigma[i][j] * H_sigma[i][j] * (chunk - 1);
     F_ESS[i] += F_sigma[i][j] * F_sigma[i][j] * (chunk - 1);
     R_ESS[i] += R_sigma[i][j] * R_sigma[i][j] * (chunk - 1);
     
     S_TGSS[i] += pow(S_avg[i][j] - S_avg_true[i], 2.0) * chunk;
     E_TGSS[i] += pow(E_avg[i][j] - E_avg_true[i], 2.0) * chunk;
     I_TGSS[i] += pow(I_avg[i][j] - I_avg_true[i], 2.0) * chunk;
     H_TGSS[i] += pow(H_avg[i][j] - H_avg_true[i], 2.0) * chunk;
     F_TGSS[i] += pow(F_avg[i][j] - F_avg_true[i], 2.0) * chunk;
     R_TGSS[i] += pow(R_avg[i][j] - R_avg_true[i], 2.0) * chunk;
   }

   S_std_dev[i] = pow((S_ESS[i] + S_TGSS[i]) / (Trajectories - 1), 0.5);
   E_std_dev[i] = pow((E_ESS[i] + E_TGSS[i]) / (Trajectories - 1), 0.5);
   I_std_dev[i] = pow((I_ESS[i] + I_TGSS[i]) / (Trajectories - 1), 0.5);
   H_std_dev[i] = pow((H_ESS[i] + H_TGSS[i]) / (Trajectories - 1), 0.5);
   F_std_dev[i] = pow((F_ESS[i] + F_TGSS[i]) / (Trajectories - 1), 0.5);
   R_std_dev[i] = pow((R_ESS[i] + R_TGSS[i]) / (Trajectories - 1), 0.5);
 }

/* Calculate the average total deaths per trajectory. */
 for (int i = 1; i < nthreads; ++i) {
   total_deaths[0] += total_deaths[i];
  }
 total_deaths[0] = total_deaths[0] / Trajectories;
 
 /* Check for desired user output file. */
 if (OutputFileName != "NONE") {
   outFile = fopen (OutputFileName.c_str(), "w");
   
   /* Print results to the output file. */
   fprintf(outFile, "t (days), S(avg), S(std dev), E(avg), E(std dev), I(avg), "
	   "I(std dev), H(avg), H(std dev), F(avg), F(std dev), R(avg), R(std dev)\n");
   for (int i = 0; i < N_samples+1; ++i) {
     fprintf(outFile, "%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, "
	     "%.2f, %.2f, %.2f\n", t_array[i][0], S_avg_true[i], S_std_dev[i], E_avg_true[i], 
	     E_std_dev[i], I_avg_true[i], I_std_dev[i], H_avg_true[i], H_std_dev[i], 
	     F_avg_true[i], F_std_dev[i], R_avg_true[i], R_std_dev[i]);
   }

   fclose(outFile);
 }
 
 return total_deaths[0];
}
