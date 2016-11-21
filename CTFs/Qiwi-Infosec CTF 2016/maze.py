#!/usr/bin/python2.7
class Cell:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.status = ' '
        self.value = ' '

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
class Maze:    

    def __init__(self):
        self.flag = ""
        self.maze_x_size = 50
        self.maze_y_size = 50
        self.create_maze()
        self.solve(0, 0)

    def create_maze(self):

        self.maze = [[Cell() for x in range(self.maze_x_size)] for y in range(self.maze_y_size)]
        
        file = open("maze.csv", "r")

        for line in file:
            currentline = line.split(",")

            number = currentline[0]
            x = int(currentline[1])
            y = int(currentline[2])
            status = currentline[3]
            value = currentline[4][:-2]
            
            if status == 'gate':
                self.maze[y][x].set_status('.') 
            elif status == 'wall':
                self.maze[y][x].set_status('#')

            self.maze[y][x].set_value(value)
        
        self.maze[0][0].set_status('S')
        self.maze[self.maze_x_size-1][self.maze_y_size-1].set_status('E')
        
    def show_matrix(self):
        for i in range(self.maze_x_size):
            for j in range(self.maze_y_size):
                print self.maze[i][j].get_status(),
            print

    def solve(self,x,y):
       
        if self.maze[y][x].get_status() == 'E':
            self.flag += self.maze[y][x].get_value()
            print 'found at %d,%d' % (x, y)
            return True
        elif self.maze[y][x].get_status() == '#':
            print 'wall at %d,%d' % (x, y)
            return False
        elif self.maze[y][x].get_status() == 'V':
            print 'visited at %d,%d' % (x, y)
            return False
 
        print 'visiting %d,%d' % (x, y)

        # mark coordinate visited
        self.maze[y][x].set_status('V')        
        
        self.flag += self.maze[y][x].get_value()

        # recursive case
        if ((x < len(self.maze)-1 and self.solve(x+1, y)) or
                (y > 0 and self.solve(x, y -1)) or
                (x > 0 and self.solve(x-1, y)) or
                (y < len(self.maze)-1 and self.solve(x, y+1))):
            return True

        self.flag = self.flag[:-1]
        self.maze[y][x].set_status('.')
        return False

    def show_flag(self):
        print 'The flag is : ' +  self.flag

maze = Maze()
maze.show_matrix()
maze.show_flag()
