#example/run_example.py 

from utils.loader import load_repository
from functions.mixture import mix_and_transform_with_tnormal
from functions import functions  # Dicionário com as funções wmean, wmin, etc.
from evaluation.evaluator import evaluate_and_save
from evaluation import scenarios
from genetic.genetic_algorithm import run_ga_optimization

# 1. Carregar os dados do especialista e o repositório
expert_data = scenarios.TPN3  # ou TPN4, TPN5, etc.
repository = load_repository("repository.json")

# 2. Rodar o AG para encontrar a melhor configuração
melhor_ind = run_ga_optimization(
    expert_data=expert_data,
    repository=repository,
    tam_pop=50,
    max_gen=10,
    taxa_mutacao=0.1,
    nome_arquivo="resultados_ag.csv"
)

# 3. Executar avaliação com a melhor configuração
# Detecta número de pais automaticamente
n_pais = len([k for k in expert_data[0] if k.startswith("A") and k != "AE_expert"])
pesos = melhor_ind.pesos
func = functions[melhor_ind.funcao]
var = melhor_ind.variancia

# Os pesos são fixados conforme o número de pais
if n_pais == 2:
    pesos_2p, pesos_3p = pesos, [2, 4, 2]  # 3p genérico só para não dar erro
else:
    pesos_2p, pesos_3p = [1, 1], pesos

# 4. Gerar a CPT com a melhor configuração
evaluate_and_save(
    csv_path="TPN3_melhor_config.csv",
    scenarios=expert_data,
    weights_2p=pesos_2p,
    weights_3p=pesos_3p,
    function=func,
    variance=var,
    repository=repository,
    transform_func=mix_and_transform_with_tnormal
)


