import os

DIRETORIO = os.path.dirname(__file__)
DIRETORIO_IMAGENS = os.path.join(DIRETORIO, 'imagens')
DIRETORIO_SONS = os.path.join(DIRETORIO, 'sons')
FONTE_SIZE =   36


FPS = 60
CONST_DIFICULDADE = 3

COMIDA_TUPLE =  (99/2, 99/2)
PACMAN_TUPLE = (32, 31)
PACMAN_ESCALE = 1.2
PACMAN_ESPESSURA = 60
ESPESSURA = 10*2.5
LARGURA =720
ALTURA = (13*PACMAN_ESPESSURA)+(ESPESSURA*2)

AZUL = (0,0,50) 
ROXO =  (164,76,163) 
BRANCO = (255,255,255)
PRETO = (0,0,0)

CREDITOS = [
"CREDITOS FINAIS",
" ",
"EMERSON - Cordenador de Atividades, Desenvovimento do jogo, Desenvovimento do ipynb ", 
"FILIPE - Pesquisa matemática, Desenvovimento do ipynb, Conclusão do relatrorio",
"DAVI PEREIRA - Relatorio: referências,Relatorio: discussão,Relatorio: análise de Resultados",
"Daniel Vítor Alves -Relatorio: dados coletados, Relatorio: equipamentos utilizados, Relatorio: objetivos",
" ",
" ",
"Agradecimento Especial à Equipe",
"Gostaria de expressar minha profunda gratidão a toda a equipe envolvida no projeto.",
"Seu empenho, dedicação e expertise foram fundamentais para entregarmos um excelente resultado.",
"Agradeço por cada contribuição, ideia inovadora e suporte técnico oferecido.",
"Foi inspirador testemunhar a paixão e entusiasmo de cada membro da equipe.",
"Obrigado por fazerem desta jornada uma experiência memorável e gratificante.",
"Com sincero apreço",
"Emerson Siva"
]
