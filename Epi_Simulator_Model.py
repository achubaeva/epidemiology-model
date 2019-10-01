# Anna Chubaeva ac3807

import random
from random import randint
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        # x and y and strings
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or "I" (infected)
        self.time_infected = 0               
        
    def infect(self):
        self.state = "I"
        self.time_infected += 1
    
    def process(self, adjacent_cells):
        
        if self.time_infected == recovery_time:
            self.state = "S"
            self.time_infected = 0
        if self.state == "I":
            if random.random() <= pdeath(self.time_infected, 3, 1):
                self.state = "R"
            for i in adjacent_cells:   
                if (i != None) and i.state == "S":
                    if random.random() <= virality:
                        i.infect()    
        else:
            pass

class Map(object):
 
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cells[(cell.x, cell.y)] = (cell)

    def display(self):      
        points = []
        image = []
        for x in range(self.width):
            for y in range(self.height):
                points.append((x,y))  
        # points is a list of all the pixel point coordinates in the 150x150 map
        d = self.cells
        for p in points:
            if p in d:
                for c in d:
                    if (c == p) and (d[c].state == "S"):
                        image.append((0.0, 1.0, 0.0))
                    if (c == p) and (d[c].state == "I"):
                        image.append((1.0, 0.0, 0.0))
                    if (c == p) and (d[c].state == "R"):
                        image.append((0.5, 0.5, 0.5))
            else:
                image.append((0.0, 0.0, 0.0))
        # if a coordinate in points is in the dictionary of cells, then it adds the tuple for green color
        # if not then it adds for black color
        pixels_of_image = []
        for i in range(self.width*self.height):
            if i%self.height == 0:
                pixels_of_image.append(image[i:i+self.height])     
        plt.imshow(pixels_of_image) 
        # this creates a list of 150 lists (the lists inside being the rows of length 150 pixel color tuples)
            
    def adjacent_cells(self, x,y):
        d = self.cells
        if (x, y + 1) in d:
            coor_up = d[(x, y+1)]
        else:
            coor_up = None
        if (x, y-1) in d:
            coor_down = d[(x, y-1)]
        else:
            coor_down = None
        if (x+1, y) in d:
            coor_right = d[(x+1, y)]
        else:
            coor_right = None
        if (x-1,y) in d:
            coor_left = d[(x-1, y)]
        else:
            coor_left = None
        return [coor_up, coor_down, coor_left, coor_right]
        # None for if the final coordinate is in water or off the map (i.e. not in the dictionary)
        
    def time_step(self):
        d = self.cells
        for c in d:
            d[c].process(self.adjacent_cells(d[c].x, d[c].y))
        self.display()
          
def read_map(filename):
    m = Map()
    file = open(filename, "r")
    for line in file:
        line = line.replace('\n', '')
        l = line.split(",")
        cell = Cell(int(l[0]), int(l[1]))
        m.add_cell(cell)
    return m

m = read_map("nyc_map.csv")
m.cells[(39, 82)].infect()


    
m.time_step()



