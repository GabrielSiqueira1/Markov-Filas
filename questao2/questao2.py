import numpy as np

def simulate_markov_chain(transition_matrix, initial_state, max_transitions):
    current_state = initial_state
    transitions = 0

    while transitions < max_transitions:
        # Gere uma transição para o próximo estado com base na matriz de transição
        next_state = np.random.choice(len(transition_matrix), p=transition_matrix[current_state])

        # Se atingir um estado absorvente (0 ou 4), retorne esse estado
        if next_state == 0 or next_state == 4:
            return next_state

        current_state = next_state
        transitions += 1

    # Se não atingir um estado absorvente em max_transitions, retorne -1
    return -1

def estimate_absorption_probabilities(transition_matrix, initial_state, max_transitions, num_simulations):
    absorption_counts = {0: 0, 4: 0}

    for _ in range(num_simulations):
        final_state = simulate_markov_chain(transition_matrix, initial_state, max_transitions)
        
        # Atualize as contagens com base no estado absorvente atingido
        if final_state != -1:
            absorption_counts[final_state] += 1

    # Calcule as probabilidades estimadas
    absorption_probabilities = {state: count / num_simulations for state, count in absorption_counts.items()}
    return absorption_probabilities

if __name__ == "__main__":
    # Defina a matriz de transição e outros parâmetros
    transition_matrix = np.array([
        [1, 0, 0, 0, 0],
        [2/3, 0, 1/3, 0, 0],
        [0, 2/3, 0, 1/3, 0],
        [0, 0, 2/3, 0, 1/3],
        [0, 0, 0, 0, 1]
    ])
    initial_state = 1  # Alteração para iniciar no estado 1
    max_transitions = 100
    num_simulations = 1000

    # Estime as probabilidades de absorção
    absorption_probabilities = estimate_absorption_probabilities(
        transition_matrix, initial_state, max_transitions, num_simulations
    )

    # Imprima os resultados
    print("Probabilidade estimada de absorção no estado 0:", absorption_probabilities[0])
    print("Probabilidade estimada de absorção no estado 4:", absorption_probabilities[4])