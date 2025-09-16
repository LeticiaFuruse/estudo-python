import pygame 

# inicializaçõa
pygame.init()
tela = pygame.display.set_mode((800, 600))
relogio = pygame.time.Clock()

# jogador
jogador_pos = [400, 500]
jogador_vel = 5 


# loop do jogo
rodando = True 
# processar eventos
while rodando:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            rodando = False
            
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_pos[0] -= jogador_vel
    if teclas[pygame.K_RIGHT]:
        jogador_pos[0] += jogador_vel
    if teclas[pygame.K_UP]:
        jogador_pos[1] -= jogador_vel
    if teclas[pygame.K_DOWN]:
        jogador_pos[1] += jogador_vel
    

    # renderizar 
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0),(jogador_pos[0], jogador_pos[1], 50, 50)) 
    pygame.display.update()
    relogio.tick(60)

pygame.quit()