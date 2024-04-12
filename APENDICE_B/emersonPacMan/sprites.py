import pygame
from pygame.locals import *
from sys import exit
from constantes import *


import pygame
import random
pygame.init()




class Comida(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.imagens_comida = []
        for i in range(10):  
            for j in range(2):  
                img = self.sprite_sheet.subsurface((j * COMIDA_TUPLE[0], i * COMIDA_TUPLE[0]), COMIDA_TUPLE)
                img = pygame.transform.scale(img, (int(COMIDA_TUPLE[0]/2), int(COMIDA_TUPLE[0]/2)))  
                self.imagens_comida.append(img)
        self.index_lista = 0
        self.image = self.imagens_comida[self.index_lista]
        self.rect = self.image.get_rect()
        self.escala_inicial = int(COMIDA_TUPLE[0]/2)
        self.escala_atual = self.escala_inicial
        self.escala_maxima = int(COMIDA_TUPLE[0])
        self.aumentando = True
        self.t_escala_atual =  self.escala_atual

    def update(self):
    
        if self.aumentando:
            self.t_escala_atual += 0.25
            self.escala_atual = int(self.t_escala_atual )
            if self.escala_atual >= self.escala_maxima:
                self.aumentando = False
        else:
            self.t_escala_atual -= 0.25
            self.escala_atual = int(self.t_escala_atual )
            if self.escala_atual <= self.escala_inicial:
                self.aumentando = True

       
        self.image = pygame.transform.scale(self.imagens_comida[self.index_lista], (self.escala_atual, self.escala_atual))

    def atualizar_posicao(self):
        self.index_lista = random.randint(0,19)
        self.rect.x = random.randint(0, LARGURA - self.escala_atual)
        self.rect.y = random.randint(0, ALTURA - self.escala_atual)
        
class Pacman(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.imagens_pacman = []
        for i in range(2):  
            for j in range(4):  
                img = self.sprite_sheet.subsurface((j * PACMAN_TUPLE[0], i *  PACMAN_TUPLE[1]), PACMAN_TUPLE)
                img = pygame.transform.scale(img, (PACMAN_TUPLE[0]*PACMAN_ESCALE, PACMAN_TUPLE[1]*PACMAN_ESCALE))  
                self.imagens_pacman.append(img)
        self.index_lista = 5
        self.image = self.imagens_pacman[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (LARGURA // 2, ALTURA // 2)
        self.direcao = 'none'


    def update(self, event, pacman_sprite):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                pacman_sprite.mover("cima")
            elif event.key == K_DOWN:
                pacman_sprite.mover("baixo")
            elif event.key == K_LEFT:
                pacman_sprite.mover("esquerda")
            elif event.key == K_RIGHT:
                pacman_sprite.mover("direita")

        if self.direcao is not None:
            if self.index_lista > 7:
                self.index_lista = 4
            self.index_lista += 0.25
            self.image = self.imagens_pacman[int(self.index_lista)]


            if self.direcao == "cima":
                self.rect.y -= 5
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direcao == "baixo":
                self.rect.y += 5
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direcao == "esquerda":
                self.rect.x -= 5
                self.image = pygame.transform.flip(self.image, True, False) 
            elif self.direcao == "direita":
                self.rect.x += 5
                if self.image.get_size()[0] < 0:
                    self.image = pygame.transform.flip(self.image, True, False)  

            
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > ALTURA:
                self.rect.bottom = ALTURA

    def mover(self, direcao):
        self.direcao = direcao

class Antman(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.imagens_antman = []
        for i in range(2): 
            for j in range(4):  
                img = self.sprite_sheet.subsurface((j * PACMAN_TUPLE[0], i * PACMAN_TUPLE[1]), PACMAN_TUPLE)
                img = pygame.transform.scale(img, (PACMAN_ESCALE * PACMAN_TUPLE[0], PACMAN_ESCALE * PACMAN_TUPLE[1]))  
                img = self.aplicar_negativo_tons(img)
                self.imagens_antman.append(img)
        self.index_lista = 0
        self.image = self.imagens_antman[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (LARGURA, ALTURA)
        self.direcaoh = 'none'
        self.direcaow = 'none'


    def update(self, x, y, antman_sprite  ):
        if self.rect.colliderect(antman_sprite.rect):
            self.mudar_direcao_para_evitar_colisao(antman_sprite)
        
        if y <  self.rect.y:
            antman_sprite.moverh("cima")
        elif y >  self.rect.y:
            antman_sprite.moverh("baixo")
        if x <  self.rect.x:
            antman_sprite.moverw("esquerda")
        elif x > self.rect.x:
            antman_sprite.moverw("direita")

        if self.direcaoh is not None or self.direcaow is not None :
            if self.index_lista > 4:
                self.index_lista = 2
            self.index_lista += 0.1
            self.image = self.imagens_antman[int(self.index_lista)]

            valor = ((abs(self.rect.x -x)*8)/1280)
            velocidade = 2 if valor < 2 else (10 if valor > 10 else valor)

            if self.direcaoh == "cima":
                self.rect.y -=velocidade
                self.direcaoh = 'none'
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direcaoh == "baixo":
                self.rect.y +=velocidade
                self.direcaoh = 'none'
                self.image = pygame.transform.rotate(self.image, -90)
            if self.direcaow == "esquerda":
                self.rect.x -= velocidade
                self.direcaow = 'none'
                self.image = pygame.transform.flip(self.image, True, False)  
            elif self.direcaow == "direita":
                self.rect.x +=velocidade
                self.direcaow = 'none'
                if self.image.get_size()[0] < 0:
                    self.image = pygame.transform.flip(self.image, True, False)  

            
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > ALTURA:
                self.rect.bottom = ALTURA

    def moverh(self, direcao):
        self.direcaoh = direcao

    def moverw(self, direcao):
        self.direcaow = direcao

    def mudar_direcao_para_evitar_colisao(self, antman_sprite):
        # Verifica a direção do outro fantasma
        delta_x = self.rect.x - antman_sprite.rect.x
        delta_y = self.rect.y - antman_sprite.rect.y

        # Se o outro fantasma estiver à direita, mova-se para a esquerda
        if delta_x < 0:
            self.moverw("esquerda")
        # Se o outro fantasma estiver à esquerda, mova-se para a direita
        elif delta_x > 0:
            self.moverw("direita")
        # Se o outro fantasma estiver abaixo, mova-se para cima
        elif delta_y < 0:
            self.moverh("cima")
        # Se o outro fantasma estiver acima, mova-se para baixo
        elif delta_y > 0:
            self.moverh("baixo")

    def aplicar_negativo_tons(self, surface):
        img = surface.copy()  
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                cor = img.get_at((x, y))  
                
                if cor != (163, 73, 164, 255):
                    img.set_at((x, y), (255 - cor[0], 255 - cor[1], 255 - cor[2], cor[3])) 
        return img

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura,coordenadas):
        super().__init__()
        self.image = pygame.Surface((largura, altura))  
        self.cor = cor 
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordenadas 