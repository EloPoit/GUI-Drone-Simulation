import model, view, controller

if __name__ == "__main__":
    swarm = model.Swarm(35, "52.516268 13.377695", 45, 25, "NE")
    app_view = view.View()
    controller = controller.SwarmController(swarm, app_view)
    self.root.mainloop()    