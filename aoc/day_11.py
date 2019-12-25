import numpy as np
from computer import Computer

class Robot():
    def __init__(self, dimx, dimy, start_color=0):
        self.map = np.zeros((dimx, dimy))
        self.x, self.y = dimx//2, dimy//2 
        self.map[self.x][self.y] = start_color
        self.painted = set()
        self.angle = 0
        self.directions = {'UP': (0,1), 'DOWN': (0,-1), 'RIGHT':(1,0), 'LEFT':(-1,0)}

    def turn(self, direction):
        if direction == 0:
            self.angle += -90
        else:
            assert direction == 1
            self.angle += 90

    def move(self):
        if self.angle%360 == 0:
            dx, dy = self.directions['DOWN']
        elif self.angle%360 == 90:
            dx, dy = self.directions['RIGHT']
        elif self.angle%360 == 180:
            dx, dy = self.directions['UP']
        else:
            assert self.angle%360 == 270
            dx, dy = self.directions['LEFT']
        self.x += dx
        self.y += dy

    def paint(self, color):
        self.map[self.x][self.y] = (1 if color == 1 else 0)
        self.painted.add((self.x, self.y))

    def make_move(self, color, direction):
        self.paint(color)
        self.turn(direction)
        self.move()

    def get_position(self):
        return self.map[self.x][self.y]

    def print_map(self):
        for m in self.map.transpose():
            t = [str(int(x)) for x in list(m)]
            print(''.join(t).replace('0',"█").replace('1', ' '))

    def get_painted_num(self):
         print(len(self.painted))

if __name__ == '__main__':
    program = [int(x) for x in open('data/day_11.csv', 'r').read().split(',')]

    ### PART 1 ###
    c = Computer(program)
    r = Robot(101, 101)

    while c.state:
        pin = r.get_position()
        col = c.compute([pin])
        pos = c.compute([])
        r.make_move(col, pos)
    
    r.get_painted_num()

    ### PART 2 ###
    c = Computer(program)
    r = Robot(101, 101, start_color=1)

    while c.state:
        pin = r.get_position()
        col = c.compute([pin])
        pos = c.compute([])
        r.make_move(col, pos)
    
    r.print_map()
