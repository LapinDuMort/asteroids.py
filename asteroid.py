import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)	
		

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity*dt
#logic for killing small asteroids or splitting larger asteroids
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		elif self.radius > ASTEROID_MIN_RADIUS:
			angle = random.uniform(20, 50)
			random_angle = self.velocity.rotate(angle)
			minus_random_angle = self.velocity.rotate(-angle)
			new_rad = int(self.radius - ASTEROID_MIN_RADIUS)
			new_asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
			new_asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
			new_asteroid1.velocity = random_angle * 1.2
			new_asteroid2.velocity = minus_random_angle * 1.2
