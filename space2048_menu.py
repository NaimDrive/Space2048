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

def menu(screen,police):
	#BG
	screen.blit(get_image('accueil.bmp'), (0,0,20, 20))
	#TITRE
	title=pygame.font.SysFont('arial',100)
	title_space=title.render("Space",True,(255,255,255))
	titlepos=title_space.get_rect()
	titlepos.centerx=300
	titlepos.centery=180
	screen.blit(title_space,titlepos)
	title=pygame.font.SysFont('freesans',100)
	title_text=title.render("2048",True,(255,255,255))
	textpos=title_text.get_rect()
	textpos.centerx=300
	textpos.centery=380
	screen.blit(title_text,textpos)
	#RECT
	rectChoix=pygame.draw.rect(screen, (255,255, 255), pygame.Rect(720, 110, 300, 80))
	screen.blit(police.render('Choisissez un niveau',True,(0,0,0)),(743,135))
	#NIVEAUX
	pygame.draw.rect(screen, (255,255, 255), pygame.Rect(720, 240, 90, 80))
	screen.blit(police.render('1',True,(0,0,0)),(758,265))
	pygame.draw.rect(screen, (255,255, 255), pygame.Rect(825, 240, 90, 80))
	screen.blit(police.render('2',True,(0,0,0)),(863,265))
	pygame.draw.rect(screen, (255,255, 255), pygame.Rect(930, 240, 90, 80))
	screen.blit(police.render('3',True,(0,0,0)),(968,265))
	#REGLES
	pygame.draw.rect(screen, (255,255, 255), pygame.Rect(720, 370, 140, 80))
	screen.blit(police.render('Règles',True,(0,0,0)),(748,395))
	#CREDITS
	pygame.draw.rect(screen, (255,255, 255), pygame.Rect(880, 370, 140, 80))
	screen.blit(police.render('Crédits',True,(0,0,0)),(905,395))
