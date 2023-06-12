from tkinter import *
import tkintermapview

class View :
    def __init__(self, root):
        # create tkinter window
        root.geometry(f"{1920}x{1080}")
        

        # create map widget
        map_widget = tkintermapview.TkinterMapView(root, width=1920, height=1080, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        # choose the address you want to print first
        map_widget.set_address("paris, france")

        test = Label(root, text="red", bg="red", fg="white")
        test.pack(padx=5, pady=15, side=LEFT)

        root.mainloop()

