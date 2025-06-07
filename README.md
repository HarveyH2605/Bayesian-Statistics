# Bayesian-Statistics

This repository contains research and experiments aimed at identifying statistical edges for algorithmic trading using Fundamental Bayesian Statistics. Topics include Bayesian inference of a Binomial Proportion, Markov Chain Monte Carlo (MCMC) Methods, Bayesian Linear Regression, and Bayesian Stochastic Volatility Models. Each module explores how Bayesian approaches can enhance decision-making and uncertainty estimation in trading algorithms.

## Bayesian Inference of a Binomial Proportion 

- This module covers Bayesian inference for a binomial proportion using a conjugate prior framework. It begins with the Bernoulli likelihood, models prior beliefs with the Beta distribution, and derives the posterior distribution analytically. The posterior is also a Beta distribution, enabling efficient updates as new binary data is observed.

## Markov Chain Monte Carlo (MCMC) Methods

- This section introduces Markov Chain Monte Carlo (MCMC) as a tool for Bayesian inference. It covers the basics of MCMC, the Metropolis algorithm, and shows how to use it to estimate a binomial proportion when exact solutions aren’t practical.

## Bayesian Linear Regression 

- This section covers Bayesian Linear Regression using a generalized linear model (GLM) framework. It demonstrates how to incorporate prior beliefs into the model and obtain posterior distributions over parameters. The results are then compared with frequentist linear regression, highlighting differences in uncertainty quantification and parameter estimation.

## Bayesian Stochastic Volatility Model 

- This section presents a Bayesian Stochastic Volatility model for capturing time-varying volatility in financial returns. Implemented in PyMC3, it covers price data retrieval, model setup, and inference using NUTS. The Bayesian approach allows for full uncertainty quantification of latent volatility.
