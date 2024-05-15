import math
import pygame 
from Body import Body
from typing import List

class GravitationalSystem:
    AU = 149.6e6 * 1000

    def __init__(self, name = "System", G = 6.674 * 10**-11, SCALE = 250):
        self.name = name
        self.G = G
        self.SCALE = SCALE/ self.AU
        self.bodies: List[Body] = []

    def run(self, WIN, WIDTH, HEIGHT, FONT, WHITE):
        run = True
        clock = pygame.time.Clock()


        while run:
            clock.tick(60)
            WIN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for body in self.bodies:
                body.update_position(self.bodies)
                body.draw(WIN, WIDTH, HEIGHT, FONT, self.SCALE)

            pygame.display.update()

        pygame.quit()



    def add_planet(self, planet):
        self.bodies.append(planet)

    def update(self):
        for planet in self.bodies:
            planet.update_position(self.bodies)

    def draw(self, win):
        for planet in self.bodies:
            planet.draw(win)