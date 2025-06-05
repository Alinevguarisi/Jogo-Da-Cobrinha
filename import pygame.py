import pygame
import time
import random

# Inicialização
pygame.init()

# Tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
azul_claro = (173, 216, 230)
verde_escuro = (0, 155, 0)
vermelho = (200, 0, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)
comida_cor = (255, 100, 100)

# Configurações
tamanho_bloco = 20
velocidade = 15
clock = pygame.time.Clock()

# Fonte
fonte = pygame.font.SysFont("arial", 28, bold=True)

def desenha_cobra(lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde_escuro, [x[0], x[1], tamanho_bloco, tamanho_bloco], border_radius=4)

def mostrar_mensagem(texto, cor, deslocamento_y=0):
    texto_renderizado = fonte.render(texto, True, cor)
    texto_rect = texto_renderizado.get_rect(center=(largura / 2, altura / 2 + deslocamento_y))
    tela.blit(texto_renderizado, texto_rect)

def jogo():
    game_over = False
    game_close = False

    x1 = largura // 2
    y1 = altura // 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not game_over:

        while game_close:
            tela.fill(azul_claro)
            mostrar_mensagem("Você perdeu!", vermelho, -30)
            mostrar_mensagem("Pressione C para continuar ou Q para sair", preto, 30)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        x1 += x1_mudanca
        y1 += y1_mudanca

        if x1 < 0 or x1 >= largura or y1 < 0 or y1 >= altura:
            game_close = True

        tela.fill(azul_claro)
        pygame.draw.rect(tela, comida_cor, [comida_x, comida_y, tamanho_bloco, tamanho_bloco], border_radius=4)

        cabeca = [x1, y1]
        lista_cobra.append(cabeca)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca:
                game_close = True

        desenha_cobra(lista_cobra)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()
