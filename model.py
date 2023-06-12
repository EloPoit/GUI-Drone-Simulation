import utils

class Swarm(utils.Observable):
    def __init__(self, number, position, area, speed, direction):
        #self.drones = drones
        self.number = number
        self.position = position
        self.area = area
        self.speed = speed
        self.direction = direction
    
    def addDrone(self) :
        self.set_number(self.number + 1)

    def deleteDrone(self) :
        self.set_number(self.number - 1)

    def set_number(self, x) :
        if (self.number == x) :
            return
        
        self.number = x
        self.set_changed(self)
        self.notify_observers(self)



