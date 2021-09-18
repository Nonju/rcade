import pygame
from pygame.locals import QUIT

# Init
pygame.init()

import sys
from enum import Enum

from constants import colors
from constants.window import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from menu import Menu
from utils import KeyState, ControllerState, Delay
from events import LOADGAME, GOTOMAINMENU

# Screen
FramePerSec = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(colors.BLACK)
pygame.display.set_caption('R-Cade')

# Init controller support
ControllerState.init()

# Init global delay utility
Delay.init()

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
			elif event.type == LOADGAME:
				if event.game.get('cls'):
					game = event.game['cls'](DISPLAYSURF)
				state = MainState.GAME
			elif event.type == GOTOMAINMENU:
				game = None,
				state = MainState.MENU

		if state == MainState.GAME and game:
			game.update(events)
			game.draw()
		elif state == MainState.MENU:
			menu.update(events)
			menu.draw()
		else:
			# Revert to menu on state exception
			state = MainState.MENU

		# Update utility
		KeyState.update(events)
		Delay.update(events)

		# Update screen
		pygame.display.update()
		FramePerSec.tick(FPS)


if __name__ == '__main__':
	main()
