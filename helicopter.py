import pygame
import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, sqrt, tan, asin, pi
from constants import *

class Cone(object):
    def __init__(self, densidade, raio, geratriz, v_inicial, altura_inicial, vertice, v_ang, a_ang, iteracoes):
        self.gravidade = 9.81
        self.densidade = densidade
        self.raio = raio
        self.geratriz = geratriz
        self.v_inicial = v_inicial
        self.area = pi * self.raio * self.geratriz
        self.massa = self.area * self.densidade
        self.area_proj = pi * self.raio * self.raio
        self.v_inicial = v_inicial
        self.angulo = asin(self.raio / self.geratriz)
        self.vertice = vertice
        self.p_direita = np.array([self.raio, -self.geratriz * cos(self.angulo)])
        self.p_esquerda = np.array([-self.raio, -self.geratriz * cos(self.angulo)])
        self.rotacao = np.radians(0.002)
        self.drotacao = v_ang
        self.dtempo = SAMPLE_TIME
        self.a_ang = a_ang
        self.velocidade = v_inicial
        self.v_ang = v_ang
        self.altura_queda = 0
        self.iteracoes = iteracoes
        
    def draw(self, screen):
        poligono_pontos = [self.vertice, self.vertice + self.p_direita, self.vertice + self.p_esquerda]
        pygame.draw.polygon(screen, (0, 0, 255), poligono_pontos)

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
        
        




