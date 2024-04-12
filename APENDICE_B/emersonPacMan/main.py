import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

import pygame
import time
from pygame.locals import *
import os
import random
from constantes import *
from sprites import *
import obstaculos

class Creditos:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('CRÉDITOS FINAIS')
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.rect_tela = self.tela.get_rect()
        self.fonte = pygame.font.SysFont("Arial", 15)
        self.relogio = pygame.time.Clock()
        self.lista_creditos = CREDITOS
        self.textos = []
        self.configurar_textos()

    def configurar_textos(self):
        for i, linha in enumerate(self.lista_creditos):
            superficie_texto = self.fonte.render(linha, 1, (10, 10, 10))
            retangulo_texto = superficie_texto.get_rect(centerx=self.rect_tela.centerx, y=self.rect_tela.bottom + i * 45)
            self.textos.append((retangulo_texto, superficie_texto))

    def renderizar_creditos(self):
        for retangulo, superficie in self.textos:
            retangulo.move_ip(0, -1)
            self.tela.blit(superficie, retangulo)

    def todos_creditos_tela(self):
        return not self.rect_tela.collidelistall([retangulo for (retangulo, _) in self.textos])

    def executar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == QUIT or evento.type == KEYDOWN and evento.key == pygame.K_ESCAPE:
                    return

            self.tela.fill((255, 255, 255))

            self.renderizar_creditos()

            if self.todos_creditos_tela():
                return

            pygame.display.flip()
            self.relogio.tick(30)

