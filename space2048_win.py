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

def win(screen,police):
	#BG
	screen.blit(get_image('accueil.bmp'), (0,0,20, 20))
	#FELICITATIONS
	win=pygame.font.SysFont('arial',100)
	win_space=win.render("Félicitations!",True,(255,255,255))
	winpos=win_space.get_rect()
	winpos.centerx=485
	winpos.centery=250
	screen.blit(win_space,winpos)

	#SCORE
	screen.blit(police.render('VOUS AVEZ ATTEINT 2048',True,(230,126,34)),(330,405))
