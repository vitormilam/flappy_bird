# Importando Biblioteca Pygame
import pygame
from pygame.locals import *

# Inicializando o pygame
pygame.init()

# Criando a tela
screen_width, screen_height = 600, 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")


# Criando o loop que manter o jogo aberto
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





pygame.quit()