from typing import *
from math import *
import pygame

pygame.init()
screenSize = pygame.display.get_desktop_sizes()[0]
screenFlags = pygame.FULLSCREEN
screen = pygame.display.set_mode((0, 0), screenFlags)
timer = pygame.time.Clock()
frameRate:Final = 60
width:Final = screen.get_width()
height:Final = screen.get_height()
