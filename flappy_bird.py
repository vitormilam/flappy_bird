# Importando Biblioteca Pygame
import pygame
from pygame.locals import *

# Inicializando o pygame
pygame.init()

# Criando a tela
screen_width, screen_height = 864, 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Criando variáveis do jogo:
ground_scroll = 0
scroll_speed = 4


# Carregar imagens
background = pygame.image.load('imgs/bg.png')
ground = pygame.image.load('imgs/ground.png')

# Criando o loop que mantem o jogo aberto
run = True
while run:


    # Adicionar background 
    screen.blit(background, (0,0))

    # Adicionar ground e movimentar para direita
    screen.blit(ground, (ground_scroll, 936))
    ground_scroll -= scroll_speed

    # Caso o player clique para fechar a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Atualiza tudo que acontece acima
    pygame.display.update()



pygame.quit()