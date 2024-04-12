from pygame.locals import *
from constantes import *
from sprites import *


CONTORNO = [
    #CONTORNO
    {"cor": AZUL, "largura": LARGURA, "altura": ESPESSURA/2.5, "coordenadas": (0, 0)},
    {"cor": AZUL, "largura": ESPESSURA/2.5, "altura": ALTURA, "coordenadas": (0, 0)},
    {"cor": AZUL, "largura": LARGURA, "altura": ESPESSURA/2.5, "coordenadas": (0, ALTURA-ESPESSURA/2.5)},
    {"cor": AZUL, "largura":ESPESSURA/2.5, "altura": ALTURA, "coordenadas": (LARGURA-ESPESSURA/2.5, 0)},
]

def rotacionar_180_graus(obstaculos, largura_labirinto, altura_labirinto):
    obstaculos_rotacionados = []

    for obstaculo in obstaculos:
        cor = obstaculo["cor"]
        largura = obstaculo["largura"]
        altura = obstaculo["altura"]
        x, y = obstaculo["coordenadas"]
        x_rotacionado = largura_labirinto - x - largura
        y_rotacionado = altura_labirinto - y - altura

        obstaculo_rotacionado = {"cor": cor, "largura": largura, "altura": altura, "coordenadas": (x_rotacionado, y_rotacionado)}
        obstaculos_rotacionados.append(obstaculo_rotacionado)

    return obstaculos_rotacionados

largura_labirinto = LARGURA
altura_labirinto = ALTURA   

PRIMEIRO_BLOCO = [
    

    #OBSTACULOS(1 E 2 QUADRANTES)
    {"cor": AZUL, "largura":PACMAN_ESPESSURA, "altura": PACMAN_ESPESSURA, "coordenadas": (PACMAN_ESPESSURA, PACMAN_ESPESSURA)},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": PACMAN_ESPESSURA, "coordenadas": (PACMAN_ESPESSURA*3, PACMAN_ESPESSURA)},
    {"cor": AZUL, "largura":ESPESSURA, "altura": PACMAN_ESPESSURA*2, "coordenadas": (int(LARGURA/2)-ESPESSURA/2.5, 0)},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": PACMAN_ESPESSURA, "coordenadas": (int(LARGURA/2)+ESPESSURA/2.5+PACMAN_ESPESSURA, PACMAN_ESPESSURA)},
     {"cor": AZUL, "largura":PACMAN_ESPESSURA, "altura": PACMAN_ESPESSURA, "coordenadas": (int(LARGURA/2)+ESPESSURA/2.5+(PACMAN_ESPESSURA*4), PACMAN_ESPESSURA)},
    
    #OBSTACULOS(3 E 4 QUADRANTES)
    {"cor": AZUL, "largura":PACMAN_ESPESSURA, "altura": ESPESSURA, "coordenadas": (PACMAN_ESPESSURA, PACMAN_ESPESSURA*3)},
    {"cor": AZUL, "largura":ESPESSURA, "altura": ESPESSURA+(PACMAN_ESPESSURA*3), "coordenadas": (PACMAN_ESPESSURA*3, PACMAN_ESPESSURA*3)},
    {"cor": AZUL, "largura":(3*PACMAN_ESPESSURA)+ESPESSURA, "altura": ESPESSURA, "coordenadas": (ESPESSURA+(PACMAN_ESPESSURA*4), PACMAN_ESPESSURA*3)},
    {"cor": AZUL, "largura":ESPESSURA, "altura": PACMAN_ESPESSURA+ESPESSURA, "coordenadas": (int(LARGURA/2)-ESPESSURA/2.5, PACMAN_ESPESSURA*3)},
    {"cor": AZUL, "largura":ESPESSURA, "altura": ESPESSURA+(PACMAN_ESPESSURA*3), "coordenadas": ((int(LARGURA/2)+(ESPESSURA/2.5)+(PACMAN_ESPESSURA*2.5)), PACMAN_ESPESSURA*3)},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA, "altura": ESPESSURA, "coordenadas": (int(LARGURA/2)+(ESPESSURA/2.5)+(PACMAN_ESPESSURA*3.5)+ESPESSURA, PACMAN_ESPESSURA*3)},

    #OBSTACULOS(5 E 6 QUADRANTES)
   {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": PACMAN_ESPESSURA*2, "coordenadas": (0, (PACMAN_ESPESSURA*4)+ESPESSURA)},
   {"cor": AZUL, "largura":ESPESSURA, "altura": PACMAN_ESPESSURA*2, "coordenadas": ((PACMAN_ESPESSURA*2)-ESPESSURA, (PACMAN_ESPESSURA*4)+ESPESSURA)},
   {"cor": AZUL, "largura":PACMAN_ESPESSURA+ESPESSURA*2, "altura": ESPESSURA, "coordenadas": ((PACMAN_ESPESSURA*3), (PACMAN_ESPESSURA*4)+ESPESSURA)},
   {"cor": AZUL, "largura":PACMAN_ESPESSURA+ESPESSURA*2, "altura": ESPESSURA, "coordenadas": (int(LARGURA/2)+(ESPESSURA/2.5)+PACMAN_ESPESSURA, (PACMAN_ESPESSURA*4)+ESPESSURA)},
    {"cor": AZUL, "largura":ESPESSURA, "altura": PACMAN_ESPESSURA*2, "coordenadas": ((int(LARGURA/2)+(ESPESSURA/2.5)+PACMAN_ESPESSURA)+(PACMAN_ESPESSURA+ESPESSURA*2)+PACMAN_ESPESSURA, (PACMAN_ESPESSURA*4)+ESPESSURA)},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": PACMAN_ESPESSURA*2, "coordenadas": ((int(LARGURA/2)+(ESPESSURA/2.5)+PACMAN_ESPESSURA)+(PACMAN_ESPESSURA+ESPESSURA*2)+PACMAN_ESPESSURA, (PACMAN_ESPESSURA*4)+ESPESSURA)},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": ESPESSURA, "coordenadas": (0, (PACMAN_ESPESSURA*6))},
    {"cor": AZUL, "largura":PACMAN_ESPESSURA*2, "altura": ESPESSURA, "coordenadas": ((int(LARGURA/2)+(ESPESSURA/2.5)+PACMAN_ESPESSURA)+(PACMAN_ESPESSURA+ESPESSURA*2)+PACMAN_ESPESSURA, (PACMAN_ESPESSURA*6))},
    {"cor": AZUL, "largura":(PACMAN_ESPESSURA*2)+(ESPESSURA*3), "altura": ESPESSURA, "coordenadas": (PACMAN_ESPESSURA*4+ESPESSURA, (PACMAN_ESPESSURA*6))},
]

SEGUNDO_BLOCO = rotacionar_180_graus(PRIMEIRO_BLOCO, largura_labirinto, altura_labirinto)