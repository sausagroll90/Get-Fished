import pygame

class Fish:
	def __init__(self):
		self.x = 400
		self.y = 300

	def draw(self, screen):
		pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 3, 0)