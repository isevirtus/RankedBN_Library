import numpy as np
from scipy.stats import truncnorm

def mix_and_transform_with_tnormal(estados_pais, pesos, repository, variance, func_comb):
    #Validation
    if not estados_pais:
        raise KeyError("estados_pais is empty")

    pesos = np.array(pesos, dtype=float)
    if len(pesos) != len(estados_pais):
        raise ValueError("length mismatch between pesos and estados_pais")
    if np.any(pesos < 0):
        raise ValueError("invalid weights (negative values)")
    if np.sum(pesos) <= 0:
        raise ValueError("invalid weights (sum ≤ 0)")

    amostras_por_pai = []
    for estado in estados_pais:
        if estado not in repository:
            raise KeyError(f"Estado {estado} not in repository")
        samples = repository[estado]['amostras']
        if len(samples) < 10000:
            raise ValueError("less than 10 000 samples")
        #amostras_por_pai.append(np.random.choice(samples, size=10000, replace=False))
        amostras_por_pai.append(np.array(samples[:10000]))

    intercalado = [item for pair in zip(pesos, amostras_por_pai) for item in pair] #adaptado para empacotar pesos e amostras
    valores_continuos = func_comb(*intercalado)

    
    if (not isinstance(valores_continuos, np.ndarray) or
        valores_continuos.ndim != 1 or
        len(valores_continuos) != 10000 or
        np.any(valores_continuos < 0) or
        np.any(valores_continuos > 1)):
        raise ValueError("incompatible shape or values returned by func_comb")

    mean = np.mean(valores_continuos)
    if variance <= 0:
        variance = 0.0001 #ATRIBUINDO VALOR MINIMO PRA EVITAR ERERRO COM VARIANCIA NULA OU NEGATICA
    max_variance = mean * (1 - mean)
    if variance > max_variance:
        variance = max(max_variance, 0.0001)  # garante limite mínimo pra variancia
        #raise ValueError("variance exceeds μ(1-μ)")
    std = np.sqrt(variance)
    
    try:
        dist = truncnorm((0 - mean) / std, (1 - mean) / std, loc=mean, scale=std)
    except (FloatingPointError, ZeroDivisionError):
        raise ValueError("invalid distribution parameters")

    bins = np.linspace(0, 1, 6)
    probs = np.array([dist.cdf(bins[i+1]) - dist.cdf(bins[i]) for i in range(5)])
    probs = np.round(probs, 3)

    if np.abs(np.sum(probs) - 1) > 1e-6:
        probs /= np.sum(probs)  # Renormaliza

    return np.round(probs, 3)