import math
import numpy as np  
import pygame

class Body:
    G = 6.67428e-11
    TIMESTEP = 3600*24 # 1 day

    def __init__(self,name, position,velocity, radius, color, mass):
        self.name = name
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.x, self.y = self.position
        self.x_vel, self.y_vel = self.velocity
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0


    def draw(self, win, WIDTH, HEIGHT, FONT, SCALE):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        
        if not self.sun:
            distance_text = FONT.render(f"{self.name}:{round(self.distance_to_sun/1000, 1)}km", 1, (255, 255, 255))
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
            
    def attraction(self, other):
        r = np.linalg.norm(self.position - other.position)
        if other.sun:
            self.distance_to_sun = r
        force_vector = self.mass *self.G  * other.mass / r**3 * (other.position - self.position)
        return force_vector

    def update_position(self, planets):
        total_f = np.zeros_like(self.position)
        for planet in planets:
            if self == planet:
                continue

            f = self.attraction(planet)
            total_f += f
        self.velocity += total_f / self.mass * self.TIMESTEP
        self.position += self.velocity * self.TIMESTEP

        self.x_vel, self.y_vel = self.velocity
        self.x, self.y = self.position

        self.orbit.append((self.x, self.y))
        # total_fx = total_fy = 0
        # for planet in planets:
        #     if self == planet:
        #         continue

        #     fx, fy = self.attraction(planet)
        #     total_fx += fx
        #     total_fy += fy

        # self.x_vel += total_fx / self.mass * self.TIMESTEP
        # self.y_vel += total_fy / self.mass * self.TIMESTEP

        # self.x += self.x_vel * self.TIMESTEP
        # self.y += self.y_vel * self.TIMESTEP
        # # TODO: vectorize this operation
        # self.position = numpy.array([self.x, self.y])
        # self.orbit.append((self.x, self.y))