import pygame

pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Tela de Análise')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 18)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Caminhão 1', True, black)

text1 = font.render('Caminhão 2', True, black)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()
text1Rect = text.get_rect()

# set the center of the rectangular object.
textRect.topleft = (10, X - 390)
text1Rect.topleft = (10, X - 370)

# infinite loop
while True:

	# completely fill the surface object
	# with white color
	display_surface.fill(white)

	# copying the text surface object
	# to the display surface object
	display_surface.blit(text, textRect)
	display_surface.blit(text1, text1Rect)

	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():

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
