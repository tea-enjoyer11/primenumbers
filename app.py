import numpy as np
import pygame
import sys


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = [i for i in range(n + 1) if sieve[i]]
    return primes


def get_primes(start: int, end: int) -> list:
    if start < 2:
        start = 2

    primes = sieve_of_eratosthenes(end)
    return [p for p in primes if start <= p <= end]


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (rho, phi)


def pol2cart(rho, phi, size_factor=1):
    x = rho * np.cos(phi) / size_factor
    y = rho * np.sin(phi) / size_factor
    return [x, y]


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.WIDTH = self.HEIGHT = 800
        self.HALF_WIDHT, self.HALF_HEIGTH = self.WIDTH // 2, self.HEIGHT // 2
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.movement = pygame.math.Vector2()
        self.key_state = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False, pygame.K_1: False, pygame.K_2: False}
        self.size_factor = 200
        self.only_primes = False

        self.create_polar_system()

    def create_polar_system(self, amount=100000):
        primes = get_primes(1, amount)
        self.polar_system = {}
        for i in range(amount + 1):
            prime = False
            pos = (i, i)
            if i in primes:
                prime = True
            self.polar_system[pos] = prime

    def draw(self, only_primes=False):
        self.screen.fill((0, 0, 0))

        prime_color, normal_color = (255, 255, 0), (255, 255, 255)

        for polar_pos in self.polar_system:
            cartesian_pos = pol2cart(polar_pos[0], polar_pos[1], size_factor=self.size_factor)
            cartesian_pos[0] += self.HALF_WIDHT
            cartesian_pos[1] += self.HALF_HEIGTH

            if 0 <= cartesian_pos[0] <= self.WIDTH and 0 <= cartesian_pos[1] <= self.HEIGHT:
                if only_primes:
                    if self.polar_system[polar_pos]:
                        pygame.draw.circle(self.screen, (255, 255, 255), cartesian_pos, 1)
                else:
                    c = prime_color if self.polar_system[polar_pos] else normal_color
                    pygame.draw.circle(self.screen, c, cartesian_pos, 1)

    def run(self):
        run = True
        while run:
            self.movement.x = 0
            self.movement.y = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key in self.key_state:
                        self.key_state[event.key] = event.type == pygame.KEYDOWN
                    if event.key == pygame.K_3:
                        self.only_primes = not self.only_primes

            if self.key_state[pygame.K_w]:
                self.movement.y = -1
            if self.key_state[pygame.K_s]:
                self.movement.y = 1
            if self.key_state[pygame.K_a]:
                self.movement.x = -1
            if self.key_state[pygame.K_d]:
                self.movement.x = 1
            if self.key_state[pygame.K_1]:
                self.size_factor += 1
            if self.key_state[pygame.K_2]:
                self.size_factor = max(1, self.size_factor - 1)

            self.draw(only_primes=self.only_primes)

            pygame.display.flip()
            pygame.display.set_caption(f"{self.clock.get_fps()}")
            self.clock.tick(60)

        self.exit()

    def exit(self):
        pygame.quit()
        sys.exit()


App().run()
