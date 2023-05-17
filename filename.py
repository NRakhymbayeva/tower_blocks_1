import sys
import pygame
import random as rn
from const_var import *
from utils import display_message
try:
    with open('highscore.txt', 'r') as f:
        high_score = int(f.read())
except FileNotFoundError:
    high_score = '0'
#initialize game
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tower Blocks")
background = pygame.image.load('./images/bk2.jpg')
background = pygame.transform.scale(background, WINDOW_SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def display_message(text, font_size, position):
    font = pygame.font.SysFont(None, font_size)
    text_obj = font.render(text, True, RED)
    screen.blit(text_obj, position)

#start the game
while True:
    screen.blit(background, (0, 0))

    #save the gihest score
    if score > high_score:
        high_score = score

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and not game_over: # and (prev_block_x is not None or not first_block):
                dropping = True

    if game_over:
        if score > high_score:
            with open('highscore.txt', 'w') as f:
                f.write(str(score))
            high_score = score

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # reset the game
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        block_x = rn.randint(0, WINDOW_WIDTH - block_width)
                        block_y = WINDOW_HEIGHT // 4.5
                        blocks = []
                        score = 0
                        prev_block_x = None
                        prev_block_y = WINDOW_HEIGHT
                        stacked = False
                        move_direction = 1
                        dropping = False
                        first_block = False
                        block_fall_count = 0
                        game_over = False
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()
            screen.blit(background, (0, 0))
            display_message("You lose!", 60, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2))
            display_message("Score: " + str(score), 40, (WINDOW_WIDTH // 2 - 30, WINDOW_HEIGHT // 2 + 40))
            display_message("Play again? (Y/N)", 40, (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 + 80))
            pygame.display.update()

    # move like a pendulum
    if not dropping:
        block_x += move_direction * block_speed
        if block_x <= 0:
            move_direction = 1
        elif block_x >= WINDOW_WIDTH - block_width:
            move_direction = -1

    if dropping: #or first_block:
        block_y += block_speed
        curr_block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
        collision = False
        # check for collisions
        for block in blocks:
            block_rect = pygame.Rect(block[0], block[1], block_width, block_height)
            if curr_block_rect.colliderect(block_rect):
                collision = True
                break

        if (block_y + block_height >= WINDOW_HEIGHT and not first_block) or collision:
            if prev_block_x is not None and \
                    not(prev_block_x - block_width * 0.3 <= block_x <= prev_block_x + block_width * 0.7):
                game_over = True
            else:
                blocks.append((block_x, block_y))
                prev_block_y = block_y
                prev_block_x = block_x
                block_x = rn.randint(max(0, int(prev_block_x - block_width * 0.2)),
                                     min(int(prev_block_x + block_width * 1.2), WINDOW_WIDTH - block_width))
                block_y = WINDOW_HEIGHT // 4.5
                score += 10
                dropping = False
                first_block = True
        elif block_y + block_height > WINDOW_HEIGHT and not collision and first_block: # and (prev_block_x is not None and not(prev_block_x <=block_x < prev_block_x + block_width)):
            block_fall_count += 1
            if block_fall_count >= 3:
                game_over = True
            else:
                block_x = rn.randint(0, WINDOW_WIDTH - block_width)
                block_y = WINDOW_HEIGHT // 4.5
                dropping = False

    #draw block and the score
    for block in blocks:
        screen.blit(block_image, block)
    screen.blit(block_image, (block_x, block_y))
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, [10, 10])
    high_score_text = font.render("Highest Score: " + str(high_score), True, RED)
    screen.blit(high_score_text, [10, 50])
    # update the dislpay
    pygame.display.update()

    #limit the frame rate
    clock.tick(60)