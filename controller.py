from tkinter import *
import model, view, utils

"""class update_number(utils.Observer) :
    def __init__(self, view) :
        super()
        self.view = view

    def action(self, swarm):
        self.view.number.text = swarm.number
"""


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

class SwarmController :
    def __init__(self,model, view) :
        self.model = model
        self.view = view

        self.view.print_swarm(self.model.position)
        print("print_swarm")

        self.view.print_info(self, model.number, model.position, model.area, model.speed, model.direction)
        print("print_info")


    def on_click(self) :
        self.view.print_info(self, model.number, model.position, model.area, model.speed, model.direction)



"""
class Controller :
    def __init__(self, model, view):
        self.model = model
        self.view = view
"""