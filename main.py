import controller
import model

if __name__ == "__main__":
    swarm = model.Swarm(35, "nord", 45, 25, "NE")
    controller = controller.Controller()
    controller.run()


#def main() :
#    drones = [model.Drone(0), model.Drone(1)]
#    swarm = model.Swarm(drones, len(drones), "47.2251659 -1.6264056", 50, 0, )