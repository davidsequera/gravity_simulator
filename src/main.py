import json
from Body import Body
from GravitationalSystem import GravitationalSystem
import pygame
import numpy


def createBodies(bodies_dict: dict):
    bodies = []
    for body in bodies_dict:
        new_body = Body(body['name'], numpy.array(body['position']),body['velocity'], body['radius'], body['color'], body['mass'])
        if 'sun' in body:
            new_body.sun = True
        bodies.append(new_body)
    return bodies

def main():
    # Import the gravitational system
    with open("./examples/three_suns.json", "r") as f:
        data = json.load(f)

    system = GravitationalSystem(data['name'], SCALE=data['scale'])
    print(system.name)
    print(system.SCALE)
    # Load the planets from the JSON file

    WHITE = (255, 255, 255)
    pygame.init()
    WIDTH, HEIGHT =  800, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planet Simulation")
    FONT = pygame.font.SysFont("comicsans", 16)

    planets = createBodies(data['bodies'])
    system.bodies = planets
    system.run(WIN, WIDTH, HEIGHT, FONT, WHITE)

if __name__ == "__main__":
    main()