class Game:
    def __init__(self):

        self.game_init = False
        self.game_over = False
        self.run = True
        self.iterar = 0
        self.color_fonte_tela_inicial = PRETO
        pygame.init()
        self.inicio = time.time()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Pac-Man')
        self.relogio = pygame.time.Clock()

        self.sprite_sheet_pacman = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'PacMan.png')).convert_alpha()
        self.sprite_sheet_comida = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'comida.png')).convert_alpha()
        self.pacman_logo = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'PacManLogo.png')).convert_alpha()
        self.pacman_logo = pygame.transform.scale(self.pacman_logo, (self.pacman_logo.get_width()/8, self.pacman_logo.get_height()/8))
        self.obstaculo_group = pygame.sprite.Group()
        self.comida_group = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.comida_sprite = None
        self.pacman_sprite = None
        self.antman_sprite = None
        self.antman_group = pygame.sprite.Group()
        self.contador_colisoes = 0
        self.fonte = pygame.font.Font(None, FONTE_SIZE)

        self.criar_obstaculos()
        self.criar_sprites()
        self.criar_comida()

    def criar_obstaculos(self):
        for obstacle_data in obstaculos.PRIMEIRO_BLOCO:
            cor = obstacle_data["cor"]
            largura = obstacle_data["largura"]
            altura = obstacle_data["altura"]
            coordenadas = obstacle_data["coordenadas"]
            
        
            obstaculo = Obstaculo(cor, largura, altura, coordenadas)
            self.obstaculo_group.add(obstaculo)

        for obstacle_data in obstaculos.SEGUNDO_BLOCO:
            cor = obstacle_data["cor"]
            largura = obstacle_data["largura"]
            altura = obstacle_data["altura"]
            coordenadas = obstacle_data["coordenadas"]
            
        
            obstaculo = Obstaculo(cor, largura, altura, coordenadas)
            self.obstaculo_group.add(obstaculo)

        for obstacle_data in obstaculos.CONTORNO:
            cor = obstacle_data["cor"]
            largura = obstacle_data["largura"]
            altura = obstacle_data["altura"]
            coordenadas = obstacle_data["coordenadas"]
            

            obstaculo = Obstaculo(cor, largura, altura, coordenadas)
            self.obstaculo_group.add(obstaculo)

    def criar_sprites(self):
        self.pacman_sprite = Pacman(self.sprite_sheet_pacman)
        self.sprites.add(self.pacman_sprite)
        antman_sprite = Antman(self.sprite_sheet_pacman)
        self.antman_group.add(antman_sprite)

    def criar_comida(self):
        
        self.comida_sprite = Comida(self.sprite_sheet_comida)
        self.comida_group.add(self.comida_sprite) 

    def atualizar(self, event):
        # Atualizações gerais
        self.comida_sprite.update() 
        self.pacman_sprite.update(event=event, pacman_sprite=self.pacman_sprite)
        for antman_sprite in self.antman_group:
            antman_sprite.update(x=self.pacman_sprite.rect.x, y=self.pacman_sprite.rect.y,antman_sprite= antman_sprite )

    def desenhar(self):
       # Desenho na tela
        self.antman_group.draw(self.tela)
        self.tela.blit(self.pacman_sprite.image, self.pacman_sprite.rect) 
        self.sprites.draw(self.tela)
        self.obstaculo_group.draw(self.tela)
        self.comida_group.draw(self.tela)
        texto = self.fonte.render(f'Pontos: {self.contador_colisoes} Dificuldade: {int(self.contador_colisoes/CONST_DIFICULDADE)} Tempo: {int(time.time()-self.inicio)}Seg',True, BRANCO)
        self.tela.blit(texto, (10, 10))

    def verificar_colisoes(self):

        for obstaculo in self.obstaculo_group:
            for antman_sprite in self.antman_group:
                if antman_sprite.rect.colliderect(obstaculo.rect):
                    if obstaculo.cor == ROXO:
                        pass
                    else:
                        
                    
                        if antman_sprite.rect.right > obstaculo.rect.left and antman_sprite.rect.left < obstaculo.rect.left:
                            antman_sprite.rect.right = obstaculo.rect.left
                        elif antman_sprite.rect.left < obstaculo.rect.right and antman_sprite.rect.right > obstaculo.rect.right:
                            antman_sprite.rect.left = obstaculo.rect.right
                        elif antman_sprite.rect.bottom > obstaculo.rect.top and antman_sprite.rect.top < obstaculo.rect.top:
                            antman_sprite.rect.bottom = obstaculo.rect.top
                        elif antman_sprite.rect.top < obstaculo.rect.bottom and antman_sprite.rect.bottom > obstaculo.rect.bottom:
                            antman_sprite.rect.top = obstaculo.rect.bottom
        for obstaculo in self.antman_group:
            for antman_sprite in self.antman_group:
                if antman_sprite.rect.colliderect(obstaculo.rect):
                        obstaculo.mudar_direcao_para_evitar_colisao(antman_sprite)
                    
                        if antman_sprite.rect.right > obstaculo.rect.left and antman_sprite.rect.left < obstaculo.rect.left:
                            antman_sprite.rect.right = obstaculo.rect.left
                        elif antman_sprite.rect.left < obstaculo.rect.right and antman_sprite.rect.right > obstaculo.rect.right:
                            antman_sprite.rect.left = obstaculo.rect.right
                        elif antman_sprite.rect.bottom > obstaculo.rect.top and antman_sprite.rect.top < obstaculo.rect.top:
                            antman_sprite.rect.bottom = obstaculo.rect.top
                        elif antman_sprite.rect.top < obstaculo.rect.bottom and antman_sprite.rect.bottom > obstaculo.rect.bottom:
                            antman_sprite.rect.top = obstaculo.rect.bottom

        for obstaculo in self.obstaculo_group:
            if self.pacman_sprite.rect.colliderect(obstaculo.rect):
                if obstaculo.cor == ROXO:
                    pass
                else:
                    if self.pacman_sprite.rect.right > obstaculo.rect.left and self.pacman_sprite.rect.left < obstaculo.rect.left:
                        self.pacman_sprite.rect.right = obstaculo.rect.left
                    elif self.pacman_sprite.rect.left < obstaculo.rect.right and self.pacman_sprite.rect.right > obstaculo.rect.right:
                        self.pacman_sprite.rect.left = obstaculo.rect.right
                    elif self.pacman_sprite.rect.bottom > obstaculo.rect.top and self.pacman_sprite.rect.top < obstaculo.rect.top:
                        self.pacman_sprite.rect.bottom = obstaculo.rect.top
                    elif self.pacman_sprite.rect.top < obstaculo.rect.bottom and self.pacman_sprite.rect.bottom > obstaculo.rect.bottom:
                        self.pacman_sprite.rect.top = obstaculo.rect.bottom

        for obstaculo in self.obstaculo_group:
            if self.comida_sprite.rect.colliderect(obstaculo.rect):
                    self.comida_group.add(self.comida_sprite)
                    self.comida_sprite.atualizar_posicao()  

        #Verifica colisões com a comida
        colisao_comida = pygame.sprite.spritecollide(self.pacman_sprite, self.comida_group, True)

        if colisao_comida:  
            self.contador_colisoes += 1  
            if self.contador_colisoes % CONST_DIFICULDADE == 0:  
                antman_sprite = Antman(self.sprite_sheet_pacman)
                antman_sprite.rect.topleft = (random.randint(0, LARGURA), random.randint(0, ALTURA))  
                self.antman_group.add(antman_sprite) 
            
            #ciominda em nova posição
            self.comida_group.add(self.comida_sprite)
            self.comida_sprite.atualizar_posicao()  

        colisao_antman = pygame.sprite.spritecollide(self.pacman_sprite, self.antman_group, True)

        if colisao_antman:
            self.game_over = True

    def desenhar_tela_imagen_texto(self, image,text):
        
        self.tela.blit(image, (LARGURA/2-image.get_width()/2,ALTURA/2-image.get_height()/2))
        texto = self.fonte.render(f'{text}',True, self.color_fonte_tela_inicial)
        self.tela.blit(texto, (LARGURA/2-texto.get_width()/2,ALTURA/2-texto.get_height()/2+90))
        if self.color_fonte_tela_inicial == PRETO and time.time() - self.inicio >= 1:
            self.color_fonte_tela_inicial = BRANCO
            self.inicio = time.time()
        elif self.color_fonte_tela_inicial == BRANCO and time.time() - self.inicio >= 1:
            self.color_fonte_tela_inicial = PRETO
            self.inicio = time.time()
    
    def executar(self):
  
        while self.run:
            self.relogio.tick(FPS)
            self.tela.fill(ROXO)

            if self.game_init == False:
                self.desenhar_tela_imagen_texto(image=self.pacman_logo,text="PRECIONE ESPAÇO PARA INICIAR O JOGO")
            elif self.game_over:
                
                self.desenhar()
                self.desenhar_tela_imagen_texto(image=self.pacman_logo,text="GAME OVER!!")
                self.iterar += 1
                if  self.iterar >= 240:
                    self.inicio = time.time()
                    self.game_over = False
                    self.game_init = False
                    self.iterar = 0
                    self.contador_colisoes = 0
            else:
                self.atualizar(event= event)
                self.verificar_colisoes()
                self.desenhar()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.inicio = time.time()
                        self.game_init = True
                if event.type == pygame.QUIT:
                    self.run = False

            

            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    creditos = Creditos()
    
    game.executar()
    creditos.executar()
