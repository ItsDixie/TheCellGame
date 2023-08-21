
class cell:
    CELLS = {}
    ROWS = 0
    COLS = 0
    DEQUEUE = []

    def __init__(self, energy, pos, direction):
        self.energy = energy
        self.pos = pos
        #self.brain = perceptron
        self.dir = direction # от 1 до 8, клетки вокруг бота
        
    
    def update_constants(self, alive_cells, rows, cols, dequeue):
        self.CELLS = alive_cells
        self.ROWS = rows
        self.COLS = cols
        self.DEQUEUE = dequeue

    def insert_brain(self, perceptron):
        self.brain = perceptron

    def think(self):
        target = self.looking(False)
        simmilar = self.looking(True)
        inputs = [self.energy, target, simmilar, self.dir]
        output = self.brain.feedforward(inputs)
        self.folow_your_brain(output)
        # [1, 0, 0, 0, 0] - пример
        #  индекс 0 - движение по направлению, индекс 1 - сменить направление по часовой стрелке (вперед-диагональ-направо)
        #  индекс 2 - фотосинтезировать энергию, индекс 3 - размножение, индекс 4 - кушать клетку по направлению
    def get_inputs(self):
        target = self.looking(False)
        simmilar = self.looking(True)
        inputs = [self.energy, target, simmilar, self.dir]
        return inputs

    def folow_your_brain(self, instruction):
        if(bool(instruction[0])):
            self.move()
        elif(bool(instruction[1])):
            self.rotate()
        elif(bool(instruction[2])):
            self.photosintez()
        elif(bool(instruction[3])):
            self.multiply()
        elif(bool(instruction[4])):
            self.eat()
            
    def calc_move(self, x, y):
        if(self.dir == 0.125):
            ox,oy = x,y+1
        if(self.dir == 0.25):
            ox,oy = x+1,y+1
        if(self.dir == 0.375):
            ox,oy = x+1,y
        if(self.dir == 0.5):
            ox,oy = x+1,y-1
        if(self.dir == 0.625):
            ox,oy = x,y-1
        if(self.dir == 0.75):
            ox,oy = x-1,y-1
        if(self.dir == 0.875):
            ox,oy = x-1,y
        if(self.dir == 1.0):
            ox,oy = x-1,y+1

        return ox,oy
    def looking(self, looking_for_simmilar): # 0 если пустая клетка, 0,5 если край карты, 1 если с ботом
        x,y = self.pos

        ox, oy = self.calc_move(x, y)

        if(ox > self.ROWS):
            ox = self.ROWS
            return 0.5
        elif(ox < 0):
            ox = 0
            return 0.5
        
        if(oy > self.COLS):
            oy = self.COLS
            return 0.5
        elif(oy < 0):
            oy = 0
            return 0.5
        
        if((ox,oy) in self.CELLS):
            if(looking_for_simmilar):
                return int(any(cell.brain == self.brain for cell in self.CELLS.values()))
        else:
            return 0
        
    def move(self):
        x,y = self.pos
        ox, oy = self.calc_move(x, y)

        if(ox > self.ROWS):
            ox = self.ROWS
        elif(ox < 0):
            ox = 0
        
        if(oy > self.COLS):
            oy = self.COLS
        elif(oy < 0):
            oy = 0
            
        return ox, oy

    def rotate(self):
        if(self.dir != 1.0):
            self.dir += 0.125
        else:
            self.dir = 0.125
    def multiply(self):
        x,y = self.pos
        if(self.energy >= 10):
            self.energy -= 10
            ox, oy = self.calc_move(x, y)
            return [ox, oy, self.brain] # позиция для новой клетки
    def eat(self):
        pass
    def photosintez(self):
        pass

    def update_dict(self):
        self.DEQUEUE.pop(1)
        self.DEQUEUE.append(self.CELLS)
        