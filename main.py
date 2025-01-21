import pygame
from player import Player
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
    player = Player(startX, startY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)


if __name__ == "__main__":
    main()
