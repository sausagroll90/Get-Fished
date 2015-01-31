import pygame
from Src.setup import *

class Gameloop:
	def __init__(self, screen, done, clock, player, backimg, viewport):
		self.screen = screen
		self.done = done
		self.clock = clock
		self.player = player
		self.backimg = backimg
		self.viewport = viewport
		self.dt = 0

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_d:
					self.player.speed += 30

	def do_updates(self):
		self.player.update(self.viewport, self.dt)
		self.viewport.update()

	def draw_to_screen(self):
		self.screen.fill((255, 255, 255))
		self.psurface = pygame.Surface((800, 600))
		self.psurface.blit(self.backimg, (self.viewport.x * -1, self.viewport.y * -1))
		self.screen.blit(self.psurface, (0, 0))
		self.player.draw(self.screen, self.viewport)
		pygame.display.flip()

	def main_loop(self):
		while not self.done:
			self.handle_events()
			self.do_updates()
			self.draw_to_screen()
			self.dt = self.clock.tick(40) / 1000