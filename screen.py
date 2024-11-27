import pygame
import threading
from threads import Entradas
from classes.encomenda import StatusEncomenda, Encomenda

def localizar_encomenda(encomenda: Encomenda):
	
	if encomenda.status is StatusEncomenda.PRODUZIDA:
		return f'<- Centro de Distribuicao {encomenda.origem}'

	if encomenda.status is StatusEncomenda.ENTREGUE:
		return f'-> Centro de Distribuicao {encomenda.destino}'
	
	if encomenda.status is StatusEncomenda.TRANSPORTE:
		return f'-- Caminhao {encomenda.nome_caminhao}'
	
	if encomenda.status is StatusEncomenda.CARREGADA:
		return f'-> Caminhao {encomenda.nome_caminhao}'
	
	if encomenda.status is StatusEncomenda.DESPACHE:
		return f'<- Caminhao {encomenda.nome_caminhao}'
	


pygame.init()

# Cores em RGB
white = (200, 200, 200)
black = (0, 0, 0)
green = (0, 63, 0)
blue = (0, 0, 128)
brown = (60, 30, 0)

# Tamanho da tela
X = 600
Y = 600

# Criacao da tela
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Tela de Acompanhamento')

# Definicao de fonte e tamanho
font = pygame.font.Font('freesansbold.ttf', 18)

# Escrita dos textos

entrada = Entradas(3,4,100,5)

text_encomendas = [None for _ in range(entrada.P)]

posicao_vertical_anterior = -1
posicao_vertical = 0
posicao_horizontal = 0

encomenda = Encomenda(1,2,"Feijao", 7)

# infinite loop
while True:


	# completely fill the surface object
	# with white color
	display_surface.fill(brown)

	# copying the text surface object
	# to the display surface object
	if posicao_vertical<0:
		posicao_vertical = 0

	if posicao_horizontal>0:
		posicao_horizontal = 0

	for i in range(posicao_vertical, posicao_vertical+20):
		if i < entrada.P:

			if posicao_vertical != posicao_vertical_anterior:

				extra = localizar_encomenda(encomenda)
				text = font.render(f'Encomenda {i}:  {encomenda.status.value}    {extra}', True, white)
				text_encomendas[i] = text
			display_surface.blit(text_encomendas[i], (10 + posicao_horizontal * 50, 5 + (i-posicao_vertical)*30))
	

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_DOWN:
				posicao_vertical_anterior = posicao_vertical
				posicao_vertical += 1
			if event.key == pygame.K_UP:
				posicao_vertical_anterior = posicao_vertical
				posicao_vertical -= 1
			if event.key == pygame.K_LEFT:
				posicao_horizontal +=1
			if event.key == pygame.K_RIGHT:
				posicao_horizontal -=1

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:

			# deactivates the pygame library
			pygame.quit()

			# quit the program.
			quit()

		# Draws the surface object to the screen.
		pygame.display.update()
