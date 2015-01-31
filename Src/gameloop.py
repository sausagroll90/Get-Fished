import pygame
from Src.setup import *

class Gameloop:
	def __init__(self, screen, done, clock, player):
		self.screen = screen
		self.done = done
		self.clock = clock
		self.player = player
		self.xoffset = 0
		self.yoffset = 0

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True

	def do_updates(self):
		keylist = pygame.key.get_pressed()

		if keylist[pygame.K_a]:
			if self.player.x != 400 and self.player.x > 0:
				self.player.x -= 5
			elif self.xoffset >= 0 and self.player.x > 0:
				self.player.x -= 5
			else:
				if self.xoffset < 0:
				 self.xoffset += 5

		if keylist[pygame.K_d]:
			if self.player.x != 400 and self.player.x < 800:
				self.player.x += 5
			elif self.xoffset <= -800 and self.player.x < 800:
				self.player.x += 5
			else:
				if self.xoffset > -800:
					self.xoffset -= 5

		if keylist[pygame.K_w]:
			if self.player.y != 300 and self.player.y > 0:
				self.player.y -= 5
			elif self.yoffset >= 0 and self.player.y > 0:
				self.player.y -= 5
			else:
				if self.yoffset < 0:
				 self.yoffset += 5

		if keylist[pygame.K_s]:
			if self.player.y != 300 and self.player.y < 600:
				self.player.y += 5
			elif self.yoffset <= -600 and self.player.y < 600:
				self.player.y += 5
			else:
				if self.yoffset > -600:
					self.yoffset -= 5



	def draw_to_screen(self):
		self.screen.fill((255, 255, 255))
		pygame.draw.rect(self.screen, (0, 0, 0), (0 + self.xoffset, 0 + self.yoffset, 1600, 1200), 1)
		self.player.draw(self.screen)
		pygame.display.flip()

	def main_loop(self):
		while not self.done:
			self.handle_events()
			self.do_updates()
			self.draw_to_screen()
			self.clock.tick(60)