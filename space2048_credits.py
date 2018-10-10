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

def credits(screen,police):
	#BG
	screen.blit(get_image('accueil.bmp'), (0,0,20, 20))
	#TITRE
	rules=pygame.font.SysFont('arial',55)
	rules_space=rules.render("Crédits",True,(255,255,255))
	rulespos=rules_space.get_rect()
	rulespos.centerx=630
	rulespos.centery=100
	screen.blit(rules_space,rulespos)
	##
	nico=pygame.font.SysFont('arial',26)
	nico_space=nico.render("Nicolas PINHAL",True,(255,255,255))
	nicopos=nico_space.get_rect()
	nicopos.centerx=390
	nicopos.centery=250
	screen.blit(nico_space,nicopos)
	##
	alex=pygame.font.SysFont('arial',26)
	alex_space=alex.render("Alexandre DUHEM",True,(255,255,255))
	alexpos=alex_space.get_rect()
	alexpos.centerx=390
	alexpos.centery=400
	screen.blit(alex_space,alexpos)
	##
	maxa=pygame.font.SysFont('arial',26)
	maxa_space=maxa.render("Maxance CAPILLIEZ",True,(255,255,255))
	maxapos=maxa_space.get_rect()
	maxapos.centerx=890
	maxapos.centery=250
	screen.blit(maxa_space,maxapos)
	##
	naim=pygame.font.SysFont('arial',26)
	naim_space=naim.render("Naïm SEDDAR",True,(255,255,255))
	naimpos=naim_space.get_rect()
	naimpos.centerx=890
	naimpos.centery=400
	screen.blit(naim_space,naimpos)
	##
	cloe=pygame.font.SysFont('arial',26)
	cloe_space=cloe.render("Cloé WARLOUZET",True,(255,255,255))
	cloepos=cloe_space.get_rect()
	cloepos.centerx=640
	cloepos.centery=550
	screen.blit(cloe_space,cloepos)
	#RETOUR
	retour=pygame.font.SysFont('arial',26)
	retour_space=retour.render("RETOUR",True,(168,231,248))
	retourpos=retour_space.get_rect()
	retourpos.centerx=160
	retourpos.centery=90
	screen.blit(retour_space,retourpos)
