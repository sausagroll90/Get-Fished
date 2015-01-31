import pygame
from Src.setup import *

class Viewport:
	def __init__(self):
		self.rect = pygame.Rect(0, 0, 800, 600)
		self.x = 0
		self.y = 0

	def update(self):
		self.rect = pygame.Rect(self.x, self.y, 800, 600)

	def draw(self, screen):
		screen.blit(screen, backimg, self.rect)