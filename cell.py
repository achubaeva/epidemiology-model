#!/usr/bin/env python3
import random
import functions as fn


class Cell(object):
    def __init__(self,x, y):
        self.x = x
        self.y = y 
        
        # Can be "S" (susceptible), "R" (resistant = dead), or "I" (infected).
        self.state = "S" 
        self.time_infected = 0 
        self.recovery_time = 0     
        self.virality = 0         
        
    def infect(self):
        self.state = "I"
        self.time_infected += 1
    
    def process(self, adjacent_cells, recovery_time, virality):
        
        if self.time_infected == recovery_time:
            self.state = "S"
            self.time_infected = 0
        
        # If cell is infected, check if resistent or dies; then infected adjecent cells based on virality
        if self.state == "I":
            if random.random() <= fn.pdeath(self.time_infected, 3, 1):
                self.state = "R"
            for i in adjacent_cells:   
                if (i != None) and i.state == "S":
                    if random.random() <= virality:
                        i.infect()    
        else:
            pass