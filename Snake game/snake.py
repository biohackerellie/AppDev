import pygame
import random
import pygame.mixer

# TODO add music files later

# TODO pygame.mixer.init() 


# TODO bg_music = pygame.mixer.music.load('bg.wav')
# TODO eating_sound = pygame.mixer.Sound('eat.wav')
# TODO game_over_sound = pygame.mixer.Sound('over.wav')

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

disp_width = 600
disp_height = 400

dis = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Snake Game')

last_food_time = pygame.time.get_ticks()
timeout = 30000

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 25

font_style = pygame.font.SysFont("Hack", 25)
score_font = pygame.font.SysFont("Hack", 35)

def Your_score(score):
	value = score_font.render("Your Score: " + str(score), True, yellow)
	dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis_width, dis_height = dis.get_size()
	mesg_width, mesg_height = mesg.get_size()
	x = (dis_width - mesg_width) /2
	y = (dis_height - mesg_height) /2
	if mesg_width > disp_width:
		words = msg.split()
		lines = []
		line = ""
		for word in words:
			if font_style.render(line+ word, True, color).get_width() < disp_width:
				line += word + " "
			else:
				lines.append(line)
				line = word + " "
		lines.append(line)
		for i, line in enumerate(lines):
			mesg = font_style.render(line, True, color)
			line_x = (dis_width - mesg.get_width()) / 2
			dis.blit(mesg, [line_x, y + i * mesg.get_height()])
	else:
		dis.blit(mesg, [x,y])

def gameLoop():
	# TODO pygame.mixer.music.play(-1)
	message("Use the arrow keys to move the snake. Don't suck", white)
	pygame.display.update()
	last_food_time = pygame.time.get_ticks()
	game_over = False
	game_close = False

	x1 = disp_width / 2
	y1 = disp_height / 2

	x1_change = 0 
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0

	while not game_over:
		
		while game_close == True:
			dis.fill(blue)
			message("You fucking suck! Press C to try again or Q to quit like a little bitch", red)
			Your_score(Length_of_snake - 1)
			# TODO game_over_sound.play()
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameLoop()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:					
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:	
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_w or event.key == pygame.K_UP:	
					y1_change = -snake_block
					x1_change = 0
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:	
					y1_change = snake_block
					x1_change = 0
		
		if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)
		pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > Length_of_snake:
			del snake_List[0]
		
		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True
		
		our_snake(snake_block, snake_List)
		Your_score(Length_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody: 
			foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
			Length_of_snake += 1
			# TODO eating_sound.play()
			last_food_time = pygame.time.get_ticks()
		
		if pygame.time.get_ticks() - last_food_time > timeout:
			game_close = True
		
		clock.tick(snake_speed)
		
	pygame.quit()
	quit()
	
gameLoop()