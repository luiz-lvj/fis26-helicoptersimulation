import pygame
import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, sqrt, tan, asin, pi, atan
from constants import *

class Helicopter(object):
    def __init__(self, altura, largura, profundidade, comprimento_cauda, altura_cauda, massa,
                    raio_helice, velocidade_ar, vertice_inicio, c_aerodinamica, iteracoes):
        self.area_helice = pi * (M2PIX * raio_helice)**2
        self.velocidade_ar = M2PIX * velocidade_ar
        self.massa = massa
        self.c_aerodinamica = c_aerodinamica
        self.area_projetada = M2PIX**2 * altura * profundidade
        self.volume = M2PIX**3 * altura * largura * profundidade
        self.vertice_inicio = vertice_inicio
        self.altura_cauda = M2PIX * altura_cauda
        self.comprimento_cauda = M2PIX * comprimento_cauda
        self.altura = M2PIX * altura
        self.largura = M2PIX * largura
        self.profundidade = M2PIX * profundidade
        self.dtempo = SAMPLE_TIME
        self.iteracoes = iteracoes

        vertice1 = self.vertice_inicio
        vertice2 = vertice1 + np.array((0, self.altura))
        vertice3 = vertice2 + np.array((self.largura,0))
        vertice4 = vertice3 + np.array((0, -self.altura/2 + self.altura_cauda/2))
        vertice5 = vertice4 + np.array((self.comprimento_cauda, 0))
        vertice6 = vertice5 + np.array((0, -self.altura_cauda))
        vertice7 = vertice6 + np.array((-self.comprimento_cauda, 0))
        vertice8 = vertice7 + np.array((0, self.altura_cauda/2 - self.altura/2))
        self.vertices = [vertice1, vertice2, vertice3, vertice4, vertice5, vertice6, vertice7, vertice8]

    def draw(self, screen):
        pygame.draw.polygon(screen, (0, 0, 255), self.vertices)

    def move(self):
        dphi_dot = (self.a_ang * self.drotacao + self.v_ang**2 * sin(self.rotacao))
        self.rotacao = self.rotacao + self.dtempo * self.drotacao
        self.drotacao = self.drotacao - self.dtempo * dphi_dot
        
        forca = 0.5 * 1.293 * pi * (self.raio**2) * (self.velocidade**2) / 2 * cos(self.rotacao)
        self.altura_queda = self.altura_queda + self.velocidade*self.dtempo - (self.gravidade - forca/ self.massa) *\
                            (self.dtempo**2)/2
        d_altura = self.velocidade*self.dtempo - (self.gravidade - forca/ self.massa) *\
                            (self.dtempo**2)/2
        self.velocidade = self.velocidade - (self.gravidade - forca / self.massa) * self.dtempo


        self.vertice[1] = self.vertice[1] - d_altura

        matriz_rotacao = np.array(( (cos(self.rotacao), -sin(self.rotacao)),
                    (sin(self.rotacao), cos(self.rotacao)) ))

        self.iteracoes = self.iteracoes+1
        self.p_direita = matriz_rotacao.dot(self.p_direita)
        self.p_esquerda = matriz_rotacao.dot(self.p_esquerda)
        return [self.velocidade, forca]

    def moveUp(self, tempo, altura_atual):
        k = densidade_ar * self.c_aerodinamica * self.area_projetada /2
        a = densidade_ar * self.area_helice
        b = self.massa * a_gravidade
        c =  densidade_ar * self.volume * a_gravidade
        d = self.massa
        formula_v = 100#sqrt(-a+b-c) * tan(sqrt(k)*tempo*sqrt(-a+b-c)/d)/sqrt(k)

        deltay = self.dtempo * formula_v
        altura_atual = altura_atual + deltay
        self.iteracoes = self.iteracoes + 1
        for vertice in self.vertices:
            vertice = vertice + np.array((0, deltay))
        return [tempo,altura_atual]

        






        
        




