from tkinter import *
import model, view

class SwarmController :
    def __init__(self,model, view) :
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        
        self.view.view_menu()


    def get_marker_position(self, var) :
        if var == 1 :
            self.view.map_widget.delete_all_polygon()
            self.view.print_default()
            if self.view.map_widget.canvas_marker_list == [] :
                self.print_element_zoom()
        elif var == 2 :
            self.view.map_widget.delete_all_marker()
            self.view.print_default()
            if self.view.map_widget.canvas_polygon_list == [] :
                self.print_surface_zoom()
        else :
            self.view.map_widget.delete_all_marker()
            self.view.map_widget.delete_all_polygon()
            self.view.print_default()
            for swarm in self.model.swarm_list :
                self.view.print_groups()

    def get_info(self, marker) :
        print("get info")
        data = marker.data
        
        if type(data) == model.Swarm :
            self.view.print_info(data.number, data.lat, data.long, data.area, data.speed, data.direction)
        else :
            self.view.print_info("-", data.lat, data.long, data.area, data.speed, data.direction)
    
    def swarm_marker(self) :
        for swarm in self.model.swarm_list :
            marker = self.view.place_marker(swarm.lat, swarm.long, swarm.white)
            marker.data = swarm
     
    def drone_marker(self) :
        for swarm in self.model.swarm_list :
            for drone in swarm.drones :
                marker = self.view.place_marker(drone.lat, drone.long, drone.white)
                marker.data = drone
     
    def print_element_zoom(self) :
        if self.view.map_widget.zoom < 9 :
            # Print the marker for all the swarms
            self.swarm_marker()
        else :
            # Print the marker for all the drones of the different swarms
            self.drone_marker()
    
    def print_surface_zoom(self) :
        if self.view.map_widget.zoom < 9 :
            # Print the surface for all the swarms
            self.swarm_surface_less()
        else :
            # Print the surface for all the drones of the different swarms
            self.swarm_surface_more()

    def swarm_surface_more(self) :
        for swarm in self.model.swarm_list :
            polygon = self.view.print_surface(swarm.position_list, 5)
            polygon.data = swarm

    def swarm_surface_less(self) :
        for swarm in self.model.swarm_list :
            polygon = self.view.print_surface(swarm.position_list, 60)
            polygon.data = swarm
