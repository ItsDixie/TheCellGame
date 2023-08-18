import numpy as np
import threading
def run():
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
            fitness = 1 # переделать под прогноз получаемой энергии и траты хп. Энергия растет при поедании и фотосинтезе. Хп падает при поедании кем-то другим
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
            best_perceptron = max(population, key=lambda p: self.evaluate_fitness(p, input_data, ))
            return best_perceptron

    # Пример входных данных и целевого вывода
    num_inputs = 5
    num_hidden_layers = 6
    num_neurons_per_layer = 5
    num_outputs = 5

    population_size = 50
    num_generations = 100
    mutation_rate = 0.1
    inputs = [0.8, 0.2, 0.4, 0.6, 0.1] # переделать под состояние клетки
    # индекс 0 - текущая энергия, индекс 1 - что видит клетка, 
    # индекс 2 - клетка на которую повернута, родственик? (0 - нет, 1 - да) индекс 3 -  направление клетки (ход по 0.125, 0 - значит на месте 
    # индекс 4 - высота клетки 



    # Создание и выполнение генетического алгоритма
    ga = GeneticAlgorithm(population_size, num_generations, mutation_rate, num_inputs, num_hidden_layers, num_neurons_per_layer, num_outputs)
    best_perceptron = ga.evolve(inputs)

    # Получение и вывод лучшего перцептрона 
    output = best_perceptron.feedforward(inputs)
    
    # [1, 0, 0, 0, 0] - пример
    #  индекс 0 - движение по направлению, индекс 1 - сменить направление по часовой стрелке (вперед-диагональ-направо)
    #  индекс 2 - фотосинтезировать энергию, индекс 3 - размножение, индекс 4 - кушать клетку по направлению