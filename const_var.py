import pygame
import random as rn

#initialize game
pygame.init()

#set the window's parameters
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#define the block
block_width = 50
block_height = 50
block_size = (block_width, block_height)
block_speed = 5
block_image = pygame.image.load('./images/wall.png')
block_image = pygame.transform.scale(block_image, block_size)
block_x = rn.randint(0, WINDOW_WIDTH - block_width)
block_y = WINDOW_HEIGHT // 4.5
blocks = []
score = 0
prev_block_x = None
prev_block_y = WINDOW_HEIGHT
stacked = False
#1 for right and -1 for left
move_direction = 1
dropping = False
first_block = False
block_fall_count = 0
game_over = False
