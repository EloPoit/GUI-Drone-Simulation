from tkinter import *
import tkintermapview
import customtkinter
import folium
import pandas as pd
from IPython.display import display
from PIL import Image, ImageTk
import os
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry(f"{1920}x{1080}")

btn = Button(root, text="Click Me", bg="black", fg="red")
#btn.pack()

status_window = Frame(root, width=300, height=180, bg='grey')
status_window.place(x=0, y=837)

status_text = Label(status_window, text="Status", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
status_text.place(x=0, y=0) 

number = Label(status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
number.place(x=0, y=50) 

# create map widget
map_widget = tkintermapview.TkinterMapView(root, width=1920, height=1080, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

# use classic google map
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
       
pos1 = ["52.516268", "13.377695"]
pos2 = ["46.548312", "3.287667"]
pos3 = ["46.548312", "3.287667"]

map_widget.set_polygon([(52.516268, 13.377695)],
                        fill_color="red",
                        outline_color="red",
                        border_width=12,
                    )


def left_click_event(coordinates_tuple) :
    print("Left click event with coordinates:", coordinates_tuple)

#map_widget.add_left_click_map_command(left_click_event)

def clicked(marker) :
    print("bonjour")



zoom = map_widget.zoom
print(zoom)


"""def print_var() :
    print(var.get())

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command = print_var)
R1.pack()

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command = print_var)
R2.pack()

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command = print_var)
R3.pack()"""

"""canvas = Canvas()

canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "white",width = 2)
canvas.pack()
"""
root.mainloop()
