import pygame

from enum import Enum
import os

from constants import colors, window
from utils import KeyState, ThrottledUpdate, MenuList
from events import LOADGAME

from games import gamesList


class MenuState(Enum):
	START = 0
	GAMESELECT = 1

class Menu:
	def __init__(self, surface):

		self.surface = surface
		self.throttledUpdate = ThrottledUpdate()

		self.gotoStart()

		self.headerFont = pygame.font.Font('fonts/Roboto-Bold.ttf', self.getHeaderFontSize())
		self.headerSurf = self.headerFont.render('< R-Cade >', False, colors.WHITE)

		# Menu items
		self.startMenuList = MenuList(surface, options=[
			dict(title=u'Spela', action=self.gotoSelect),
			dict(title=u'Avsluta', action=self.quit)
		])
		self.gameSelectMenuList = MenuList(surface, options=self.getGameItems())

	def getHeaderFontSize(self):
		return int(window.SCREEN_HEIGHT * 0.15)

	def getGameItems(self):
		items = []
		for game in gamesList:
			items.append(dict(title=game.get('title', 'No name'), game=game, action=self.gotoGame))
		items.append(dict(title=u'<< Meny', action=self.gotoStart))
		return items

	def gotoStart(self):
		self.state = MenuState.START

	def gotoSelect(self):
		self.state = MenuState.GAMESELECT

	def gotoGame(self, item):
		e = pygame.event.Event(LOADGAME, game=item.get('game'))
		pygame.event.post(e)

	def quit(self):
		e = pygame.event.Event(pygame.locals.QUIT)
		pygame.event.post(e)

	def update(self, events):
		if self.state == MenuState.GAMESELECT:
			self.gameSelectMenuList.update(events)
		else:
			self.startMenuList.update(events)


	def draw(self):
		self.surface.fill(colors.BLACK) # Should this be placed in __init__ instead?

		# Draw header
		headerRect = self.headerSurf.get_rect(center=(window.SCREEN_WIDTH/2, self.getHeaderFontSize()))
		self.surface.blit(self.headerSurf, headerRect)

		# Draw items
		if self.state == MenuState.GAMESELECT:
			self.gameSelectMenuList.draw()
		else:
			self.startMenuList.draw()

