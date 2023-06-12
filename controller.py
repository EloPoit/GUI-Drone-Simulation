from tkinter import *
import model, view, utils

class update_number(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, observable):
        self.view.

class update_position(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, observable):
        return super().action(observable)

class update_area(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, observable):
        return super().action(observable)

class update_speed(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, observable):
        return super().action(observable)

class update_direction(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, observable):
        return super().action(observable)


class Controller :
    def __init__(self):
        self.root = Tk()
        self.model = model.Swarm(35, "sud", 45, 24, "NE")
        self.view = view.View(self.root)


    def run(self):
        self.root.title("GUI Drones Simulation")
        self.root.deiconify()
        self.root.mainloop()