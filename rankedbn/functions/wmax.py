import numpy as np

def wmax(*args):
    
    if len(args) % 2 != 0:
        return None

    n = len(args) // 2
    if n < 2:
        return None

    weights = []
    values = []
    for i in range(n):
        w_i = args[2 * i]
        x_i = args[2 * i + 1]
        if w_i < 0 or not np.all((0 <= x_i) & (x_i <= 1)): #adaptando essa linha para trabalhar com vetores de amostras, e não com valores escalares.
            return None
        weights.append(w_i)
        values.append(x_i)

    all_zero_denominators = True
    for i in range(n):
        denom = weights[i] + (n - 1)
        if denom != 0:
            all_zero_denominators = False
            break
    if all_zero_denominators:
        return None

    max_e = None
    sum_all = sum(values)
    for i in range(n):
        w_i = weights[i]
        x_i = values[i]
        denom = w_i + (n - 1)
        numerator = w_i * x_i + (sum_all - x_i)
        e_i = numerator / denom
        if max_e is None: #adaptando aqui para comparar arrays posição a posição.
            max_e = e_i
        else:
            max_e = np.maximum(max_e, e_i)
    return max_e