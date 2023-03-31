""" Drawing Squares """

import pygame
from pygame.locals import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)



background = GRAY


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


running = True


start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []
points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            print(event)            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start, size)
            rect_list.append(rect)
            drawing = False
            print(event)
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size= end[0] - start [0], end[1] - start[1] #or end[0] - start [0], end[-1] - start[-1]

            print(event)
        screen.fill(GRAY)
        for rect in rect_list:
            pygame.draw.rect(screen, RED, rect, 3)
        pygame.draw.rect(screen, BLUE, (start, size), 1
				)
        pygame.display.update()

pygame.quit()