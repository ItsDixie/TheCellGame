import numpy as np
import cells
from random import randint, choice
def run(q):
    size_list = q[0]
    ROWS, COLS = size_list[0]-1, size_list[1]-1
    q.pop()
    print(q)
    class Perceptron:
        def __init__(self, num_inputs, num_hidden_layers, num_neurons_per_layer, num_outputs):
            self.weights = []
            self.biases = []
            self.num_layers = 2 + num_hidden_layers
            
            layer_sizes = [num_inputs] + [num_neurons_per_layer] * num_hidden_layers + [num_outputs]
            for i in range(1, self.num_layers):
                num_connections = layer_sizes[i] * layer_sizes[i-1]
                self.weights.append(np.random.randn(num_connections).reshape(layer_sizes[i], layer_sizes[i-1]))
                self.biases.append(np.random.randn(layer_sizes[i]))

        def activation_function(self, x):
            return 1 if x >= 0 else 0
        
        def feedforward(self, inputs):
            for i in range(self.num_layers - 1):
                weighted_sum = np.dot(self.weights[i], inputs) + self.biases[i]
                inputs = [self.activation_function(x) for x in weighted_sum]
            return inputs
    # Генетический алгоритм для оптимизации перцептрона
    class GeneticAlgorithm:
        def __init__(self, population_size, num_generations, mutation_rate, num_inputs, num_hidden_layers, num_neurons_per_layer, num_outputs):
            self.population_size = population_size
            self.num_generations = num_generations
            self.mutation_rate = mutation_rate
            self.num_inputs = num_inputs
            self.num_hidden_layers = num_hidden_layers
            self.num_neurons_per_layer = num_neurons_per_layer
            self.num_outputs = num_outputs
        
        def initialize_population(self):
            population = []
            for _ in range(self.population_size):
                perceptron = Perceptron(self.num_inputs, self.num_hidden_layers, self.num_neurons_per_layer, self.num_outputs)
                population.append(perceptron)
            return population

        
        def evaluate_fitness(self, perceptron, input_data):
            output = perceptron.feedforward(input_data)
            fitness = 1
            if(output[3] == 1):
                fitness *= 20
             # переделать под прогноз получаемой энергии и траты хп. Энергия растет при поедании и фотосинтезе. Хп падает при поедании кем-то другим
            return fitness
        
        def select_parents(self, population, input_data):
            parents = []
            for _ in range(2):  # Выбираем двух родителей
                fitness_scores = [self.evaluate_fitness(p, input_data, ) for p in population]
                probabilities = fitness_scores / np.sum(fitness_scores)
                parent_index = np.random.choice(len(population), p=probabilities)
                parents.append(population[parent_index])
            return parents
        
        def crossover(self, parent1, parent2):
            child = Perceptron(self.num_inputs, self.num_hidden_layers, self.num_neurons_per_layer, self.num_outputs)
            for i in range(len(child.weights)):
                crossover_point = np.random.randint(0, len(child.weights[i]))
                child.weights[i][:crossover_point] = parent1.weights[i][:crossover_point]
                child.weights[i][crossover_point:] = parent2.weights[i][crossover_point:]
                
                crossover_point = np.random.randint(0, len(child.biases[i]))
                child.biases[i][:crossover_point] = parent1.biases[i][:crossover_point]
                child.biases[i][crossover_point:] = parent2.biases[i][crossover_point:]
            return child
        
        def mutate(self, child):
            for i in range(len(child.weights)):
                if np.random.rand() < self.mutation_rate:
                    child.weights[i] += np.random.randn(*child.weights[i].shape)
                
                if np.random.rand() < self.mutation_rate:
                    child.biases[i] += np.random.randn(*child.biases[i].shape)
            return child
        
        def evolve(self, input_data, ):
            population = self.initialize_population()
            for generation in range(self.num_generations):
                new_population = []
                for _ in range(self.population_size // 2):
                    parent1, parent2 = self.select_parents(population, input_data, )
                    child = self.crossover(parent1, parent2)
                    child = self.mutate(child)
                    new_population.extend([parent1, parent2, child])
                population = new_population
            best_perceptron = max(population, key=lambda p: self.evaluate_fitness(p, input_data))
            return best_perceptron

    # Пример входных данных и целевого вывода
    num_inputs = 4
    num_hidden_layers = 2
    num_neurons_per_layer = 5
    num_outputs = 5

    population_size = 10
    num_generations = 5
    mutation_rate = 0.1 
    # индекс 0 - текущая энергия, индекс 1 - что видит клетка, 
    # индекс 2 - клетка на которую повернута, родственик? (0 - нет, 1 - да) индекс 3 -  направление клетки (ход по 0.125, 0 - значит на месте 
     

    base_energy = 1
    cells_amount = 100
    alive_cells = {}
    # Создание и выполнение генетического алгоритма
    ga = GeneticAlgorithm(population_size, num_generations, mutation_rate, num_inputs, num_hidden_layers, num_neurons_per_layer, num_outputs)
    
    def give_cells():
        q.append(alive_cells)
        
    
    for i in range(cells_amount):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        alive_cell = cells.cell(base_energy, (randint(0, ROWS), randint(0, COLS)), choice([0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]), color)
        alive_cell.update_constants(alive_cells, ROWS, COLS, q)
        inputs = alive_cell.get_inputs()
        best_perceptron = ga.evolve(inputs)
        alive_cell.insert_brain(best_perceptron)
        alive_cells[f"cell{i}"] = alive_cell
    give_cells()


