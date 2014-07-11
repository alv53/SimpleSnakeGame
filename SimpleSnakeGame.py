#!/usr/bin/python
import pygame, sys
from random import randint

# Helper functions
def GameOver(screen):
	print "Dead!"
	text = font.render("You Died", 1, (0,0,0))
	screen.blit(text, (100, 100))
	pygame.display.flip()
	pygame.time.wait(5000)
	sys.exit(0)

def Collision(x1, x2, y1, y2):
	return x1==x2 and y1==y2

# Config
width = 800
height = 600

# Create the window
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption('SimpleSnakeGame')
pygame.display.flip()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
running = True

# Init speed of the snake, will increment after every number of food eaten
# Not using yet...
speed = 5

# Direction of the snake
# 0 = right
# 1 = down
# 2 = left
# 3 = up
d = 0 

Score = 0

# List to hold the snake
SnakeX = [300, 290, 280, 270]
SnakeY = [300, 300, 300, 300]

# Variables to store food position
FoodX = 10*randint(0,width/10-1)
FoodY = 10*randint(0,height/10-1)

# a block represents a segment of the snake
block = pygame.Surface((10, 10))
block.fill((0,200,100))

# block for food
Food = pygame.Surface((10,10))
Food.fill((255,0,0))

pygame.init()
font = pygame.font.SysFont("monospace", 30)
while running:
	DirSet = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif not DirSet:
			if event.type == pygame.KEYDOWN:
				# Figure out if it was an arrow key. If so
				# adjust speed.
				if event.key == pygame.K_LEFT:
					if d != 0:
						d = 2
						DirSet = True
				elif event.key == pygame.K_RIGHT:
					if d != 2:
						d = 0
						DirSet = True
				elif event.key == pygame.K_UP:
					if d != 1:
						d = 3
						DirSet = True
				elif event.key == pygame.K_DOWN:
					if d != 3:
						d = 1
						DirSet = True
	screen.fill((255,255,255))

	# Check for collisions
	if Collision(SnakeX[0], FoodX, SnakeY[0], FoodY):
		Score+=10
		SnakeX.append(0)
		SnakeY.append(0)
		FoodX = 10*randint(0,width/10)
		FoodY = 10*randint(0,height/10)
	# Calculate new head location
	if d == 0: 		#right
		NewHeadX = SnakeX[0] + 10
		NewHeadY = SnakeY[0]
	elif d == 1: 	#down
		NewHeadX = SnakeX[0]
		NewHeadY = SnakeY[0] + 10
	elif d == 2: 	#left
		NewHeadX = SnakeX[0] - 10
		NewHeadY = SnakeY[0]
	else: 			#up
		NewHeadX = SnakeX[0]
		NewHeadY = SnakeY[0] - 10

	# Update snake's body position
	x = len(SnakeX)-1
	while x > 0:
		SnakeX[x] = SnakeX[x-1]
		SnakeY[x] = SnakeY[x-1]
		# Check if the current block collides with the new head
		if Collision(SnakeX[x], NewHeadX, SnakeY[x], NewHeadY):
			print "%d: %d, %d, %d, %d" % (x, SnakeX[x], NewHeadX, SnakeY[x], NewHeadY)
			GameOver(screen)
		x-=1

	# Update head
	SnakeX[0] = NewHeadX
	SnakeY[0] = NewHeadY

	# Check for out of bounds
	if SnakeX[0] < 0 or SnakeX[0] >= width or SnakeY[0] < 0 or SnakeY[0] >= height:
		GameOver(screen)

	# Drawing the snake
	for x in range(len(SnakeX)):
		screen.blit(block, (SnakeX[x],SnakeY[x]))

	print (FoodX, FoodY)
	screen.blit(Food, (FoodX, FoodY))
	text = font.render("Score: %d" % Score, 1, (0,0,0))
	screen.blit(text, (10, 10))
	# Update
	pygame.display.flip()

	clock.tick(10)
pygame.quit()