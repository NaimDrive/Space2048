import sys
import pygame
import math
import random
import time
pygame.init()
pygame.font.init()
from space2048_enemy import *
from space2048_player import *
from space2048_menu import *



font = pygame.font.SysFont('Courrier New', 30)


display = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
fond = pygame.image.load("planete/fond.jpg").convert()
clock = pygame.time.Clock()
FPS = 60
speed = 10*1.5
vitesse_cube = 1*1.6
score = 2
en = []

#etat=menu
#menu(display,font)

joueur = Player(640)

#Pour test le win
#joueur.setValue(1024)


def motion_test():
    #joueur = Player(640)
    score1 = score
    #print(score1)
    while not gameOver() and not won(): 
        # check quit
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            joueur.setX(joueur.getX()-speed)
        if pressed[pygame.K_RIGHT]:
            joueur.setX(joueur.getX()+1*speed)
        if joueur.getX() == -40+(1*speed):
            joueur.setX(1320)
        if joueur.getX() >= 1321:
            joueur.setX(-30)

        display.blit(fond, (0, 0))
        display.blit(joueur.getImage(), (joueur.getX(), joueur.getY()))


        for i in range(len(en)):
            display.blit(en[i].getPlanete(), (en[i].getX(), en[i].getY()))
        pygame.display.flip()

        afficherScore(joueur.getValue())

        updateCube(len(en))
        # draw the rect and flip the display
        display.blit(joueur.getImage(), (joueur.getX(), joueur.getY()))


        # Check colisions
        score1 = checkColisions(joueur, score)

        # tick the clock
        pygame.display.flip()
        clock.tick(FPS)
    

def afficherScore(score):
    scoreAffiche = "Score : " + str(score)
    textScore = font.render(scoreAffiche, False, (255, 255, 255))
    display.blit(textScore, (50,50))
    pygame.display.flip()


def genererCube(difficulte):
    for i in range(difficulte):
        en.append(Enemy(random.randint(0,1280),vitesse_cube))


def updateCube(difficulte):
    for i in range(difficulte):
        en[i].update(1)

def won():
    if checkColisions(joueur, joueur.getValue()) == "Won":
        return True
    else:
        return False

def gameOver():
    if checkColisions(joueur, joueur.getValue()) == "Game over":
        return True
    else:
        False


def checkColisions(joueur, score):
    j = len(en)
    for i in range(j):
        if en[i].getY() >720:
            en[i].remove()
        if en[i].getX() <= joueur.getX() + 40 and en[i].getX() >= joueur.getX()-40:
            if en[i].getY() <= joueur.getY() + 40 and en[i].getY() >= joueur.getY()-40 and en[i].getvalue() == joueur.getValue():
                if joueur.getValue() == 1024 and en[i].getvalue() == 1024:
                    #score = joueur.setValue(2048)
                    print("C'est gagné non d'une pipe !")
                    print("Score : " +  str(2048))
                    return "Won"
                    #pygame.quit()
                    #sys.exit()
                else:
                    joueur.setValue(en[i].getvalue()*2)
                    print("valeur du joueur :", joueur.getValue())
                    joueur.setImage()
                    en[i].remove()
                    score = joueur.getValue()
                    return score
            if en[i].getY() <= joueur.getY() + 40 and en[i].getY() >= joueur.getY()-40:
                if joueur.getValue() == 2 and en[i].getvalue() != 2:
                    print("Game over")
                    print("Score : ", score)
                    #exec(open("space2048_over.py").read())
                    #over(display,font)
                    #etat = over
                    #pygame.quit()
                    #sys.exit()
                    return "Game over"
                    
                elif en[i].getvalue() < joueur.getValue():
                    joueur.setValue(en[i].getvalue())
                    joueur.setImage()
                    en[i].remove()
                    score = joueur.getValue()
                    return score
                elif en[i].getvalue() > joueur.getValue():
                    joueur.setValue(joueur.getValue()//2)
                    joueur.setImage()
                    en[i].remove()
                    score = joueur.getValue()
                    return score
    return score

def game(screen,police):
    genererCube(12)
    motion_test()  
    
