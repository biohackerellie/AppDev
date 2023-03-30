import pygame
import random



# define colors 

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set Screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("poop mah goop")


#load assetts

bg = GRAY

# TODO bg = pygame.image.load("background.jpg").convert()
player_img = pygame.image.load("randompy/logo.png").convert_alpha()

#game variables
player_x = 50
player_y = 400
player_speed = 5
is_jump = False
jump_count = 10
level = 1

#Game Loop

running = True
while running:
    # Handle Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					is_jump = True
		
		#Update game state
		if is_jump:
			if jump_count >= -10:
				player_y -= (jump_count * abs(jump_count)) * 0.5
				jump_count -= 1
			else:
				is_jump = False
				jump_count = 10
		
		#Draw the game
		screen.fill(bg)
		screen.blit(player_img, (player_x, player_y))
		pygame.display.flip()