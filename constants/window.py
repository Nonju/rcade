import pygame

FPS = 30

_screen_info = pygame.display.Info()
SCREEN_WIDTH = min(_screen_info.current_w, 1024)
SCREEN_HEIGHT = min(_screen_info.current_h, 800)
