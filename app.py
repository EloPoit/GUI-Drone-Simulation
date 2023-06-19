import model
import view
import controller
import tkinter as tk


class App(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.title('GUI Swarm Drone Simulation')
        self.geometry(f"{1920}x{1080}")
        self.swarm = model.Swarm(35, "52.516268 13.377695", 45, 25, "NE")

        self.view = view.AppView(self)

        self.controller = controller.SwarmController(self.swarm, self.view)

        self.view.set_controller(self.controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()    