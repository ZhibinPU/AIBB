"""AIBB — adaptive information-borrowing Bayesian covariance estimation with HMC.

Typical use::

    import numpy as np
    from aibb import fit_corr_aibb, significant_aibb

    X = np.random.randn(200, 3000)                 # n samples x d variables
    R_hat = fit_corr_aibb(X, preset="sim_block_n200")   # (d, d) correlation
    shrink = significant_aibb(X, preset="sim_block_n200")
    shrink["posterior_prob"]                        # per-entry shrinkage prob.

See :data:`aibb.api.HMC_PRESETS` for the tuned chain settings and ``README.md``
for the layout of the package.
"""

from .api import (
    HMC_PRESETS,
    fit_corr_aibb,
    fit_cov_aibb,
    run_chain,
    significant_aibb,
)
from .hmc import hmc_sample
from .model import CorrShrinkCovModel
from .posterior import reconstruct_corr, reconstruct_sigma, significant_mask
from .priors import log_half_cauchy, log_inv_gamma

__all__ = [
    "CorrShrinkCovModel",
    "hmc_sample",
    "log_half_cauchy",
    "log_inv_gamma",
    "reconstruct_sigma",
    "reconstruct_corr",
    "significant_mask",
    "run_chain",
    "fit_cov_aibb",
    "fit_corr_aibb",
    "significant_aibb",
    "HMC_PRESETS",
]

__version__ = "0.1.0"
