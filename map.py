from tkinter import *
import tkintermapview
import customtkinter

# create tkinter window
root_tk = Tk()
root_tk.geometry(f"{1920}x{1080}")
root_tk.title("map_view_simple_example.py")


# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1920, height=1080, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

btn = Button(root_tk, text="Click Me", bg="black", fg="red")
btn.pack()

test = Label(root_tk, text="red", bg="red", fg="white")
test.pack(padx=5, pady=15, side=LEFT)



map_widget.set_address("nantes, france")

root_tk.mainloop()
