import pygame
import numpy as np
from matplotlib import pyplot as plt
from cone import Cone
from math import pi
from constants import *

pygame.init()

screen_size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Simulação')

clock = pygame.time.Clock()

pivot = np.array((WIDTH/2, HEIGHT/10))

cone = Cone(0.75, 16, 47, -200, pivot[1]/4, pivot, 0.0001, -0.001, 0)

running = True
lista_fv = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or cone.iteracoes >= 800:
            running = False

    screen.fill(BACKGROUND_COLOR)

    cone.draw(screen)

    pygame.display.flip()

    lista_fv.append(cone.move())

    clock.tick(FREQUENCY)

pygame.quit()

forcas = []
velocidades = []

for item in lista_fv:
    forcas.append(item[1])
    velocidades.append(item[0])
plt.figure(figsize=fig_size)
plt.plot(velocidades, forcas)
plt.xlabel('Velocidade')
plt.ylabel('Força de Resistência')
plt.savefig('plot.%s'%fig_format, format = fig_format)
plt.show()
