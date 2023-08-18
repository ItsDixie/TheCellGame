
class cell:
    def __init__(self, hp, energy, pos, direction, perceptron):
        self.hp = hp
        self.energy = energy
        self.pos = pos
        self.brain = perceptron
        self.dir = direction
    
    def think(self):
        inputs = [self.hp, ]
        self.brain.feedforward(inputs)
    
    def looking(self):
        pass

    def move(self):
        pass
    def rotate(self):
        pass
    def multiply(self):
        pass
    def eat(self):
        pass
    def photosintez(self):
        pass
        