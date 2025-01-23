import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius)
        pygame.draw.circle(screen, "black", self.position, self.radius - 2)

    def update(self, dt, screen):
        self.position = self.wrap_position(self.position + self.velocity * dt, screen)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        rotation_change = random.uniform(20, 50)
        direction_a = self.velocity.rotate(rotation_change)
        direction_b = self.velocity.rotate(-rotation_change)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = direction_a
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = direction_b
