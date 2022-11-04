import random

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x = 1200
y = 720

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Space')

bg = pygame.image.load('cenario/fundo.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

nave = pygame.image.load('personagem/nave.png').convert_alpha()
nave = pygame.transform.scale(nave, (50,50))

player = pygame.image.load('personagem/player.png').convert_alpha()
player = pygame.transform.scale(player, (50,50))
player = pygame.transform.rotate(player, -90)

missil = pygame.image.load('personagem/missil.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -85)

tabuada = pygame.image.load('personagem/tabuada.png').convert_alpha()
tabuada = pygame.transform.scale(tabuada, (1100,240))

pos_nave_x = 500
pos_nave_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

pos_tabuada_x = 5
pos_tabuada_y = 5

resultado1 = 0

triggered = False

rodando = True

font = pygame.font.SysFont('fonts/BRL.TTF', 50)

player_rect = player.get_rect()
nave_rect = nave.get_rect()
missil_rect = missil.get_rect()


def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]

def colisions():
    global resultado1
    if player_rect.colliderect(nave_rect) or nave_rect.x == 60:
        resultado1 -= 2
        return  True
    elif missil_rect.colliderect(nave_rect):
        resultado1 += 2
        return True
    else:
        return False

while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False

    tela.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    tela.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        tela.blit(bg, (rel_x, 0))

    #Teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1

        if not triggered:
             pos_missil_y -=1

    if tecla[pygame.K_DOWN] and pos_player_y < 655:
        pos_player_y += 1

        if not triggered:
             pos_missil_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 2

    #respawn
    if pos_nave_x == 50:
        pos_nave_x = respawn()[0]
        pos_nave_y = respawn()[1]

    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()

    if pos_nave_x == 50 or colisions():
        pos_nave_x = respawn()[0]
        pos_nave_y = respawn()[1]

    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    nave_rect.y = pos_nave_y
    nave_rect.x = pos_nave_x

    #movimento
    x-=2
    pos_nave_x -=1

    pos_missil_x += vel_missil_x


    #criarimagem
    tela.blit(nave, (pos_nave_x, pos_nave_y))
    tela.blit(missil, (pos_missil_x,pos_missil_y))
    tela.blit(player, (pos_player_x, pos_player_y))
    tela.blit(tabuada, (pos_tabuada_x, pos_tabuada_y))


    pygame.display.update()

