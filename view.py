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
        self.map_widget = tkintermapview.TkinterMapView(self.root, width=1920, height=1015, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        
        # address you want to print first
        self.map_widget.set_position(52.516268, 13.377695)

        # Status Menu
        self.status_menu()
        
        # View Status
        self.var = IntVar()
        self.view_menu()
        
        
        
        # Image of the drones
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.drone_classic = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone.png")).resize((60, 60)))
        self.drone_blanc = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "drone_blanc.png")).resize((60, 60)))


    def set_controller(self, controller) :
        self.controller = controller


    ## For the view by element ##

    def print_marker(self) :
        self.map_widget.delete_all_marker() 
        self.controller.get_marker_position()

    def place_marker(self, lat, long) :        
        self.map_widget.set_marker(lat, long, icon=self.drone_blanc, command=self.swarm_clicked)

    def swarm_clicked(self, marker) :
        # When the swarn is clicked, the icon change
        for m in self.map_widget.canvas_marker_list :
            if m.position == marker.position :
                marker.change_icon(self.drone_classic)       
            else :
                m.change_icon(self.drone_blanc)
        # Information from the swarm is retrieved
        self.controller.get_info(marker.position)

    def print_info(self, number, lat, long, area, speed, direction) :
        self.number_value.configure(text = number)

        self.lat_value.configure(text = lat)
        
        self.long_value.configure(text = long)

        self.area_value.configure(text = area)

        self.speed_value.configure(text = speed)

        self.direction_value.configure(text = direction)


    ## For the view by surface ##
    def print_surface(self) :
        self.map_widget.delete_all_marker() 
        print("surface")

    ## For the view by groups ##
    def print_groups(self) :
        self.map_widget.delete_all_marker()
        print("groups")


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
        self.view_window = Frame(self.root, width=300, height=230, bg='grey')
        self.view_window.grid(row = 0,column = 0, sticky=SE)

        self.view_text = Label(self.view_window, text="VIEW", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        self.view_text.place(x=0, y=0) 
        
        
        R1 = Radiobutton(self.view_window, text="By elements - Points", variable=self.var, value=1, padx=5, pady=5, 
                         background="grey", font=("Arial", 12), activebackground="grey", command = self.print_marker)
        R1.place(x=0, y=40) 
        
        R2 = Radiobutton(self.view_window, text="By elements - Surfaces", variable=self.var, value=2, padx=5, pady=5, 
                         background="grey", font=("Arial", 12), activebackground="grey", command=self.print_surface)
        R2.place(x=0, y=90)
        
        R3 = Radiobutton(self.view_window, text="By groups", variable=self.var, value=3, padx=5, pady=5, 
                         background="grey", font=("Arial", 12), activebackground="grey", command=self.print_groups)
        R3.place(x=0, y=140)


        
        

    """# Button to change view
    selected_month = tk.StringVar()
    vlist = ["By elements - Points", "By elements - Surfaces", "By groups"]
    month_cb = ttk.Combobox(root, textvariable=selected_month, values=vlist, background="grey", font="Arial 16 bold")
    month_cb.set("Choose a view")
    month_cb['state'] = 'readonly'
    month_cb.grid(row = 0, column = 0, sticky=SE, padx=10, pady=10)

    def callbackFunction(event) :
        country = event.widget.get()
        print(country)

    month_cb.bind("<<ComboboxSelected>>", callbackFunction)"""

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

        
