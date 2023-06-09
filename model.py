class Drone:
    def __init__(self, id) :
        self.id


class Swarm:
    def __init__(self, drones, number, position, area, speed, direction):
        self.drones = drones
        self.number = number
        self.position = position
        self.area = area
        self.speed = speed
        self.direction = direction
    
    def add(self, drone):
        self.drones.append(drone)
    
    def get(self, id) : 
        for drone in self.drones :
            if drone.id == id :
                return drone
            return None
        
    def get_all(self):
        return self.drones
