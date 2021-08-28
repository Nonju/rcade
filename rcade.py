import pygame
from pygame.locals import *

import sys
from enum import Enum

from constants import colors
from menu import Menu
from utils.keystate import KeyState

# Init
pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()


# Screen
screen_info = pygame.display.Info()
SCREEN_WIDTH = min(screen_info.current_w, 1024)
SCREEN_HEIGHT = min(screen_info.current_h, 800)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(colors.BLACK)
pygame.display.set_caption('R-Cade')


class MainState(Enum):
	MENU = 0
	GAME = 1

def main():
	state = MainState.MENU
	menu = Menu(DISPLAYSURF)
	game = None

	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if state == MainState.GAME and game:
			game.update()
			game.draw()
		elif state == MainState.MENU:
			menu.update()
			menu.draw()
		else:
			# Revert to menu on state exception
			state = MainState.MENU

		KeyState.update(events)

		pygame.display.update()
		FramePerSec.tick(FPS)

if __name__ == '__main__':
	main()
