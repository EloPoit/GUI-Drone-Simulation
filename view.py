from tkinter import *
import tkintermapview
from tkinter import ttk
import tkinter as tk
import graham_hull

import sys

class AppView() :
    def __init__(self, root) :
        self.root = root
        self.controller = None

        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(self.root, width=1920, height=1015, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        
        # address you want to print first
        self.map_widget.set_position(52.516268, 13.377695)

        # Status Menu
        self.status_menu()
        
        # View Menu
        # called in the controller

        # Zoom
        self.last_zoom = 16
        
        self.map_widget.button_zoom_in.add_command(command=self.zoom_in)
        self.map_widget.button_zoom_out.add_command(command=self.zoom_out)
     
        self.map_widget.canvas.bind("<MouseWheel>", self.mouse_zoom)

        # Image of the drones
       

    def set_controller(self, controller) :
        self.controller = controller

    def get_view(self) :
        self.controller.get_marker_position(self.var.get())


    ## For the view by element ##

    def place_marker(self, lat, long, icon_size) :        
        marker = self.map_widget.set_marker(lat, long, icon=icon_size, command=self.marker_clicked)
        return marker
    

    def marker_clicked(self, marker) :
        # When the swarm is clicked, the icon changes
        for m in self.map_widget.canvas_marker_list :
            if m.position == marker.position :
                marker.change_icon(marker.data.classic)       
            else :
                m.change_icon(marker.data.white)
        # Information from the swarm is retrieved
        self.controller.get_info(marker)


    def print_info(self, number, lat, long, area, speed, direction) :
        self.number_value.configure(text = number)

        self.lat_value.configure(text = lat)
        
        self.long_value.configure(text = long)

        self.area_value.configure(text = area)

        self.speed_value.configure(text = speed)

        self.direction_value.configure(text = direction)
        
    def print_default(self) :
        self.number_value.configure(text = "-")

        self.lat_value.configure(text = "-")
        
        self.long_value.configure(text = "-")

        self.area_value.configure(text = "-")

        self.speed_value.configure(text = "-")

        self.direction_value.configure(text = "-")


    ## For the view by surface ##

    def print_surface(self, position_list, border) :
        extern_points = graham_hull.convex_hull_graham(position_list)
        print(extern_points)
        polygon = self.map_widget.set_polygon(extern_points,
                                outline_color="red",
                                border_width=border,
                                fill_color = "blue",
                                command=self.controller.get_info,
                                )
        return polygon

    ## For the view by groups ##
    def print_groups(self) :
        print("groups")


    ### ZOOM ###
    def zoom_in(self) :
        self.last_zoom = self.map_widget.last_zoom

        self.map_widget.set_zoom(self.map_widget.zoom + 1, relative_pointer_x=0.5, relative_pointer_y=0.5)
        
        if self.last_zoom <= 9 and self.map_widget.zoom > 9 :
            if self.var.get() == 1 :
                #passer du swarm au drones
                self.map_widget.delete_all_marker()
                self.print_default()
                self.controller.drone_marker()
            elif self.var.get() == 2 :
                self.map_widget.delete_all_polygon()
                self.print_default()
                self.controller.swarm_surface_more()
                
    def zoom_out(self) :
        self.last_zoom = self.map_widget.last_zoom

        self.map_widget.set_zoom(self.map_widget.zoom - 1, relative_pointer_x=0.5, relative_pointer_y=0.5)

        if self.last_zoom >= 9 and self.map_widget.zoom < 9 :
            if self.var.get() == 1 :
                #passer des drones au swarm
                self.map_widget.delete_all_marker()
                self.print_default()
                self.controller.swarm_marker()
            elif self.var.get() == 2 :
                self.map_widget.delete_all_polygon()
                self.print_default()
                self.controller.swarm_surface_less()
        
    def mouse_zoom(self, event):
        relative_mouse_x = event.x / self.map_widget.width  # mouse pointer position on map (x=[0..1], y=[0..1])
        relative_mouse_y = event.y / self.map_widget.height

        if sys.platform == "darwin":
            new_zoom = self.zoom + event.delta * 0.1
        elif sys.platform.startswith("win"):
            new_zoom = self.map_widget.zoom + event.delta * 0.01
        elif event.num == 4:
            new_zoom = self.map_widget.zoom + 1
        elif event.num == 5:
            new_zoom = self.map_widget.zoom - 1
        else:
            new_zoom = self.map_widget.zoom + event.delta * 0.1

        self.last_zoom = self.map_widget.last_zoom

        self.map_widget.set_zoom(new_zoom, relative_pointer_x=relative_mouse_x, relative_pointer_y=relative_mouse_y)


        if self.last_zoom <= 9 and self.map_widget.zoom > 9 :
            if self.var.get() == 1 :
                #passer du swarm au drones
                self.map_widget.delete_all_marker()
                self.print_default()
                self.controller.drone_marker()
            elif self.var.get() == 2 :
                self.map_widget.delete_all_polygon()
                self.print_default()
                self.controller.swarm_surface_more()
        elif self.last_zoom > 9 and self.map_widget.zoom < 9 :
            if self.var.get() == 1 :    
                #passer des drones au swarm
                self.map_widget.delete_all_marker()
                self.print_default()
                self.controller.swarm_marker()
            elif self.var.get() == 2 :
                self.map_widget.delete_all_polygon()
                self.print_default()
                self.controller.swarm_surface_less() 


    ### MENUS ###
    def status_menu(self) : 
        self.status_window = Frame(self.root, width=300, height=230, bg='grey')
        self.status_window.grid(row = 0,column = 0, sticky=SW)
                
        self.status_text = Label(self.status_window, text="STATUS", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        self.status_text.place(x=0, y=0) 

        self.number = Label(self.status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.number.place(x=0, y=35) 

        self.number_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.number_value.place(x=80, y=35) 

        self.lat = Label(self.status_window, text="Latitude", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.lat.place(x=0, y=65) 

        self.lat_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.lat_value.place(x=80, y=65) 
        
        self.long = Label(self.status_window, text="Longitude", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.long.place(x=0, y=95) 

        self.long_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.long_value.place(x=80, y=95) 

        self.area = Label(self.status_window, text="Area", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.area.place(x=0, y=125) 

        self.area_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.area_value.place(x=80, y=125) 

        self.speed = Label(self.status_window, text="Speed", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.speed.place(x=0, y=155) 

        self.speed_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.speed_value.place(x=80, y=155) 

        self.direction = Label(self.status_window, text="Direction", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.direction.place(x=0, y=185) 

        self.direction_value = Label(self.status_window, text="-", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.direction_value.place(x=80, y=185) 

    def view_menu(self) : 
        self.var = IntVar()
        self.view_window = Frame(self.root, width=300, height=230, bg='grey')
        self.view_window.grid(row = 0,column = 0, sticky=SE)

        self.view_text = Label(self.view_window, text="VIEW", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        self.view_text.place(x=0, y=0) 
        
        self.R1 = Radiobutton(self.view_window, text="By elements - Points", variable=self.var, value=1, padx=5, pady=5, foreground="white", background="grey", selectcolor="grey",
                         font=("Arial", 12), activeforeground="black", activebackground="grey", command = self.get_view)
        self.R1.place(x=0, y=40) 
        
        self.R2 = Radiobutton(self.view_window, text="By elements - Surfaces", variable=self.var, value=2, padx=5, pady=5, foreground="white", background="grey", selectcolor="grey",
                          font=("Arial", 12), activeforeground="black", activebackground="grey", command=self.get_view)
        self.R2.place(x=0, y=90)
        
        self.R3 = Radiobutton(self.view_window, text="By groups", variable=self.var, value=3, padx=5, pady=5, foreground="white", background="grey", selectcolor="grey",
                         font=("Arial", 12), activeforeground="black", activebackground="grey", command=self.get_view)
        self.R3.place(x=0, y=140)






        
