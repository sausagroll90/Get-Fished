import pygame
import Src.fish

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Get Fished")
clock = pygame.time.Clock()

player = Src.fish.Fish()