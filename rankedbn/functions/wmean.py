import numpy as np

def wmean(*args):
    
    if len(args) % 2 != 0:
        raise ValueError("An even number of arguments (weight-value pairs) is required.")

    partial_sum_value = 0.0
    partial_sum_weight = 0.0

    for i in range(0, len(args), 2):
        w = args[i]
        x = args[i + 1]
        partial_sum_value += w * x
        partial_sum_weight += w

    if partial_sum_weight == 0:
        return None

    return partial_sum_value / partial_sum_weight