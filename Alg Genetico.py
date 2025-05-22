# Importa a biblioteca random para gerar números aleatórios
import random

# Função que calcula o fitness de um indivíduo x (nesse caso, f(x) = x^2)
def fitness(x):
    return x**2

# Função que cria um indivíduo aleatório (um número inteiro entre 0 e 31)
def create_individual():
    return random.randint(0, 31)

# Função que cria uma população de indivíduos
# size: tamanho da população
def create_population(size):
    return [create_individual() for _ in range(size)]

# Função que seleciona dois pais para reprodução com base no fitness
# population: lista de indivíduos
# fitness_values: lista de valores de fitness correspondentes
def select_parents(population, fitness_values):
    total_fitness = sum(fitness_values)  # Soma total dos valores de fitness
    selection_probs = [f/total_fitness for f in fitness_values]  # Probabilidade de seleção de cada indivíduo
    parents = random.choices(population, weights=selection_probs, k=2)  # Seleciona 2 pais com base nas probabilidades
    return parents

# Função que realiza o crossover (recombinação) entre dois pais para gerar dois filhos
# parent1, parent2: pais selecionados
def crossover(parent1, parent2):
    point = random.randint(1, 4)  # Escolhe um ponto de corte aleatório entre 1 e 4
    # Gera o primeiro filho combinando partes dos pais
    child1 = (parent1 & (0b11111 << point)) | (parent2 & (0b11111 >> (5 - point)))
    # Gera o segundo filho combinando partes dos pais
    child2 = (parent2 & (0b11111 << point)) | (parent1 & (0b11111 >> (5 - point)))
    return child1, child2

# Função que aplica mutação em um indivíduo
# individual: indivíduo a ser mutado
def mutate(individual):
    if random.random() < 0.1:  # 10% de chance de mutação
        bit = random.randint(0, 4)  # Escolhe um bit aleatório para mutar (0 a 4)
        individual ^= 1 << bit  # Inverte o bit selecionado usando operação XOR
    return individual

# Função principal que executa o Algoritmo Genético
def genetic_algorithm():
    population = create_population(4)  # Cria uma população inicial de 4 indivíduos
    for generation in range(10):  # Itera por 10 gerações
        fitness_values = [fitness(ind) for ind in population]  # Calcula o fitness de cada indivíduo
        new_population = []  # Lista para armazenar a nova geração
        for _ in range(2):  # Gera 2 filhos por geração
            parent1, parent2 = select_parents(population, fitness_values)  # Seleciona dois pais
            child1, child2 = crossover(parent1, parent2)  # Realiza o crossover para gerar dois filhos
            child1 = mutate(child1)  # Aplica mutação no primeiro filho
            child2 = mutate(child2)  # Aplica mutação no segundo filho
            new_population.extend([child1, child2])  # Adiciona os filhos à nova população
        population = new_population  # Substitui a população antiga pela nova
        print(f"Geração {generation}: {population}")  # Exibe a população atual
    return max(population, key=fitness)  # Retorna o indivíduo com maior fitness

# Executa o algoritmo e imprime a melhor solução encontrada
best_solution = genetic_algorithm()
print(f"Melhor solução encontrada: {best_solution}")