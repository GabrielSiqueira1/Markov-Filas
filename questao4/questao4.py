# Questao4 - Trabalho de OTM2
#
# FELIPE MARTINS LEMOS DE MORAIS - 20193001045
# GABRIEL SIQUEIRA SILVA -20203008814
# FERNANDO GARAMVÖLGYI MAFRA VEIZAGA - 20203001902
#
# Descrição do codigo: 
# O código implementa funções para analisar sistemas de filas usando os modelos MM1 e MMS. O modelo MM1 é para uma única fila, 
# enquanto o modelo MMS é para várias filas. A função tabela gera uma tabela com várias métricas para diferentes configurações 
# de servidores (s). Os parâmetros incluem taxa de chegada (lambd) e taxa de atendimento (mi). As métricas incluem probabilidades,
# números esperados de clientes na fila e no sistema, tempos de espera, e probabilidades de tempo de espera na fila ser maior que 
# zero, um, dois e cinco. O resultado é impresso em uma tabela formatada.

import numpy as np
import math

def mm1(lambd, mi, s):
    
    # Formulas descritas no slide 34 de filas
    rho = lambd/mi # fator de utilização para s = 1
    p0 = 1 - rho # probabilidade de ter 0 clientes no sistema de filas
    pn = lambda n: (1 - rho)*rho**n # cálculo de probabilidade para qualquer n, lambda faz com que pn seja uma função que recebe n como parâmetro
    l = lambd/(mi - lambd) # número esperado de clientes na fila
    lq = l * (lambd/mi) # comprimento esperado da fila
    w = 1 / (mi - lambd) # tempo de espera no sistema
    wq = rho / (mi - lambd) # tempo de espera na fila
    pwq_gt_t = lambda t: rho*np.exp(-mi*(1-rho)*t) # P(Wq > t) = rho*np.exp(-mi*(1-rho)*t)
    
    return s, p0, pn(1), pn(2), pn(5), pn(10), l, lq, w, wq, pwq_gt_t(0), pwq_gt_t(1), pwq_gt_t(2), pwq_gt_t(5)
    
def mms(lambd, mi, s):
    
    # Formulas descritas no slide 37 de filas
    rho = lambd/(s*mi)
    p0 = 1 / (sum([((lambd/mi) ** i) / math.factorial(i) for i in range(s)]) + (((lambd/mi) ** s) / (math.factorial(s) * (1/(1-rho)))))
    pn = lambda n: (lambd/mi)**n/math.factorial(n)*p0 if n <= s else (lambd/mi)**n/(math.factorial(s)*s**(n-s))*p0
    lq = (p0*(lambd/mi)**s*rho)/(math.factorial(s)*(1-rho)**2)
    wq = lq/lambd
    w = wq + 1/mi
    l = lq + (lambd/mi)
    pwq_eq_0 = sum([pn(i) for i in range(0, s)])
    pwq_gt_t = lambda t: (1 - pwq_eq_0)*np.exp(-s*mi*(1-rho)*t)
    
    return s, p0, pn(1), pn(2), pn(5), pn(10), l, lq, w, wq, pwq_gt_t(0), pwq_gt_t(1), pwq_gt_t(2), pwq_gt_t(5)

def tabela(lambd, mi):
    
    # Cabeçalho
    cblho = ["s", "   P0  ", "   P1  ", "   P2  ", "   P5  ", "  P10  ", "   L   ", "   Lq  ", "   W   ", "   Wq  ", "P(Wq>0)", "P(Wq>1)", "P(Wq>2)", "P(Wq>5)"]

    # Tracejado entre as palavras do cabeçalho
    divisor = "|".join(cblho)
    print(divisor)
    
    # Imprimindo a divisoria
    divisoria = "--------" * len(cblho)
    print(divisoria)   

    for s in range(1, 5):
        if s == 1:
            parametros = mm1(lambd, mi, s)
        else:
            parametros = mms(lambd, mi, s)
        
        conteudo = ""
        contador = 0
        for parametro in parametros:
            if contador == 0:
                conteudo += f"{parametro}|"
                contador+=1 
            else:
                conteudo += f"{parametro:.5f}|"
            
        print(conteudo)

if __name__ == "__main__":
    taxa_chegada = 0.56  
    taxa_atendimento = 0.88  

    tabela(taxa_chegada, taxa_atendimento)