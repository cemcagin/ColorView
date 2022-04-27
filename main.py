from email.errors import MultipartInvariantViolationDefect
import pygame
pygame.init()
pygame.font.init()
import time
pygame.display.init()
import sys
from re import X
import matplotlib.image as image
from PIL import Image
import numpy as np

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

X = 1280
Y = 720
running = True
X_photo = 280
Y_photo = 120

background = pygame.image.load("background.png")
picture = pygame.image.load("porcelaincat.jpg")
picture = pygame.transform.scale(picture, (720, 480))

redbutton = pygame.Rect((100,620),(180,60))
greenbutton = pygame.Rect((550,620),(180,60))
bluebutton = pygame.Rect((1000,620),(180,60))
resetbutton = pygame.Rect((10,10),(240,80))


screen = pygame.display.set_mode((X, Y))


pygame.display.set_caption('colorview')

frame_left = pygame.Rect((270,110),(10,500))
frame_top = pygame.Rect((270,110),(740,10))
frame_right = pygame.Rect((1000,110),(10,500))
frame_bottom = pygame.Rect((270,600),(740,10))

font = pygame.font.SysFont("Segoe UI", 30)
titlefont = pygame.font.SysFont("Segoe UI",60)
title = titlefont.render("Color View", False, black)	
title_rect = title.get_rect(center=(X/2, 20))
resettext = titlefont.render("RESET",False,black)
reset_rect = resettext.get_rect(center=(125,45))

def refresh():
    screen.blit(background,(0,0))
    pygame.draw.rect(screen, red, redbutton)
    pygame.draw.rect(screen, green, greenbutton)
    pygame.draw.rect(screen, blue, bluebutton)
    screen.blit(title, title_rect)
    pygame.draw.rect(screen, black, frame_left)
    pygame.draw.rect(screen, black, frame_top)
    pygame.draw.rect(screen, black, frame_right)
    pygame.draw.rect(screen, black, frame_bottom)
    screen.blit(picture,(X_photo,Y_photo))
    pygame.draw.rect(screen, gray, resetbutton)
    screen.blit(resettext, reset_rect)
    pygame.display.flip()

def modify():
    picture=image.imread('porcelaincat.jpg')
    for row in picture:
        for pixel in row:
            if pixel[0] <= pixel[1] or pixel[0] <= pixel[2]:
                pixel[0] = pixel[1] = pixel[2] = 255
    picture = Image.fromarray(picture, 'RGB')
    screen.blit(picture,(X_photo,Y_photo))

refresh()


while running:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if redbutton.collidepoint(pygame.mouse.get_pos()):
            refresh()
            text = titlefont.render("Red",False,red)
            caption_rect = text.get_rect(center=(X/2,70))
            screen.blit(text,caption_rect)
            modify()
            pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if greenbutton.collidepoint(pygame.mouse.get_pos()):
            refresh()
            text = titlefont.render("Green",False,green)
            caption_rect = text.get_rect(center=(X/2,70))
            screen.blit(text,caption_rect)
            pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if bluebutton.collidepoint(pygame.mouse.get_pos()):
            refresh()
            text = titlefont.render("Blue",False,blue)
            caption_rect = text.get_rect(center=(X/2,70))
            screen.blit(text,caption_rect)
            pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if resetbutton.collidepoint(pygame.mouse.get_pos()):
            refresh()
    pygame.display.flip()





#----------COPY CODE----------#

#from re import X
#import matplotlib.image as image
#from PIL import Image
#import numpy as np
#
#img=image.imread('porcelaincat.jpg')
#print('The Shape of the image is:',img.shape)
#print('The image as array is:')
#print(img)
#
#from PIL import Image
#import numpy as np
#
#for row in img:
#  for pixel in row:
#     if pixel[0] <= pixel[1] or pixel[0] <= pixel[2]:
#       pixel[0] = pixel[1] = pixel[2] = 255
#
#
#img = Image.fromarray(img, 'RGB')
#
#img.save('my.png')
#img.show()
