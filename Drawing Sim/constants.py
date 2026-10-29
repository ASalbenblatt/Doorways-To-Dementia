from typing import *
from math import *
from random import *
import pygame

pygame.init()
screenFlags = pygame.FULLSCREEN
screen = pygame.display.set_mode((0, 0), screenFlags)
timer = pygame.time.Clock()
frameRate:Final = 60
width:Final = screen.get_width()
height:Final = screen.get_height()

lineColor:Final = [0, 0, 0]
lineThickness:Final = 3
distanceBetweenPoints:Final = 5

screenScaleFactor:Final = 2
