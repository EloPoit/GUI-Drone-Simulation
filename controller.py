from tkinter import *
import model, view, utils

class update_number(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, swarm):
        self.view.number.text = swarm.number

class on_click :
    def __init__(self, view) :
        super()
        self.view = view
    
    def action(self, swarm) :
        self.view.update_status(self)

"""class add_marker :
    def __init__(self, view):
        super()
        self.view = view

    def action(self, swarm)

"""
'''
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
'''

class Controller :
    def __init__(self, model):
        self.root = Tk()
        self.model = model
        self.view = view.View(self.root)

        self.model.add_observers(on_click(self, self.view))

        self.view.number

    def left_click_event(self) :
        on_click(self, self.view)


    def run(self):
        self.root.title("GUI Drones Simulation")
        self.root.deiconify()
        self.root.mainloop()