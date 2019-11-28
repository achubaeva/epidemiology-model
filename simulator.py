from cell import Cell
from map_class import Map
   
    
recovery_time = 1 # Recovery for cell time in days.
virality = 0.7 # Higher number conveys higher chance of becoming infected.
days = 5 # ays passed after first infection.                                                 
          
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


for i in range(days):
    m.time_step(recovery_time, virality)



