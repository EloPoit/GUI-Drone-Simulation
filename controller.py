from tkinter import *
import model, view, utils


class SwarmController :
    def __init__(self,model, view) :
        self.model = model
        self.view = view

        """ self.view.swarm_view.print_swarm(self.view.map_view, self.model.position)
        print("print_swarm")

        print(model.number)
        self.view.swarm_view.print_info(model.number, model.position, model.area, model.speed, model.direction)
        print("print_info")"""

    def get_info(self) :
        """self.model.number = number
        self.model.position = position
        self.model.area = area
        self.model.speed = speed
        self.model.direction = direction"""

        self.view.print_info(self.model.number, self.model.position, self.model.area, self.model.speed, self.model.direction)
