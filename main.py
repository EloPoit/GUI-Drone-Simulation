import controller
import model

if __name__ == "__main__":
    swarm = model.Swarm(35, "nord", 45, 25, "NE")
    controller = controller.Controller(swarm)
    controller.run()