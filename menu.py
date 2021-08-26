import pygame
from pygame.locals import *
from sys import exit
from Labirinto import *

screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
pygame.init()
menu_selection = 1
ALTURA = 600
LARGURA = 800
botao_enter = False
WHITE = (255, 255, 255)
pygame.display.set_caption('Labirinto')
background = pygame.image.load("bg.jfif")
background = pygame.transform.scale(background,(800,600))
logo = pygame.image.load('logo.jfif').convert_alpha()
logo = pygame.transform.scale(logo,(200,200))


def selecao():
    global menu_selection, botao_enter
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                menu_selection += 1
            if event.key == K_UP:
                menu_selection -= 1
            if event.key == K_SPACE or event.key == K_RETURN:
                menu_selection += 10
            if event.key == K_ESCAPE:
                if menu_selection == 1 or menu_selection == 2:
                    pygame.quit()
                else:
                    menu_selection -= 10


def eventos():
    screen.fill((0, 0, 0))
    global menu_selection, botao_enter

    if menu_selection == 1:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(logo,(305,50))

        fonte = pygame.font.SysFont("Arial", 30, False, False)
        novo_jogo = fonte.render('> Novo Jogo <', True, WHITE)
        novo_jogo_rect = novo_jogo.get_rect(center=(LARGURA/2, ALTURA/2))
        screen.blit(novo_jogo, (novo_jogo_rect))

        fonte = pygame.font.SysFont("Arial", 30, False, False)
        creditos = fonte.render('Creditos', True, WHITE)
        creditos_rect = creditos.get_rect(center=(LARGURA/2, (ALTURA+100)/2))
        screen.blit(creditos, creditos_rect)


    if menu_selection == 2:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(logo,(305,50))
        fonte = pygame.font.SysFont("Arial", 30, False, False)
        novo_jogo = fonte.render('Novo Jogo', True, WHITE)
        novo_jogo_rect = novo_jogo.get_rect(center=(LARGURA/2, ALTURA/2))
        screen.blit(novo_jogo, (novo_jogo_rect))

        fonte = pygame.font.SysFont("Arial", 30, False, False)
        creditos = fonte.render('> Creditos <', True, WHITE)
        creditos_rect = creditos.get_rect(center=(LARGURA/2, (ALTURA+100)/2))
        screen.blit(creditos, creditos_rect)

    if menu_selection == 3:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(logo,(305,50))
        menu_selection = 1
    if menu_selection == 0:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(logo,(305,50))
        menu_selection = 2
    if menu_selection == 399:
        menu_selection = 400
    if menu_selection == 401:
        menu_selection = 400


    if menu_selection == 400:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))



        fonte = pygame.font.SysFont("Arial", 40 ,False, False)
        fonte_criador = pygame.font.SysFont("Besley",30,False,False)
        fonte_render = fonte.render("Criadores:",True, (255,255,255))
        fonte_back = pygame.font.SysFont("Arial",20,False,False)
        criador1 = fonte_criador.render("Bruno Guilherme da Silva", True, (255,255,255))
        criador2 = fonte_criador.render("Filipe Fernando da Silva Balbino", True, (255,255,255))
        criador3 = fonte_criador.render("João Victor Soares Ferreira", True, (255,255,255))
        criador4 = fonte_criador.render("Leonardo Canuto de Oliveira Magalhães", True, (255,255,255))
        criador5 = fonte_criador.render("Mártison José Bernado da Silva", True, (255,255,255))
        criador6 = fonte_criador.render("Theo Hebert Camargo Perman",True,(255,255,255))
        screen.blit(fonte_render,(100, 100))
        screen.blit(criador1, (200, 220))
        screen.blit(criador2, (200, 250))
        screen.blit(criador3, (200, 280))
        screen.blit(criador4, (200, 310))
        screen.blit(criador5, (200, 340))
        screen.blit(criador6,(200,370))
        voltar_render = fonte_back.render("> Voltar <",True, (255,255,255))
        screen.blit(voltar_render,(600,500))
    if menu_selection == 410:
        menu_selection = 2
    if menu_selection > 400:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        menu_selection = 400

    if menu_selection == 11:
        menu_selection = 1
        main()

    if menu_selection == 12:
        menu_selection = 400
    if menu_selection == 390:
        menu_selection = 1




while True:
    clock.tick(30)
    selecao()
    eventos()

    pygame.display.update()
