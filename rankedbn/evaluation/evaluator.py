# evaluator.py
import numpy as np
import csv
from sklearn.metrics import mean_squared_error

def evaluate_and_save(csv_path, scenarios, weights_2p, weights_3p, function, variance, repository, transform_func):
    example = scenarios[0]
    n_parents = len([k for k in example if k.startswith("A") and k != "AE_expert"])
    weights = weights_3p if n_parents == 3 else weights_2p

    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        header = (["VarA", "VarB"] + (["VarC"] if n_parents == 3 else []) +
                  ["VL_exp", "L_exp", "M_exp", "H_exp", "VH_exp", 
                   "VL_calc", "L_calc", "M_calc", "H_calc", "VH_calc", "Brier"])
        writer.writerow(header)

        briers = []
        for s in scenarios:
            states = [s[k] for k in s if k != "AE_expert"]
            expected = s["AE_expert"]
            predicted = transform_func(estados_pais=states, pesos=weights,
                                        repository=repository, variance=variance,
                                        func_comb=function)
            brier = mean_squared_error(expected, predicted)
            briers.append(brier)

            row = states + [str(e) for e in expected] + [f"{p:.5f}".replace('.', ',') for p in predicted] + [f"{brier:.5f}".replace('.', ',')]
            writer.writerow(row)

    print(f"Saved: {csv_path}, Avg Brier Score: {round(np.mean(briers), 5)}")