import pygame, pytmx



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


MAP_COLLISION_LAYER = 1


background = GRAY


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



class Game(object):
    def __init__(self):
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(fileName = #TODO"Assetts/level1.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]
        
				self.player = Player(x = 200, y = 100)
        self.player.currentLevel = self.currentLevel