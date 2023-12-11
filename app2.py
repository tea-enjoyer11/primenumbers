import pygame
import numpy as np
import sys
from random import randrange


def random_color() -> tuple:
    return (randrange(0, 255), randrange(0, 255), randrange(0, 255))


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.WIDTH = self.HEIGHT = 1000
        self.HALF_WIDHT, self.HALF_HEIGTH = self.WIDTH // 2, self.HEIGHT // 2
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Müssen jeden Frame basierend auf einem zoom factor und den Pixel des Fensters erstellt werden.
        self.arr = []
        for y in range(self.HEIGHT // 4):
            row = []
            for x in range(self.WIDTH // 4):
                prime = is_prime(y * self.WIDTH + x)
                row.append([(x, y), prime])
            self.arr.append(row)

    def draw(self):
        scale = 4
        prime_color = (255, 255, 0)
        normal_color = (0, 0, 0)
        start_point = (self.HALF_WIDHT, self.HALF_HEIGTH)
        for row in self.arr:
            for col in row:
                # pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
                color = prime_color if col[1] else normal_color
                pygame.draw.rect(self.screen, color, [col[0][0] * scale, col[0][1] * scale, scale, scale])

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
            pygame.display.flip()
            pygame.display.set_caption(f"{self.clock.get_fps()}")
            self.clock.tick(60)
        self.exit()

    def exit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    App().run()
