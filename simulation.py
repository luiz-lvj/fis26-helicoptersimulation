import pygame
import numpy as np
from matplotlib import pyplot as plt
from helicopter import Helicopter
from math import pi
from constants import *

pygame.init()

screen_size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Simulação')

clock = pygame.time.Clock()

pivot = np.array((WIDTH*0.45, HEIGHT*0.75))

helicopter = Helicopter(18, 37, 4, 22, 3, 23.5, 34, 4.61, pivot ,1.05, 0)

running = True
tempo = 0
altura_inicial = 0
lista_yt = [[tempo, altura_inicial]]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or helicopter.iteracoes >= 800:
            running = False

    screen.fill(BACKGROUND_COLOR)

    helicopter.draw(screen)

    pygame.display.flip()

    tempo = tempo + helicopter.dtempo
    altura_atual = lista_yt[-1][1]
    
    lista_yt.append(helicopter.moveUp(tempo, altura_atual))

    clock.tick(FREQUENCY)

pygame.quit()

alturas = []
tempos = []
for item in lista_yt:
    alturas.append(item[1])
    tempos.append(item[0])

plt.figure(figsize=fig_size)
plt.plot(tempos, alturas)
plt.xlabel('Tempo')
plt.ylabel('Altura')
plt.savefig('plot.%s'%fig_format, format = fig_format)
plt.show()
