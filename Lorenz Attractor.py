# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:34:00 2022

@author: satvi
"""

import pygame
import os
import colorsys
import math

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1920, 1080
size = (width, height)
white, black = (200,200,200),(0,0,0)
pygame.init()
pygame.display.set_caption("Lorenz attractor")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

sigma = 10
rho = 28
beta = 8/3
x,y,z = 0.01,0,0
scale = 15
run = True
while run:
    #screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time = 0.01
    dx = (sigma * (y-x))* time
    dy = (x * (rho - z) - y) * time
    dz = (x * y - beta * z) * time

    x = x + dx
    y = dy + y
    z = dz + z

    pygame.draw.circle(screen, white, (int(x*scale) + width//2 , int(y*scale) + height//2), 1)

    pygame.display.update()

pygame.quit()