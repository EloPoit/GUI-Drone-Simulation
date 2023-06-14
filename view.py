from tkinter import *
import tkintermapview
import model


class View :

    def __init__(self, root, model):
        self.model = model
        self.root = root
        
        # create tkinter window
        root.geometry(f"{1920}x{1080}")


        # create map widget
        map_widget = tkintermapview.TkinterMapView(root, width=1920, height=1080, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

        # use classic google map
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        # choose the address you want to print first
        map_widget.set_position(48.860381, 2.338594)

        def polygon_click(polygon):
            print(f"polygon clicked - text: {polygon.name}")


        switzerland_marker = map_widget.set_address("Switzerland", marker=True, text="Switzerland")
        map_widget.set_zoom(8)

        polygon_1 = map_widget.set_polygon([(46.0732306, 6.0095215)],
                                        fill_color=None,
                                        outline_color="red",
                                        border_width=35,
                                        command=polygon_click,
                                        name="switzerland_polygon")

        # creer un champs pour position, area, direction...

        root.mainloop()


    def update_status(self) :
        status_window = Frame(self.root, width=300, height=210, bg='grey')
        status_window.place(x=0, y=810)

        status_text = Label(status_window, text="Status", bg="grey", anchor=W, font=("Arial", 16), fg="white", padx=5, pady=5)
        status_text.place(x=0, y=0) 

        number = Label(status_window, text="Number", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        number.place(x=0, y=35) 

        number_value = Label(status_window, text="0", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        number_value.place(x=70, y=35) 

        position = Label(status_window, text="Position", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        position.place(x=0, y=65) 

        position_value = Label(status_window, text="48.860381 2.338594", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        position_value.place(x=70, y=65) 

        area = Label(status_window, text="Area", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        area.place(x=0, y=95) 

        area_value = Label(status_window, text="45", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        area_value.place(x=70, y=95) 

        speed = Label(status_window, text="Speed", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        speed.place(x=0, y=125) 

        speed_value = Label(status_window, text="0", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        speed_value.place(x=70, y=125) 

        direction = Label(status_window, text="Direction", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        direction.place(x=0, y=155) 

        direction_value = Label(status_window, text="NE", bg="grey", anchor=W, font=("Arial", 12), fg="white", padx=5, pady=5)
        direction_value.place(x=70, y=155) 