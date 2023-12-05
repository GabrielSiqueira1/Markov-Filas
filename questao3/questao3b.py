import random
import matplotlib.pyplot as plt

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
        # O reversed é uma propriedade útil para listas que estão sendo alteradas dentro de um loop onde o loop depende dos seu tamanho. Sem o reversed, a próxima posição que poderia sofrer pop não existiria
        for i in reversed(range(len(atendentes_ocupados))):
            if random.uniform(0, 1) < mi and atendentes_ocupados[i]:
                atendentes_ocupados.pop(i)
                
        # Vetores a serem retornados com os que aguardam atendimento e o total de clientes
        clientes_aguardando.append(len(fila_espera))
        clientes_totais.append(len(fila_espera)+len(atendentes_ocupados))
        
    return clientes_aguardando, clientes_totais

def exibir_resultados(clientes_aguardando, clientes_totais, save_path):
    plt.close()
    plt.figure(figsize=(10, 6))
    plt.plot(clientes_aguardando, label='Clientes aguardando')
    plt.plot(clientes_totais, label='Total de clientes')
    plt.xlabel('Iteração')
    plt.ylabel('Número de clientes')
    plt.title('Fila')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    print(f"Arquivo {save_path} gerado no diretório da questão")
        
# Função genérica para os diferentes sistemas propostos
def instancia(lambd, mi, s, T, i):
    clientes_aguardando, clientes_totais = simular(lambd, mi, s, T) 
    exibir_resultados(clientes_aguardando, clientes_totais, save_path=f'simulacao_ponto_{s}_vez_{i}.png')

if __name__ == "__main__":
    
    for i in range(0, 100):
        lambd = 0.3 # taxa de chegada
        mi = 0.25 # taxa de atendimento
        s = 1 # número de atendentes
        T = 1000 # tempo de simulação
        instancia(lambd, mi, s, T, i) 
    
    for i in range(0, 100):
        lambd = 0.3 # taxa de chegada
        mi = 0.25 # taxa de atendimento
        s = 2 # número de atendentes
        T = 1000 # tempo de simulação
        instancia(lambd, mi, s, T, i) 
    
    for i in range(0, 100):
        lambd = 0.3 # taxa de chegada
        mi = 0.20 # taxa de atendimento
        s = 3 # número de atendentes
        T = 1000 # tempo de simulação
        instancia(lambd, mi, s, T, i) 
    
    
    
    
    