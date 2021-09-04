import pygame

from enum import Enum
import os

from constants import colors
from utils.keystate import KeyState
from utils import ThrottledUpdate
from events import LOADGAME

from games import gamesList


class MenuState(Enum):
	START = 0
	GAMESELECT = 1

class Menu:
	def __init__(self, surface):

		self.surface = surface
		self.throttledUpdate = ThrottledUpdate()

		# self.state = MenuState.START.value
		self.gotoStart()

		self.headerFont = pygame.font.SysFont(pygame.font.get_default_font(), self.getHeaderFontSize())
		self.headerSurf = self.headerFont.render('< R-Cade >', False, colors.WHITE)

		activeSize = self.getHeaderFontSize() * 0.3
		self.activeFont = pygame.font.SysFont(pygame.font.get_default_font(), int(activeSize))
		self.inactiveFont = pygame.font.SysFont(pygame.font.get_default_font(), int(activeSize * 0.9))

		# Menu items
		states = [state.value for state in MenuState]
		self.active = {state: 0 for state in states}
		self.items = {state: [] for state in states}
		self.items[MenuState.START.value] = [
			dict(title=u'Spela', action=self.gotoSelect),
			dict(title=u'Avsluta', action=self.quit)
		]
		self.items[MenuState.GAMESELECT.value] = self.getGameItems()

	def getHeaderFontSize(self):
		_, h = self.surface.get_size()
		return int(h * 0.2)

	def getGameItems(self):
		items = []
		for game in gamesList:
			items.append(dict(title=game.get('title', 'No name'), game=game, action=self.gotoGame))
		items.append(dict(title=u'<< Meny', action=self.gotoStart))
		return items

	def gotoStart(self):
		self.state = MenuState.START.value

	def gotoSelect(self):
		self.state = MenuState.GAMESELECT.value

	def gotoGame(self):
		state = MenuState.GAMESELECT.value
		item = self.items[state][self.active[state]]

		e = pygame.event.Event(LOADGAME, game=item.get('game'))
		pygame.event.post(e)

	def quit(self):
		e = pygame.event.Event(pygame.locals.QUIT)
		pygame.event.post(e)

	def update(self, events):
		if not self.throttledUpdate.shouldUpdate(events):
			return

		if KeyState.up():
			self.active[self.state] = max([0, self.active[self.state]-1])
		elif KeyState.down():
			self.active[self.state] = min([len(self.items[self.state])-1, self.active[self.state]+1])
		elif KeyState.enter(single=True):
			self.items[self.state][self.active[self.state]]['action']()


	def draw(self):
		self.surface.fill(colors.BLACK) # Should this be placed in __init__ instead?

		width, height = self.surface.get_size()

		# Draw header
		headerRect = self.headerSurf.get_rect(center=((width // 2), self.getHeaderFontSize() / 2))
		self.surface.blit(self.headerSurf, headerRect)


		# Draw items
		y = height * 0.4

		items = self.items[self.state]
		for index, item in enumerate(items):
				active = index == self.active[self.state]
				font = self.activeFont if active else self.inactiveFont
				textSurface = font.render(item['title'], False, colors.ACTIVETEXT if active else colors.INACTIVETEXT)
				self.surface.blit(textSurface, (0, y))
				_, h = font.size(item['title'])
				y += h * 1.5
