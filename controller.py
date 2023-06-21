from tkinter import *
import model, view, utils


class SwarmController :
    def __init__(self,model, view) :
        self.model = model
        self.view = view

        # Print the marker for all the swarms
        for swarm in self.model.swarm_list :
            self.view.place_marker(swarm.lat, swarm.long)

    

    def get_info(self, position) :
        (lat, long) = position
        
        for swarm in self.model.swarm_list :
            if lat == swarm.lat and long == swarm.long :
                self.view.print_info(swarm.number, swarm.lat, swarm.long, swarm.area, swarm.speed, swarm.direction)
        
