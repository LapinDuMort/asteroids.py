from circleshape import *
import pygame
from constants import *
from main import *
from shot import *

class Player(CircleShape):

	def __init__(self, x, y, PLAYER_RADIUS, shots_group) :
		super().__init__(x, y, PLAYER_RADIUS)
		self.shots = shots_group
		self.rotation = 0
		self.radius = PLAYER_RADIUS
		self.cooldown = 0
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
	
	def rotate(self, dt):
		self.rotation = self.rotation + PLAYER_TURN_SPEED * dt


	def update(self, dt):
		keys = pygame.key.get_pressed()
		if self.cooldown > 0 and self.cooldown >= dt:
			self.cooldown -= dt
		elif self.cooldown > 0 and self.cooldown < dt:
			self.cooldown = 0
		else:
			pass
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			if self.cooldown == 0:
				self.shoot()
				self.cooldown = PLAYER_SHOOT_COOLDOWN
			elif self.cooldown > 0:
				pass

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
#create a new shot
		new_shot = Shot(self.position.x, self.position.y)
#set velocity of shot
		velocity = pygame.Vector2(0, 1)
		velocity = velocity.rotate(self.rotation)
		velocity = velocity *  PLAYER_SHOOT_SPEED
		new_shot.velocity = velocity
#add shot to shots group
		self.shots.add(new_shot)
		
