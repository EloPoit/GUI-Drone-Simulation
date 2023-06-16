from tkinter import *
import tkintermapview
from tkinter import ttk
import tkinter as tk

class MapView() :
    def __init__(self, root) :
        self.root = root

        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(self.root, width=1920, height=1080, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        
        # address you want to print first
        self.map_widget.set_position(48.860381, 2.338594)


class SwarmView(tk.Tk) : 
    def __init__(self, root) :
        self.root = root


    def print_swarm(self, map_view, position) :
        pos = position.split()
        print(float(pos[0]))
        print(map_view.map_widget)
        map_view.map_widget.set_polygon([(float(pos[0]), float(pos[1]))],
                                        fill_color="red",
                                        outline_color="red",
                                        border_width=35,
                                        command=self.swarm_click)
        print("cest fait")


    def swarm_click(self, polygon):
        print(f"polygon clicked - text: {polygon.name}")
           

    def left_click_event(self) :
        self.on_click(self, self.view)


    def print_info(self, number, position, area, speed, direction) :
        status_window = Frame(self.root, width=300, height=210, bg='grey')
        status_window.place(x=0, y=810)

        status_text = Label(status_window, text="Status", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        status_text.place(x=0, y=0) 

        number = Label(status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        number.place(x=0, y=35) 

        number_value = Label(status_window, text=str(number), bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        number_value.place(x=70, y=35) 

        position = Label(status_window, text="Position", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        position.place(x=0, y=65) 

        position_value = Label(status_window, text=position, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        position_value.place(x=70, y=65) 

        area = Label(status_window, text="Area", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        area.place(x=0, y=95) 

        area_value = Label(status_window, text=area, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        area_value.place(x=70, y=95) 

        speed = Label(status_window, text="Speed", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        speed.place(x=0, y=125) 

        speed_value = Label(status_window, text=speed, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        speed_value.place(x=70, y=125) 

        direction = Label(status_window, text="Direction", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        direction.place(x=0, y=155) 

        direction_value = Label(status_window, text=direction, bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        direction_value.place(x=70, y=155) 



class StatusView : 
    def __init__(self, root) :
        self.root = root



class View(tk.Tk) :
    def __init__(self):
        super().__init__()
        #self.root = Tk()

        # create tkinter window
        #self.geometry(f"{1920}x{1080}")

        # create the maps
        self.map_view = MapView(self)
        print("MapView")
        self.swarm_view = SwarmView(self)
        print("SwarmView")

        
