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
# 0 = right
# 1 = down
# 2 = left
# 3 = up
d = 0 

# List to hold the snake
SnakeX = [300, 290, 280, 270]
SnakeY = [300, 300, 300, 300]

# a block represents a segment of the snake
block = pygame.Surface((10, 10))
block.fill((0,200,100))
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			# Figure out if it was an arrow key. If so
			# adjust speed.
			if event.key == pygame.K_LEFT:
				print "left"
				if d != 0:
					d = 2
			elif event.key == pygame.K_RIGHT:
				print "right"
				if d != 2:
					d = 0
			elif event.key == pygame.K_UP:
				print "up"
				if d != 1:
					d = 3
			elif event.key == pygame.K_DOWN:
				print "down"
				if d != 3:
					d = 1

	screen.fill((255,255,255))

	# Update snake's position
	x = len(SnakeX)-1
	while x > 0:
		SnakeX[x] = SnakeX[x-1]
		SnakeY[x] = SnakeY[x-1]
		x-=1

	if d == 0: 		#right
		SnakeX[0] = SnakeX[1] + 10
		SnakeY[0] = SnakeY[1]
	elif d == 1: 	#down
		SnakeX[0] = SnakeX[1]
		SnakeY[0] = SnakeY[1] + 10
	elif d == 2: 	#left
		SnakeX[0] = SnakeX[1] - 10
		SnakeY[0] = SnakeY[1]
	else: 			#up
		SnakeX[0] = SnakeX[1]
		SnakeY[0] = SnakeY[1] - 10
	
	# Drawing
	print SnakeX
	print SnakeY
	print "\n"

	for x in range(len(SnakeX)):
		screen.blit(block, (SnakeX[x],SnakeY[x]))
	# Update
	pygame.display.flip()

	# 60 fps
	clock.tick(10)
# pygame.quit()