#Building the Snake game in Python

import pygame

#Pygame is a set of cross module Python Codes that is designed to program video games using Python language

pygame.init() #Initializes all of the imported Pygame modules
dis=pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake game by Nikky')
 
blue=(0,0,255)
red=(255,0,0)
 
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,blue,[200,150,10,10]) #draw.rect() can be used to draw rectangles in Pygame
    pygame.display.update()
pygame.quit()
quit()