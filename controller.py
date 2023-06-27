from tkinter import *
import model, view, utils


class SwarmController :
    def __init__(self,model, view) :
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        
        self.view.view_menu()


    def get_marker_position(self, var) :
        if var == 1 :
            if self.view.map_widget.canvas_marker_list == [] :
                # Print the marker for all the swarms
                for drone in self.model.swarm_list[0].drones :
                    self.view.place_marker(drone.lat,drone.long)
        elif var == 2 :
            self.view.map_widget.delete_all_marker()
            self.view.print_default()
            for swarm in self.model.swarm_list :
                self.view.print_surface()
        else :
            self.view.map_widget.delete_all_marker()
            self.view.print_default()
            for swarm in self.model.swarm_list :
                self.view.print_groups()

    def get_info(self, position) :
        (lat, long) = position
        
        for swarm in self.model.swarm_list :
            if lat == swarm.lat and long == swarm.long :
                self.view.print_info(swarm.number, swarm.lat, swarm.long, swarm.area, swarm.speed, swarm.direction)
        
