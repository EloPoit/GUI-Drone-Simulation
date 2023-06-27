import model
import view
import controller
import tkinter as tk


class App(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.title('GUI Swarm Drone Simulation')
        self.geometry(f"{1920}x{1000}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.swarm_list = model.SwarmList()
        
        self.swarm_1 = model.Swarm(10, 52.516268, 13.377695, 45, 25, "NE")
        self.swarm_1.create_drones()
        
        
        """self.swarm_2 = model.Swarm(15, 46.548312, 3.287667, 30, 20, "SW")
        self.swarm_3 = model.Swarm(22, 35.548312, 15.287667, 36, 23, "S")

        self.swarm_list.add(self.swarm_1)
        self.swarm_list.add(self.swarm_2)
        self.swarm_list.add(self.swarm_3)"""
        
        self.swarm_list.add(self.swarm_1)
        
        self.view = view.AppView(self)

        self.controller = controller.SwarmController(self.swarm_list, self.view)

        #self.view.set_controller(self.controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()    