import matplotlib.pyplot as plt
import numpy as np
import pymc as pm
import scipy.stats as stats
import arviz as az

plt.style.use("ggplot")

# Parameters
n = 50      # Number of trials
z = 10      # Number of observed heads
alpha = 12.0
beta = 12.0
alpha_post = 22.0
beta_post = 22.0
iterations = 100000

# PyMC model
with pm.Model() as basic_model:
    theta = pm.Beta("theta", alpha=alpha, beta=beta)

    y = pm.Binomial("y", n=n, p=theta, observed=z)

    start = pm.find_MAP()

    step = pm.Metropolis()
    trace = pm.sample(iterations, step=step, start=start, random_seed=1, progressbar=True)

# Posterior histogram
theta_samples = trace.posterior["theta"].values.ravel()

bins = 50
plt.hist(
    theta_samples, bins=bins,
    histtype="step", density=True,
    label="Posterior MCMC", color="red"
)

# Prior and posterior Beta distributions
x = np.linspace(0, 1, 100)
plt.plot(x, stats.beta.pdf(x, alpha, beta), "--", label="Prior", color="blue")
plt.plot(x, stats.beta.pdf(x, alpha_post, beta_post), "--", label="Posterior", color="green")

plt.legend(title="Parameters", loc="best")
plt.xlabel("$\\theta$, Fairness")
plt.ylabel("Density")
plt.title("Bayesian Inference for Binomial Proportion")
plt.show()