import pygame

# Define some colors
BLACK	= (   0,   0,   0)
WHITE	= ( 255, 255, 255)
GREEN	= (   0, 255,   0)
RED	  = ( 255,   0,   0)

# Config options
(width, height) = (700, 500)

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Alvin\'s Test Game')
pygame.display.flip()


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
running = True
x = 300
y = 200
x_speed = 10
y_speed = 0
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
 # User pressed down on a key
	if event.type == pygame.KEYDOWN:
		# Figure out if it was an arrow key. If so
		# adjust speed.
		if event.key == pygame.K_LEFT:
			if not x_speed > 0:
				x_speed = -10
				y_speed = 0
		if event.key == pygame.K_RIGHT:
			if not x_speed < 0:
				x_speed = 10
				y_speed = 0
		if event.key == pygame.K_UP:
			if not y_speed > 0:
				y_speed = -10
				x_speed = 0
		if event.key == pygame.K_DOWN:
			if not y_speed < 0:
				y_speed = 10
				x_speed = 0
				


	# Drawing
	screen.fill(WHITE)
	x += x_speed
	y += y_speed
	pygame.draw.rect(screen, RED, [x, y, 10, 10])
	
	# Update
	pygame.display.flip()

	# 60 fps
	clock.tick(60)
pygame.quit()