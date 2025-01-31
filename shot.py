import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, dt, screen):
        self.position = self.wrap_position(self.position + self.velocity * dt, screen)
