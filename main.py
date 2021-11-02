import pygame
import random

WIDTH = 300
HEIGHT = 300
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("This is typing test")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

while running :
    clock.tick(FPS)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.

    screen.fill(WHITE)
    pygame.display.flip()