from tkinter import *
import tkintermapview
import customtkinter
import folium
import pandas as pd
from IPython.display import display

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

canvas = Canvas()

canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "white",width = 2)
canvas.pack()

#root.mainloop()
