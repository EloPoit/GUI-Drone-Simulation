from random import *
from PIL import Image, ImageTk
import os

class Drone :
    def __init__(self, swarm, lat, long, area, speed, direction) :
        self.swarm = swarm
        self.lat = lat
        self.long = long
        self.area = area
        self.speed = speed
        self.direction = direction 
        
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

        self.classic = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone.png")).resize((50, 50)))
        self.white = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone_blanc.png")).resize((50, 50)))

class Swarm :
    def __init__(self, number, lat, long, area, speed, direction):
        self.drones = []
        self.position_list = []
        self.number = number
        self.lat = lat
        self.long = long
        self.area = area
        self.speed = speed
        self.direction = direction
        
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        
        self.classic = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone.png")).resize((60, 60)))
        self.white = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone_blanc.png")).resize((60, 60)))
        
    
    def random_position(self) :
        delta_lat = uniform(0.0, 0.15) - 0.1
        delta_long = uniform(0.0, 0.3) - 0.1 
        return (round(self.lat + delta_lat, 6), round(self.long + delta_long, 6))
    
    def create_drones(self) :
        for i in range(self.number) :
            (la, lo) = self.random_position()
            self.position_list.append((la, lo))
            drone = Drone(self, la, lo, self.area, self.speed, self.direction)
            self.drones.append(drone)

    
class SwarmList :
    def __init__(self) :
        self.swarm_list = []
        
    def add(self, swarm) :
        self.swarm_list.append(swarm)
