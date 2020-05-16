# A3Q5
# Author: Farzad Rahman
# Date Start: 15/04/20
# ICS3UI - 03, Ms. Harris

"""
WOW me with your Pygame Sprite knowledge. You may use one I gave you in
class, long ago (a square called Car) as a starting point or create your own. Have
fun with this one!
"""

# Background from https://www.amazon.ca/Click-Play-Non-Slip-Educational-Bedroom-79/dp/B07DJXBVPD
# Modifications:



import pygame
import random

pygame.init() # Initializes all the modules
screen = pygame.display.set_mode((1500, 756)) # Sets screen with given display size
pygame.display.set_caption("First Game")


black = (0,0,0)
red = (255,0,0)


class Background(pygame.sprite.Sprite):
    def __init__(self, picture, origin):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = origin



class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        super(Vehicle, self).__init__()
        self.image = pygame.image.load('car_right.png')
        self.x = 50
        self.y = 50
        self.vel = 20
        self.rect = pygame.Rect(self.x, self.y,64,32)

    def update(self,direction):
        self.rect = pygame.Rect(self.x, self.y,64,32)
        if direction == 'up':
            self.rect = pygame.Rect(self.x, self.y, 32, 64)
            self.image = pygame.image.load('car_up.png')
        elif direction == 'down':
            self.rect = pygame.Rect(self.x, self.y, 32, 64)
            self.image = pygame.image.load('car_down.png')
        elif direction == 'right':
            self.rect = pygame.Rect(self.x, self.y, 64, 32)
            self.image = pygame.image.load('car_right.png')
        elif direction == 'left':
            self.rect = pygame.Rect(self.x, self.y, 64, 32)
            self.image = pygame.image.load('car_left.png')



background = Background('bgpic.jpg',[0,0])
group = pygame.sprite.Group(Vehicle())



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        group.sprites()[0].x -= group.sprites()[0].vel
        group.update('left')
    elif keys[pygame.K_RIGHT]:
        group.sprites()[0].x += group.sprites()[0].vel
        group.update('right')
    elif keys[pygame.K_UP]:
        group.sprites()[0].y -= group.sprites()[0].vel
        group.update('up')
    elif keys[pygame.K_DOWN]:
        group.sprites()[0].y += group.sprites()[0].vel
        group.update('down')

    screen.blit(background.image, background.rect)
    group.draw(screen)

    pygame.display.update()

    if group.sprites()[0].x <= 0 or group.sprites()[0].y <=0:
        group.sprites()[0].image = pygame.image.load('explosion.png')
        group.draw(screen)
    elif group.sprites()[0].x >= 1468 or group.sprites()[0].y >= 692:
        group.sprites()[0].image = pygame.image.load('explosion.png')
        group.sprites()[0].x -= 50
        group.sprites()[0].y -= 50

pygame.quit()





















