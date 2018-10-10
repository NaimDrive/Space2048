import pygame
import os
import sys
import space2048_niv1 as sp1 , space2048_niv2 as sp2 , space2048_niv3 as sp3
from space2048_menu import *
from space2048_rules import *
from space2048_credits import *
from space2048_etats import *
from space2048_over import *
from space2048_player import *
from space2048_win import *



pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
done = False
police=pygame.font.Font("contenu/Roboto-Black.ttf",26)
pygame.mixer.music.load("contenu/musique_accueil.mp3")
etat=menu

menu(screen, police)

#MUSIQUE
pygame.mixer.music.play()

_image_library = {}
def mousepos():
    return pygame.mouse.get_pos()
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type== pygame.MOUSEBUTTONDOWN:
            if (mouse[0]>720 and mouse[0]<860 and mouse[1]>370 and mouse[1]<450 and etat==menu):
                rules(screen,police)
                etat=rules

            if (mouse[0]>130 and mouse[0]<250 and mouse[1]>70 and mouse[1]<100 and etat==rules):
                menu(screen,police)
                etat=menu
            if (mouse[0]>880 and mouse[0]<1020 and mouse[1]>370 and mouse[1]<450 and etat==menu):
                credits(screen,police)
                etat=credits
            if (mouse[0]>130 and mouse[0]<250 and mouse[1]>70 and mouse[1]<100 and etat==credits):
                menu(screen,police)
                etat=menu
                
            if (mouse[0]>720 and mouse[0]<810 and mouse[1]>240 and mouse[1]<320 and etat==menu):
                sp1.game(screen,police)
                etat = sp1.game
            
            if (mouse[0]>825 and mouse[0]<915 and mouse[1]>240 and mouse[1]<320 and etat==menu):
                sp2.game(screen,police)
                etat = sp2.game

            if (mouse[0]>930 and mouse[0]<1020 and mouse[1]>240 and mouse[1]<320 and etat==menu):
                sp3.game(screen,police)
                etat = sp3.game
            
            if (mouse[0]>335 and mouse[0]<635 and mouse[1]>380 and mouse[1]<460 and etat==over):
                menu(screen,police)
                etat = menu

            if (mouse[0]>335 and mouse[0]<635 and mouse[1]>545 and mouse[1]<625 and etat==win):
                menu(screen,police)
                etat = menu

    if etat==sp1.game or etat==sp2.game or etat==sp3.game:
        if sp1.gameOver() or sp2.gameOver() or sp3.gameOver():
            over(screen,police)
            etat = over

            sp1.en = []
            sp1.joueur = Player(640) 
                
            sp2.en = []
            sp2.joueur = Player(640) 

            sp3.en = []
            sp3.joueur = Player(640)

        elif sp1.won() or sp2.won() or sp3.won():
            win(screen,police)
            etat = win

            sp1.en = []
            sp1.joueur = Player(640) 
                
            sp2.en = []
            sp2.joueur = Player(640) 

            sp3.en = []
            sp3.joueur = Player(640)


    mouse=mousepos()
    pygame.display.flip()
