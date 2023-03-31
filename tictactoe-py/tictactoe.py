# Simples programa pygame
 
# Importar o módulo pygame
import pygame
pygame.init()
 
# Construindo a Janela
screen = pygame.display.set_mode([500, 500])
 
# Executar até que o usuário peça para sair (loop do jogo)
running = True
while running:
	# O usuário clicou no botão Fechar Janela?
	for event in pygame.event.get():
 
		if event.type == pygame.QUIT:
			running = False
 
    # Plano de Fundo Branco
	screen.fill((255, 255, 255))
 
    # Desenhar um círculo azul no centro
	pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
 
    # Atualizar a Tela
	pygame.display.flip()
 
# Pronto! Hora de sair.
pygame.quit()