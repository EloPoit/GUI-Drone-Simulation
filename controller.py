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
                if self.view.map_widget.zoom < 9 :
                    # Print the marker for all the swarms
                    for swarm in self.model.swarm_list :
                        marker = self.view.place_marker(swarm.lat, swarm.long)
                        marker.data = swarm
                else :
                    # Print the marker for all the drones of the different swarms
                    for swarm in self.model.swarm_list :
                        for drone in swarm.drones :
                            marker = self.view.place_marker(drone.lat, drone.long)
                            marker.data = drone
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

    def get_info(self, marker) :
        (lat, long) = marker.position
        data = marker.data
        
        if type(data) == model.Swarm :
            self.view.print_info(data.number, data.lat, data.long, data.area, data.speed, data.direction)
        else :
            self.view.print_info("-", data.lat, data.long, data.area, data.speed, data.direction)
            
"""for swarm in self.model.swarm_list :
    for drone in swarm.drones :
        if lat == drone.lat and long == drone.long :
            self.view.print_info(drone.number, drone.lat, drone.long, drone.area, drone.speed, drone.direction)

"""