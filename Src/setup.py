import pygame
import Src.fish
import Src.gameloop
import Src.viewport

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Get Fished")
clock = pygame.time.Clock()

fishimg = pygame.image.load("Resources/player.png")
backimg = pygame.image.load("Resources/background.png")

viewport = Src.viewport.Viewport()
player = Src.fish.Fish(fishimg)
mainloop = Src.gameloop.Gameloop(screen, False, clock, player, backimg, viewport)