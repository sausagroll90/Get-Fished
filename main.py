import pygame
from Src.setup import *
import Src.gameloop

mainloop = Src.gameloop.Gameloop(screen, False, clock)

mainloop.main_loop()

pygame.quit()