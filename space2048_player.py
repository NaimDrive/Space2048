import sys
import pygame
import math
import random

class Player:

    def __init__(self,x):
        self.rect = pygame.rect.Rect((x, 640), (40, 40))
        self.value = 2
        self.image = pygame.image.load("contenu/soucoupe-volante-2.png").convert_alpha()

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def setX(self, x):
        self.rect.x = x

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v

    def getImage(self):
        return self.image

    def setImage(self):
        if self.value == 2:
            self.image = pygame.image.load("contenu/soucoupe-volante-2.png").convert_alpha()
        elif self.value == 4:
            self.image = pygame.image.load("contenu/soucoupe-volante-4.png").convert_alpha()
        elif self.value == 8:
            self.image = pygame.image.load("contenu/soucoupe-volante-8.png").convert_alpha()
        elif self.value == 16:
            self.image = pygame.image.load("contenu/soucoupe-volante-16.png").convert_alpha()
        elif self.value == 32:
            self.image = pygame.image.load("contenu/soucoupe-volante-32.png").convert_alpha()
        elif self.value == 64:
            self.image = pygame.image.load("contenu/soucoupe-volante-64.png").convert_alpha()
        elif self.value == 128:
            self.image = pygame.image.load("contenu/soucoupe-volante-128.png").convert_alpha()
        elif self.value == 256:
            self.image = pygame.image.load("contenu/soucoupe-volante-256.png").convert_alpha()
        elif self.value == 512:
            self.image = pygame.image.load("contenu/soucoupe-volante-512.png").convert_alpha()
        elif self.value == 1024:
            self.image = pygame.image.load("contenu/soucoupe-volante-1024.png").convert_alpha()
