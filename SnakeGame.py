#Building the Snake game in Python

import pygame

#Pygame is a set of cross module Python Codes that is designed to program video games using Python language

pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Nikky')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()