import pygame
import math
import sys


WIDTH, HEIGHT = 800, 800


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
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.zoom = 10
        self.counter = 0
        self.movement = pygame.math.Vector2()
        self.font = pygame.font.SysFont(None, 24)

    def draw(self):
        self.screen.fill((0, 0, 0))

        dict_ = {}
        for y in range(int(HEIGHT / self.zoom)):
            for x in range(int(WIDTH / self.zoom)):
                if is_prime(y * WIDTH + x):
                    dict_[(x, y)] = True

        for pos in dict_:
            # pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
            y = pos[1] + self.movement.y
            x = pos[0] + self.movement.x
            pygame.draw.rect(self.screen, (255, 255, 255), [x * self.zoom, y * self.zoom, self.zoom, self.zoom])
        self.counter += 0.01

        self.screen.blit(self.font.render(f"{self.movement}", True, (0, 255, 255)), (20, 20))

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if event.key == pygame.K_RIGHT:
                        self.movement.x += 1
                    if event.key == pygame.K_LEFT:
                        self.movement.x -= 1
                    if event.key == pygame.K_UP:
                        self.movement.y -= 1
                    if event.key == pygame.K_DOWN:
                        self.movement.y += 1

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
            pygame.display.set_caption(f"{self.clock.get_fps()}")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    App().run()
