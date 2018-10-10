import os
import time
import pygame

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def rules(screen,police):
	#BG
	screen.blit(get_image('accueil.bmp'), (0,0,20, 20))
	#TITRE
	rules=pygame.font.SysFont('arial',70)
	rules_space=rules.render("Règles  du  jeu",True,(255,255,255))
	rulespos=rules_space.get_rect()
	rulespos.centerx=620
	rulespos.centery=140
	screen.blit(rules_space,rulespos)
	#EXPLICATIONS
	expl=pygame.font.SysFont('arial',26)
	expl_space=expl.render("Les règles du jeu sont relativement simples, il s'agit de toucher une planète ayant",True,(255,255,255))
	explpos=expl_space.get_rect()
	explpos.centerx=600
	explpos.centery=270
	screen.blit(expl_space,explpos)
	##
	expl2=pygame.font.SysFont('arial',26)
	expl2_space=expl2.render("le même chiffre que la fusée pour pouvoir doubler sa valeur, jusqu'à atteindre 2048.",True,(255,255,255))
	expl2pos=expl2_space.get_rect()
	expl2pos.centerx=613
	expl2pos.centery=310
	screen.blit(expl2_space,expl2pos)
	###
	expl3=pygame.font.SysFont('arial',26)
	expl3_space=expl3.render("En revanche, si vous touchez un chiffre différent de celui de la fusée, deux cas se",True,(255,255,255))
	expl3pos=expl3_space.get_rect()
	expl3pos.centerx=600
	expl3pos.centery=400
	screen.blit(expl3_space,expl3pos)
	####
	expl4=pygame.font.SysFont('arial',26)
	expl4_space=expl4.render("présentent:",True,(255,255,255))
	expl4pos=expl4_space.get_rect()
	expl4pos.centerx=203
	expl4pos.centery=440
	screen.blit(expl4_space,expl4pos)
	#####
	expl5=pygame.font.SysFont('arial',26)
	expl5_space=expl5.render("- Soit le chiffre de la planète est plus petit,dans ce cas vous retombez à cette valeur",True,(255,255,255))
	expl5pos=expl5_space.get_rect()
	expl5pos.centerx=625
	expl5pos.centery=505
	screen.blit(expl5_space,expl5pos)
	######
	expl6=pygame.font.SysFont('arial',26)
	expl6_space=expl6.render("- Soit le chiffre de la planète est grand, dans ce cas vous retombez à l'étage inférieur",True,(255,255,255))
	expl6pos=expl6_space.get_rect()
	expl6pos.centerx=630
	expl6pos.centery=555
	screen.blit(expl6_space,expl6pos)
	#RETOUR
	retour=pygame.font.SysFont('arial',26)
	retour_space=retour.render("RETOUR",True,(168,231,248))
	retourpos=retour_space.get_rect()
	retourpos.centerx=160
	retourpos.centery=90
	screen.blit(retour_space,retourpos)
