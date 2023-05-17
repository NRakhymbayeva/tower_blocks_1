import pygame
from const_var import RED

def display_message(screen, text, font_size, position):
    font = pygame.font.SysFont(None, font_size)
    text_obj = font.render(text, True, RED)
    screen.blit(text_obj, position)
