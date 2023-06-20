import utils


class Swarm():
    def __init__(self, number, lat, long, area, speed, direction):
        self.number = number
        self.lat = lat
        self.long = long
        self.area = area
        self.speed = speed
        self.direction = direction
    
    
class SwarmList :
    def __init__(self) :
        self.swarm_list = []
        
    def add(self, swarm) :
        self.swarm_list.append(swarm)



