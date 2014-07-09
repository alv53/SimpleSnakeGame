import pygame

# Config
width = 800
height = 600

# Create the window
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption('Alvin\'s Test Game')
pygame.display.flip()


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
running = True

# Init speed of the snake, will increment after every number of food eaten
speed = 5

# Direction of the snake
# 1 = right
# 2 = down
# 3 = left
# 4 = up
d = 1 

# List to hold the snake
SnakeX = [300, 290, 280, 270]
SnakeY = [300, 300, 300, 300]

# a block represents a segment of the snake
block = pygame.Surface((10, 10))
block.fill((0, 200, 100))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
 # User pressed down on a key
	if event.type == pygame.KEYDOWN:
		# Figure out if it was an arrow key. If so
		# adjust speed.
		if event.key == pygame.K_LEFT:
			print "left"
		elif event.key == pygame.K_RIGHT:
			print "right"
		elif event.key == pygame.K_UP:
			print "up"
		elif event.key == pygame.K_DOWN:
			print "down"

	# Update snake's position

	# Drawing
	for x in range(len(SnakeX)):
		screen.blit(block, (SnakeX[x],SnakeY[x]))
	# Update
	pygame.display.flip()

	# 60 fps
	clock.tick(60)
pygame.quit()