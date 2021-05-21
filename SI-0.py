# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400,600))

#creating objects of game
player=pygame.Rect(200,500,30,30)


while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.draw.rect(screen,(23,100,100),player)
    
    pygame.display.update()
   

