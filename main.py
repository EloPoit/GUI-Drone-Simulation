import controller, view, model

def main() :
    print("bonjour")
    drones = [model.Drone(0), model.Drone(1)]
    swarm = model.Swarm(drones, len(drones), "47.2251659 -1.6264056", 50, 0, )