# Questao1 - Trabalho de OTM2
#
# FELIPE MARTINS LEMOS DE MORAIS - 20193001045
# GABRIEL SIQUEIRA SILVA -20203008814
# FERNANDO GARAMVÖLGYI MAFRA VEIZAGA - 20203001902
#
# Descrição do codigo: 
# O código implementa um jogo par ou impar entre dois jogadores, onde cada jogador escolhe um número de dedos entre 1 e 10. 
# O jogo possui diferentes matrizes de prêmios. O programa realiza simulações usando estratégias mistas e calcula o total de prêmios 
# acumulados em 100 jogos. Ele compara uma solução ótima com uma ligeiramente diferente, calcula a norma euclidiana entre as soluções 
# e verifica a diferença nos somatórios de prêmios. O resultado é exibido com as probabilidades de estratégias e os valores do jogo.

import random
import numpy as np
from scipy.optimize import linprog

def rodar_estrategias_mistas(payoff_matrix):
   num_players, num_strategies = matriz_premios.shape

    # Definição da função objetivo p/maximizar o valor do jogo
   c = np.ones(num_strategies )

    # Restrições de prob. para cada estratégia
   A_eq = np.ones((1, num_strategies ))
   b_eq = np.array([1.0])

    # Restrições para n negativar as probs.
   bounds = [(0, 1) for _ in range(num_strategies )]

   probabilidades = []
   valores_jogos = []

   for jogador in range(num_players):

       # Resolução da programação linear
       resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

       #Salvando as probs e o valor do jogo para o jogador atual
       probabilidades.append(resultado.x)
       valores_jogos.append(-resultado.fun)

   # Retornar as probs de cada estratégia para cada jogador
   return probabilidades, valores_jogos


def jogoParOuImpar(matriz_premios, opcao_nao_otima=False):
   repeticoes=100
   total_premios = 0

   for _ in range(repeticoes):
      # Simulação dos números de dedos escolhidos pelos jogadores
      dedos_jogador1 = np.random.randint(1, 11)
      dedos_jogador2 = np.random.randint(1, 11)

      # Verificação se a soma dos dedos é par ou ímpar
      soma_dedos = dedos_jogador1 + dedos_jogador2
      escolha_par_ou_impar = soma_dedos % 2  # 0 para par, 1 para ímpar

      # Construção da matriz de prêmios com base na escolha par ou ímpar
      matriz_premios_jogo = matriz_premios[:, escolha_par_ou_impar]

      if opcao_nao_otima:
            # Simulação com uma solução ligeiramente distinta da ótima
            probabilidades_distintas, valores_jogos = rodar_estrategias_mistas(matriz_premios_jogo)
            # Perturbação das probabilidades
            probabilidades_distintas = perturbar_probabilidades(probabilidades_distintas, perturbacao=0.01)
            # Calcular a norma euclidiana entre as soluções
            norma_euclidiana = calcular_norma_euclidiana(probabilidades_otimas[0], probabilidades_distintas[0])
      else:
            # Simulação convencional
            probabilidades, valores_jogos = rodar_estrategias_mistas(matriz_premios_jogo)
            norma_euclidiana = 0  # Não usada nesta simulação

      # Acumulação do prêmio do jogador 1
      total_premios += valores_jogos[0]

   return total_premios, norma_euclidiana


def perturbar_probabilidades(probabilidades, perturbacao=0.01):
    perturbacao_randomica = np.random.uniform(low=-perturbacao, high=perturbacao, size=len(probabilidades))
    probabilidades_perturbadas = np.clip(probabilidades + perturbacao_randomica, 0, 1)
    probabilidades_perturbadas /= np.sum(probabilidades_perturbadas)
    return probabilidades_perturbadas

def calcular_norma_euclidiana(vetor1, vetor2):
    return np.linalg.norm(vetor1 - vetor2)


if __name__ == "__main__":

   # Settando uma matriz de prêmios inicial
   matriz_premios = np.array(
       [[3, -1], 
        [-5, -6]]
    )
   
   # Resposta a)
   prob, val = rodar_estrategias_mistas(matriz_premios)
   print(f"As probabilidades são:{prob}, e os valores do jogo são {val}")
   
   # Resposta b)
   matriz_parOuimpar = np.array([
      [1,-1],
      [-1,1]
   ])

   total_premios, _ = jogoParOuImpar(matriz_parOuimpar)
   print(f"Total prêmios do jogo de par ou ímpar: {total_premios}")

   #Resposta c)
   #(i) Solução com a tabela de prêmios fornecida
   tabela_premios_fornecida = np.array([
      [3, -1, -3], 
      [-2, 4, -1], 
      [-5, -6, -2]
   ])
   probabilidades_otimas, _ = rodar_estrategias_mistas(tabela_premios_fornecida)

   #(ii) Simulando o jogo em 100 rodadas com a solução ótima
   total_premios_otimo = jogoParOuImpar(tabela_premios_fornecida)

   #(iii) Simulando o jogo em 100 rodadas com uma solução ligeiramente diferente
   total_premios_distinta, norma_euclidiana = jogoParOuImpar(matriz_premios, True)
   print("isso aqui  ",total_premios_distinta)

   #Resultados
   print(f"Solução Ótima c/Total de prêmios acumulado em 100 jogos: {total_premios_otimo}")
   print(f"Solução Ligeiramente Diferente c/Total de prêmios acumulado em 100 jogos: {total_premios_distinta}")
   print(f"Norma Euclidiana entre as soluções: {norma_euclidiana}")

   #(iv) Comparação numerica dos somatórios dos prêmios das duas simulações
   print("Diferença nos somatórios de prêmios das duas simulações", diferenca_premios = total_premios_otimo - total_premios_distinta)



   
