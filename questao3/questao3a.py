import random

def simular(lambd, mi, s, T):
    fila_espera = []
    atendentes_ocupados = []
    clientes_aguardando = []
    clientes_totais = []
    
    for it in range(T):
        # Obedecendo o primeiro ponto, quando um valor aleatório entre 0 e 1 for menor que lambda, um novo cliente é colocado na fila de espera
        if random.uniform(0, 1) < lambd:
            fila_espera.append(it)

        # Obedecendo o segundo ponto, é necessário verificar os atendentes ociosos
        while len(atendentes_ocupados) != s and len(fila_espera):
            # A fila é uma estrutura de dados no estilo FIFO, o primeiro que entra é o primeiro a sair, dessa forma, pode-se usar o pop no primeiro item para retirar o primeiro indivíduo da fila
            cliente = fila_espera.pop(0)
            atendentes_ocupados.append(cliente) 
            
        # Ainda no segundo ponto, para cada atendente ocupado, se um valor aleatório entre 0 e 1 for menor que mi, então, considera-se atendido
        # O reversed é uma propriedade útil para listas que estão sendo alteradas dentro de um loop onde o loop depende dos seus funcionamento.
        for i in reversed(range(len(atendentes_ocupados))):
            if random.uniform(0, 1) < mi and atendentes_ocupados[i]:
                atendentes_ocupados.pop(i)
                
        # Vetores a serem retornados com os que aguardam atendimento e o total de clientes
        clientes_aguardando.append(len(fila_espera))
        clientes_totais.append(len(fila_espera)+len(atendentes_ocupados))
        
    return clientes_aguardando, clientes_totais

def exibir_resultados(clientes_aguardando, clientes_totais):
    
    # Cabeçalho
    cblho = ["Iteração", "Clientes aguardando", "Total de clientes"]

    # Tracejado entre as palavras do cabeçalho
    divisor = "|".join(cblho)
    print(divisor)
    
    # Imprimindo a divisoria
    divisoria = "--------------------" * len(cblho)
    print(divisoria) 
    
    linha = ""
    for i in range(len(clientes_aguardando)):
        linha += f"    {i+1}   |         {clientes_aguardando[i]}         |             {clientes_totais[i]}   \n"
            
    print(linha)

if __name__ == "__main__":
    # Utilizando um exemplo da letra b
    lambd = 0.3 # taxa de chegada
    mi = 0.25 # taxa de atendimento
    s = 2 # número de atendentes
    T = 1000 # tempo de simulação
    
    clientes_aguardando, clientes_totais = simular(lambd, mi, s, T)
    
    exibir_resultados(clientes_aguardando, clientes_totais)
    