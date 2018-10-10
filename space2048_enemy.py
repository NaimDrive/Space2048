import sys
import pygame
import math
import random

class Enemy:

    def __init__(self, x, speed):
        self.rect = pygame.rect.Rect((x,0), (40,40))
        self.speed = speed*(random.randint(100,350)/100)
        self.valueTab = [2,4,8,16,32,64,128,256,512,1024]
        self.value = self.valueTab[random.randint(0,9)]
        self.planete = self.setPlanete()

    def update(self, time_passed):
        self.rect.y += self.speed

    def setPlanete(self):
        if self.value == 2:
            planete = pygame.image.load("planete/planet2.png").convert_alpha()
            return planete
        elif self.value == 4:
            planete = pygame.image.load("planete/planet4.png").convert_alpha()
            return planete
        elif self.value == 8:
            planete = pygame.image.load("planete/planet8.png").convert_alpha()
            return planete
        elif self.value == 16:
            planete = pygame.image.load("planete/planet16.png").convert_alpha()
            return planete
        elif self.value == 32:
            planete = pygame.image.load("planete/planet32.png").convert_alpha()
            return planete
        elif self.value == 64:
            planete = pygame.image.load("planete/planet64.png").convert_alpha()
            return planete
        elif self.value == 128:
            planete = pygame.image.load("planete/planet128.png").convert_alpha()
            return planete
        elif self.value == 256:
            planete = pygame.image.load("planete/planet256.png").convert_alpha()
            return planete
        elif self.value == 512:
            planete = pygame.image.load("planete/planet512.png").convert_alpha()
            return planete
        elif self.value == 1024:
            planete = pygame.image.load("planete/planet1024.png").convert_alpha()
            return planete

    def getPlanete(self):
        return self.planete

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def getvalue(self):
        return self.value

    def remove(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, 1280)
        self.value = self.valueTab[random.randint(0, 9)]
        self.planete = self.setPlanete()


