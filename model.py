import utils
from random import *

class Drone :
    def __init__(self, swarm, lat, long, area, speed, direction) :
        self.swarm = swarm
        self.lat = lat
        self.long = long
        self.area = area
        self.speed = speed
        self.direction = direction 

class Swarm :
    def __init__(self, number, lat, long, area, speed, direction):
        self.drones = []
        self.number = number
        self.lat = lat
        self.long = long
        self.area = area
        self.speed = speed
        self.direction = direction
    
    def random_position(self) :
        delta_lat = round(uniform(0.0, 0.15) - 0.1, 7) 
        delta_long = round(uniform(0.0, 0.3) - 0.1, 7) 

        return (self.lat + delta_lat, self.long + delta_long)
    
    def create_drones(self) :
        for i in range(self.number) :
            (la, lo) = self.random_position()
            drone = Drone(self, la, lo, self.area, self.speed, self.direction)
            self.drones.append(drone)

    
class SwarmList :
    def __init__(self) :
        self.swarm_list = []
        
    def add(self, swarm) :
        self.swarm_list.append(swarm)
