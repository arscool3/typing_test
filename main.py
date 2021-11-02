import pygame
import random

WIDTH = 1280
HEIGHT = 720
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

red_img = pygame.image.load("red.jpg")
red = pygame.transform.scale(red_img, (30, 30))
redrect = red.get_rect()


default_text = "Hello world. It's me, Arslan. Nice to meet you!"

font = pygame.font.SysFont('serif', 40)

text = font.render(default_text, True, BLACK)

index = 0

while running :
    clock.tick(FPS)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if pygame.KMOD_SHIFT & pygame.key.get_mods() :
                try:
                    if chr(event.key) == default_text[index].lower() :
                        index += 1
                        print("OK")
                        redrect.x += 16
                except :
                    pass
            else :
                try:
                    if chr(event.key) == default_text[index]:
                        index += 1
                        print("OK")
                        redrect.x += 16
                except :
                    pass
    redrect.y = 30
    screen.fill(WHITE)
    screen.blit(red, redrect)
    screen.blit(text, (0, 0))
    pygame.display.flip()