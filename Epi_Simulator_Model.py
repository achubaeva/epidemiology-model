# Anna Chubaeva ac3807


from matplotlib import pyplot as plt
from cell import Cell
   
    
recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in 
                  # each time step                                                  


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
            d[c].process(self.adjacent_cells(d[c].x, d[c].y), recovery_time, virality)
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



