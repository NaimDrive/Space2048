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

def over(screen,police):
	#BG
	screen.blit(get_image('contenu/accueil.bmp'), (0,0,20, 20))
	#GAME OVER
	over=pygame.font.SysFont('arial',100)
	over_space=over.render("Game   Over",True,(255,255,255))
	overpos=over_space.get_rect()
	overpos.centerx=455
	overpos.centery=180
	screen.blit(over_space,overpos)
	#RECT
	rectRejouer=pygame.draw.rect(screen, (168,231,248), [335, 380, 300, 80],2)
	screen.blit(police.render('Rejouer',True,(168,231,248)),(440,405))