import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
# Initialise main function and pygame, setting the screen variable equal to HxW of screen
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#  Create containers for different elements
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
# Terminal messages
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
#Capping frames with Delta Time
	clock = pygame.time.Clock()
	dt = 0
# Create a player object
	player_rad = PLAYER_RADIUS
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, player_rad, shots_group)
#Initialise the asteroid field
	asteroidfield = AsteroidField()

# Game Loop
	while True:
		screen.fill((0,0,0))
		for drawing in drawable:
			drawing.draw(screen)
		updatable.update(dt)
#Check if player collides with asteroid
		for i in asteroids:
			if i.collision(player) == True:
				sys.exit("Game over!")
#update timer for shots
		shots_group.update(dt)
#draw shots when added to group
		for shot in shots_group:
			pygame.draw.circle(screen, (255,255,255), (int(shot.position.x), int(shot.position.y)), shot.radius)
#check if bullet collides with asteroid, remove bullet and split/kill asteroid
		for bullet in shots_group:
			for ast in asteroids:
				if bullet.collision(ast) == True:
					ast.split()
					bullet.kill()

		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				return

		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
