from tkinter import *
import tkintermapview
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os

class AppView() :
    def __init__(self, root) :
        self.root = root
        self.controller = None

        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(self.root, width=1920, height=1080, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        
        # address you want to print first
        self.map_widget.set_position(52.516268, 13.377695)

        #Status Menu
        self.status_menu()

        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        drone_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "drone-camera.png")).resize((60, 60)))
        swarm_marker = self.map_widget.set_marker(52.516268, 13.377695, icon=drone_image, command=self.swarm_clicked)

    def set_controller(self, controller) :
        self.controller = controller

    def swarm_clicked(self, marker) :
        self.controller.get_info()

    def print_info(self, number, position, area, speed, direction) :
        self.number_value.configure(text = str(number))

        self.position_value.configure(text = position)

        self.area_value.configure(text = area)

        self.speed_value.configure(text = speed)

        self.direction_value.configure(text = direction)


    def status_menu(self) : 
        self.status_window = Frame(self.root, width=300, height=210, bg='grey')
        self.status_window.place(x=0, y=810)

        self.status_text = Label(self.status_window, text="Status", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        self.status_text.place(x=0, y=0) 

        self.number = Label(self.status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.number.place(x=0, y=35) 

        self.number_value = Label(self.status_window, text="", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.number_value.place(x=70, y=35) 

        self.position = Label(self.status_window, text="Position", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.position.place(x=0, y=65) 

        self.position_value = Label(self.status_window, text="", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.position_value.place(x=70, y=65) 

        self.area = Label(self.status_window, text="Area", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.area.place(x=0, y=95) 

        self.area_value = Label(self.status_window, text="", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.area_value.place(x=70, y=95) 

        self.speed = Label(self.status_window, text="Speed", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.speed.place(x=0, y=125) 

        self.speed_value = Label(self.status_window, text="", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.speed_value.place(x=70, y=125) 

        self.direction = Label(self.status_window, text="Direction", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.direction.place(x=0, y=155) 

        self.direction_value = Label(self.status_window, text="", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        self.direction_value.place(x=70, y=155) 




class SwarmView() : 
    def __init__(self, map_widget, app_view) :
        self.map_widget = map_widget
        self.app_view = app_view
        
    def print_swarm(self, map_view, position) :
        pos = position.split()
        
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        drone_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "drone-camera.png")).resize((60, 60)))
        swarm_marker = self.map_widget.set_marker(float(pos[0]), float(pos[1]), icon=drone_image)

        print("cest fait")


    def print_info(self, number, position, area, speed, direction) :
        self.app_view.number_value.configure(text = str(number))

        self.app_view.position_value.configure(text = position)

        """area_value = Label(status_window, text=area, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)

        speed_value = Label(status_window, text=speed, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)

        direction_value = Label(status_window, text=direction, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)"""




"""class View() :
    def __init__(self):
        
        #self.root = Tk()

        # create tkinter window
        #self.geometry(f"{1920}x{1080}")

        # create the maps
        self.app_view = AppView(self)
        print("AppView")
        self.swarm_view = SwarmView(self)
        print("SwarmView")"""

        
