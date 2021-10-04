import pygame
import time
import random 

snake_speed = 15

window_x = 500
window_y = 500

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('snsnsaaake')
pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

