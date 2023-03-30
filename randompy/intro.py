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




key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

print(key_dict)




background = GRAY


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                caption = 'background color = ' + str(background)
                pygame.display.set_caption(caption)
        screen.fill(background)
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

pygame.quit()