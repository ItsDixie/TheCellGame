
class cell:
    def __init__(self, energy, pos, direction, perceptron, alive_cells, rows, cols):
        self.energy = energy
        self.pos = pos
        self.brain = perceptron
        self.dir = direction # от 1 до 8, клетки вокруг бота

        self.cells = alive_cells
        self.rows = rows
        self.cols = cols
    
    def think(self):
        target = self.looking(False)
        simmilar = self.looking(True)
        inputs = [self.hp, target, self.dir, simmilar, self.dir]
        output = self.brain.feedforward(inputs)
        # [1, 0, 0, 0, 0] - пример
        #  индекс 0 - движение по направлению, индекс 1 - сменить направление по часовой стрелке (вперед-диагональ-направо)
        #  индекс 2 - фотосинтезировать энергию, индекс 3 - размножение, индекс 4 - кушать клетку по направлению
    def looking(self, looking_for_simmilar): # 0 если пустая клетка, 0,5 если край карты, 1 если с ботом
        x,y = self.pos
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
        if(self.dir == 1):
            ox,oy = x-1,y+1
        
        if(ox > self.rows):
            ox = self.rows
            return 0.5
        elif(ox < 0):
            ox = 0
            return 0.5
        
        if(oy > self.cols):
            oy = self.cols
            return 0.5
        elif(oy < 0):
            oy = 0
            return 0.5
        
        if((ox,oy) in self.cells):
            if(looking_for_simmilar):
                return int(any(cell.brain == self.brain for cell in self.cells.values()))
        else:
            return 0
        
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
        