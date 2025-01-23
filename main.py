import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    startX = SCREEN_WIDTH / 2
    startY = SCREEN_HEIGHT / 2

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (drawable, updatable)
    player = Player(startX, startY)

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt, screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(120) / 1000


if __name__ == "__main__":
    main()
