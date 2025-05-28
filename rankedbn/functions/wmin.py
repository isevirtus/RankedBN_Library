import numpy as np

def wmin(*args):
    if len(args) % 2 != 0:
        raise ValueError("An even number of arguments (weight-value pairs) is required.")

    n = len(args) // 2
    if n < 2:
        return None

    weights = [args[2 * i] for i in range(n)]
    values = [args[2 * i + 1] for i in range(n)]

    if sum(weights) == 0:
        return None

    S = sum(values)
    current_min = float('inf')
    for i in range(n):
        w_i = weights[i]
        denom = w_i + (n - 1)
        numerator = w_i * values[i] + (S - values[i])
        e_i = numerator / denom
        current_min = np.minimum(current_min, e_i)  # Comparação elemento a elemento (alteracao feita no codigo)

    return current_min