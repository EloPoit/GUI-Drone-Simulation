from tkinter import *
import tkintermapview
import customtkinter
import folium
import pandas as pd
from IPython.display import display
from PIL import Image, ImageTk
import os
from tkinter import ttk

root = Tk()
root.geometry(f"{1920}x{1080}")

btn = Button(root, text="Click Me", bg="black", fg="red")
btn.pack()

status_window = Frame(root, width=300, height=180, bg='grey')
status_window.place(x=0, y=837)

status_text = Label(status_window, text="Status", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
status_text.place(x=0, y=0) 

number = Label(status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
number.place(x=0, y=50) 

# create map widget
"""map_widget = tkintermapview.TkinterMapView(root, width=1920, height=1080, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

# use classic google map
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
 """       
pos = ["52.516268", "13.377695"]
"""
map_widget.set_polygon([(float(pos[0]), float(pos[1]))],
                                fill_color="red",
                                outline_color="red",
                                border_width=35,
                                )"""

def left_click_event(coordinates_tuple) :
    print("Left click event with coordinates:", coordinates_tuple)

#map_widget.add_left_click_map_command(left_click_event)

def clicked(marker) :
    print("bonjour")


frame_button = Frame(root)
#frame_button.pack()
vlist = ["By elements - Points", "By elements - Surfaces", "By groups"]
view_button = ttk.Combobox(frame_button, values = vlist)
view_button.set("Choose a view")


"""canvas = Canvas()

canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "white",width = 2)
canvas.pack()
"""
root.mainloop()
