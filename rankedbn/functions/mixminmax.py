import numpy as np

def mixminmax(*args):
    """
    Calculates:
      (wmin * min(values) + wmax * max(values)) / (wmin + wmax)
    Subject to:
      - All weights must be non-negative
      - Return None if sum of weights is zero
      - Raise ValueError if invalid arguments are passed
    Expected Input:
      mixminmax(w1, x1, w2, x2, ..., wn, xn)
    """
    if len(args) % 2 != 0:
        raise ValueError("An even number of arguments (weight-value pairs) is required.")

    n = len(args) // 2
    weights = [args[2 * i] for i in range(n)]
    values = [args[2 * i + 1] for i in range(n)]

    if any(w < 0 for w in weights):
        raise ValueError("Weights must be non-negative.")
    if sum(weights) == 0:
        return None

    values_array = np.array(values)  # matriz N x amostras
    mins = np.min(values_array, axis=0)
    maxs = np.max(values_array, axis=0)

    return (weights[0] * mins + weights[1] * maxs) / sum(weights)