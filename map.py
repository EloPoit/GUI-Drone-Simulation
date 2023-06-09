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
from functools import *

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

def afficher() :
    print("Afficher")

map_widget.set_polygon([(52.516268, 13.377695)],
                        fill_color="red",
                        outline_color="red",
                        command=afficher,
                        border_width=12,
                    )


def left_click_event(coordinates_tuple) :
    print("Left click event with coordinates:", coordinates_tuple)

#map_widget.add_left_click_map_command(left_click_event)
    
def mouse(event) :
    print("Mouse event with coordinates:")
    
    
map_widget.canvas.bind("<Button-4>", mouse, add="+")

points = [(52.516268, 13.377695), (46.548312, 3.287667), (35.548312, 15.287667), 
          (12.494058, 3.434581), (55.585951, 15.271348), (52.585951, 40.271348)]

for p in points :
    map_widget.set_marker(p[0], p[1], text = p)
    

def convex_hull_graham(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm. 
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

print(convex_hull_graham(points))















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
