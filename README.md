# Algoritmo Genético em Python

Este projeto implementa um **algoritmo genético simples** para maximizar a função `f(x) = x²`, onde `x` é um número inteiro entre `0` e `31`. O objetivo é simular a evolução de uma população ao longo de várias gerações, utilizando operadores genéticos como **seleção**, **crossover** e **mutação**.

---

## 🔢 Representação dos Indivíduos

- Cada indivíduo é um número inteiro entre `0` e `31`, ou seja, representado por 5 bits.
- A aptidão (fitness) de um indivíduo é dada por `f(x) = x²`.

---

## ⚙️ Componentes do Algoritmo

### Funções principais:

- `create_individual()`: Gera um indivíduo aleatório.
- `create_population(size)`: Gera uma população inicial de tamanho `size`.
- `fitness(x)`: Função objetivo — calcula o valor de `x²`.
- `select_parents(population, fitness_values)`: Seleciona dois pais com base na roleta viciada (seleção proporcional ao fitness).
- `crossover(parent1, parent2)`: Realiza o cruzamento entre dois pais com ponto de corte aleatório.
- `mutate(individual)`: Aplica mutação com 10% de probabilidade invertendo um bit aleatório.
- `genetic_algorithm()`: Executa o algoritmo por 10 gerações com uma população de 4 indivíduos.

---

## 🧪 Execução

A cada geração:
- São selecionados dois pares de pais.
- São gerados dois filhos por par através de crossover e mutação.
- A nova geração substitui completamente a anterior.
- O processo se repete por 10 gerações.

---

## 🏁 Resultado

Ao final da execução, o programa imprime:
- Todas as populações geradas a cada geração.
- A **melhor solução** encontrada ao final (indivíduo com maior fitness).
