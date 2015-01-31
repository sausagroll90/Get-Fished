import pygame
from Src.setup import *

class Fish:
	def __init__(self, img):
		self.x = 400
		self.y = 300
		self.direction = pygame.math.Vector2(1, 0)
		self.speed = 200
		self.img = img

	def inputs(self, dt):
		self.keylist = pygame.key.get_pressed()

		if self.keylist[pygame.K_a]:
			self.direction.rotate_ip(round(300 * dt))

		if self.keylist[pygame.K_d]:
			self.direction.rotate_ip(round(-300 * dt))

	def update(self, viewport, dt):
		self.inputs(dt)

		self.speed *= 0.99
		
		self.dx = self.direction.x * self.speed
		self.dy = self.direction.y * self.speed

		if self.x < 0:
			self.dx = 0
			self.x = 0
		elif self.x > 1600:
			self.dx = 0
			self.x = 1600

		if self.y < 0:
			self.dy = 0
			self.y = 0
		elif self.y > 1200:
			self.dy = 0
			self.y = 1200

		self.x += self.dx * dt
		self.y -= self.dy * dt

		self.x = round(self.x)
		self.y = round(self.y)

		if 400 <= self.x <= 1200:
			viewport.x = self.x - 400
			
		if 300 <= self.y <= 900:
			viewport.y = self.y - 300

	def draw(self, screen, viewport):
		screen.blit(pygame.transform.rotate(self.img, self.direction.as_polar()[1]), ((self.x - viewport.x) - 25, (self.y - viewport.y) - 15))