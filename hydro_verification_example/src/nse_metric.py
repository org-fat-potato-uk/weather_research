import numpy as np

def nse(observed, simulated):
    """Calculate Nash-Sutcliffe Efficiency."""
    observed = np.array(observed)
    simulated = np.array(simulated)
    return 1 - np.sum((observed - simulated)**2) / np.sum((observed - np.mean(observed))**2)
