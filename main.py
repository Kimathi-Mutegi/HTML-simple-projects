import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
red = (255, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            run = False