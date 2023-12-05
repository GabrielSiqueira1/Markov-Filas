import numpy as np
import random

def simular_cadeia_markov(P, estado_inicial, numero_transicoes):
    estado_atual = estado_inicial 
    t = 0

    while t < numero_transicoes:
        chute = random.uniform(0,1)
        
        # Roleta
        # O procedimento de roletagem se baseia nas probabilidades da matriz e o quanto um chute é maior que o valor daquela probabilidade. Além disso, por ser representado por um gráfico de setor, as porcentagens da roleta são somadas, ou seja, se para o estado 1 temos 20% e para o estado 2 20%, na roleta só alcançaremos o estado 2 se ficarmos entre 20% e 40%, dessa forma, se o chute for em 35%, o estado irá para 2.
        probabilidades=P[estado_atual]
        somatorio=probabilidades[0]
        
        i = 1
        while i < len(P):
            if chute > somatorio: # se o chute não estiver na região do setor
                somatorio += probabilidades[i] 
                if chute < somatorio: # se estiver na região do setor
                    estado_atual = i
                    i = len(P) # break no looping
            else: # caso o chute inicial já esteja dentro do setor
                estado_atual = i-1
                i = len(P)
                
            i += 1
        t += 1
    return estado_atual

def estimar(P, estado_inicial, numero_transicoes, numero_simulacoes):
    dicio_estados_quantidade = {chave: 0 for chave in range(5)} # Cria um dicionário com os 5 estados possíveis

    for _ in range(numero_simulacoes):
        estado_final = simular_cadeia_markov(P, estado_inicial, numero_transicoes)
        
        dicio_estados_quantidade[estado_final] += 1
        
    probabilidades = {estado: contador/numero_simulacoes for estado, contador in dicio_estados_quantidade.items()} # Verificação quantitativa da porcentagem de estados finais com relação ao número de simulações 
    return probabilidades

if __name__ == "__main__":
    P = np.array([
        [1, 0, 0, 0, 0],
        [2/3, 0, 1/3, 0, 0],
        [0, 2/3, 0, 1/3, 0],
        [0, 0, 2/3, 0, 1/3],
        [0, 0, 0, 0, 1]
    ])
    
    # Parâmetros da questão
    estado_inicial = 1
    numero_simulacoes = 1000
    numero_transicoes = 100
    
    probabilidades = estimar(P, estado_inicial, numero_transicoes, numero_simulacoes)
    
    # Conforme o exercício, estime as probabilidades dos estados de absorção
    print("Probabilidade do estado absorvente 0:", probabilidades[0])
    print("Probabilidade do estado absorvente 4:", probabilidades[4])