
import random       
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import time
import csv


from functions import functions
from functions.mixture import mix_and_transform_with_tnormal



def gerar_pesos(n_pais):
    return np.random.randint(1, 6, size=n_pais)  # Valores entre 1 e 5 deve esr dado na entrada na chamadado ag


variancias = [0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5] # io deve er paado na chamada do ag
# Representação do Indivíduo
class Individuo:
    def __init__(self, n_pais, expert_data):
        self.funcao = random.choice(list(functions.keys()))
        self.pesos = gerar_pesos(n_pais)
        self.variancia = random.choice(variancias)
        self.fitness = None
        self.expert_data = expert_data

    def avaliar(self, repository, verbose=False):
        erros = []
        self.probs_por_cenario = []

        for c in self.expert_data:
            estados_pais = [c["AT"], c["AC"]] if "AE" not in c else [c["AT"], c["AC"], c["AE"]]
            probs_model = mix_and_transform_with_tnormal(estados_pais, self.pesos, repository, variance=self.variancia, func_comb=functions[self.funcao])
            erro = mean_squared_error(c["AE_expert"], probs_model)

            self.probs_por_cenario.append({
                "cenario": estados_pais,
                "esperado": c["AE_expert"],
                "calculado": probs_model.tolist(),
                "brier": erro
            })
            erros.append(erro)
            if verbose:
                print(f"Cenário: {estados_pais}")
                print(f"Esperado: {c['AE_expert']}")
                print(f"Calculado: {np.round(probs_model, 4).tolist()}")
                print(f"Brier Score: {erro:.5f}\n")

        self.fitness = np.mean(erros)
        return self.fitness


def exportar_resultados_excel_like(individuo):
    print("\nVarA\tVarB\tVL\tL\tM\tH\tVH\tVL\tL\tM\tH\tVH\tBrier")
    for r in individuo.probs_por_cenario:
        a, b = r["cenario"][:2]  # usa só os dois primeiros, mesmo com 3 pais
        esperado = "\t".join(str(e) for e in r["esperado"])
        calculado = "\t".join(f"{p:.3f}" for p in r["calculado"])
        print(f"{a}\t{b}\t{esperado}\t{calculado}\t{r['brier']:.5f}")



# Inicialização da População
def inicializar_populacao(tam_pop, n_pais, expert_data):
    return [Individuo(n_pais, expert_data) for _ in range(tam_pop)]


# Seleção por Torneio
def selecao_torneio(populacao, k=3):
    return min(random.sample(populacao, k), key=lambda ind: ind.fitness)

# Crossover de 1 Ponto
def crossover(pai1, pai2):
    
    filho = Individuo(len(pai1.pesos), pai1.expert_data)
    filho.funcao = pai1.funcao if random.random() < 0.5 else pai2.funcao
    ponto = random.randint(1, len(pai1.pesos) - 1)
    filho.pesos = np.concatenate((pai1.pesos[:ponto], pai2.pesos[ponto:]))
    #filho.pesos = np.round(filho.pesos / np.sum(filho.pesos), 2) #REMOVIDA A NORMALIZACÃO
    filho.variancia = random.choice([pai1.variancia, pai2.variancia])
    return filho

# Mutação
def mutacao(ind, taxa_mutacao):
    if random.random() < taxa_mutacao:
        ind.funcao = random.choice(list(functions.keys()))
    if random.random() < taxa_mutacao:
        ind.pesos = gerar_pesos(len(ind.pesos))
    if random.random() < taxa_mutacao:
        ind.variancia = random.choice(variancias)
    return ind

# Algoritmo Genético Principal
def algoritmo_genetico(tam_pop, n_pais, max_gen, taxa_mutacao, repository, functions, expert_data):
    populacao = inicializar_populacao(tam_pop, n_pais, expert_data)

    for ind in populacao:
        ind.avaliar(repository)

    for geracao in range(max_gen):
        nova_populacao = []
        elite = min(populacao, key=lambda ind: ind.fitness)
        nova_populacao.append(elite)  # Elitismo

        while len(nova_populacao) < tam_pop:
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)
            # ✅ Controle da Taxa de Cruzamento (80%)
            if random.random() < 0.8:
                filho = crossover(pai1, pai2)
            else:
                filho = selecao_torneio(populacao)  # Replicação direta de um pai
            
            filho = mutacao(filho, taxa_mutacao)
            filho.avaliar(repository)
            nova_populacao.append(filho)

        populacao = nova_populacao
        
        # Logging
        melhores = sorted(populacao, key=lambda ind: ind.fitness)
        #print(f"[GEN {geracao}] Melhor Brier: {melhores[0].fitness:.5f} | Função: {melhores[0].funcao} | Pesos: {melhores[0].pesos} | Variância: {melhores[0].variancia}")


    melhor = min(populacao, key=lambda ind: ind.fitness)
    print("\nMelhor configuração encontrada:")
    print(f"Função: {melhor.funcao}, Pesos: {melhor.pesos}, Variância: {melhor.variancia}, Brier Score: {melhor.fitness}")
    print("\n📋 Probabilidades e Brier Score por cenário:")
    melhor.avaliar(repository, verbose=True)
    return melhor


def run_ga_optimization(expert_data, repository, tam_pop=50, max_gen=10, taxa_mutacao=0.1, nome_arquivo="resultados_ag.csv"):
    n_pais = len([k for k in expert_data[0] if k.startswith("A") and k != "AE_expert"])
    melhor_ind = algoritmo_genetico(
        tam_pop=tam_pop,
        n_pais=n_pais,
        max_gen=max_gen,
        taxa_mutacao=taxa_mutacao,
        repository=repository,
        functions=functions,
        expert_data=expert_data
    )
    salvar_resultados_csv(melhor_ind, nome_arquivo)
    return melhor_ind


def salvar_resultados_csv(individuo, nome_arquivo="resultados_ag.csv"):
    import csv

    cabecalho = ["VarA", "VarB", "VL_exp", "L_exp", "M_exp", "H_exp", "VH_exp",
                 "VL_calc", "L_calc", "M_calc", "H_calc", "VH_calc", "Brier"]

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=';')
        writer.writerow(cabecalho)

        for r in individuo.probs_por_cenario:
            estados = r["cenario"]
            esperado = r["esperado"]
            calculado = [f"{p:.5f}".replace('.', ',') for p in r["calculado"]]
            brier = f"{r['brier']:.5f}".replace('.', ',')

            if len(estados) == 2:
                linha = [estados[0], estados[1]] + esperado + calculado + [brier]
            elif len(estados) == 3:
                linha = [estados[0], estados[1], estados[2]] + esperado + calculado + [brier]
                if len(cabecalho) == 13:
                    cabecalho.insert(2, "VarC")
                    writer.writerow(cabecalho)

            writer.writerow(linha)

    print(f"\n✅ CSV salvo em: {nome_arquivo}")


def run_ga_optimization(expert_data, repository, tam_pop=50, max_gen=10, taxa_mutacao=0.1, nome_arquivo="resultados_ag.csv"):
    n_pais = len([k for k in expert_data[0] if k.startswith("A") and k != "AE_expert"])
    melhor_ind = algoritmo_genetico(
        tam_pop=tam_pop,
        n_pais=n_pais,
        max_gen=max_gen,
        taxa_mutacao=taxa_mutacao,
        repository=repository,
        functions=functions,
        expert_data=expert_data
    )
    salvar_resultados_csv(melhor_ind, nome_arquivo)
    return melhor_ind
