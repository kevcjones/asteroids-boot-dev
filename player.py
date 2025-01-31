import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_ACCELERATION,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.next_shot = PLAYER_SHOOT_COOLDOWN
        self.accelerating = False

    # in the player class
    def body(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def booster(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius*2
        b = self.position - forward * (self.radius + 1) - right/2
        c = self.position - forward * (self.radius + 1) + right/2
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.body(), 2)
        if self.accelerating > 0:
            pygame.draw.polygon(screen, "yellow", self.booster(), 3)

    def update(self, dt, screen):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.accelerate()
            self.accelerating = True
        else:
            self.accelerating = False
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.move(dt, screen)

    def accelerate(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, screen):
        self.position = self.wrap_position(self.position + self.velocity * dt, screen)

    def shoot(self, dt):
        self.next_shot -= dt
        if self.next_shot < 0:
            self.next_shot = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            )
