import pygame
import inspect

from utils import KeyState, ThrottledUpdate
from constants import colors, window

class MenuList:

	def __init__(self, surface, options=[], font='fonts/Roboto-Medium.ttf', fontSize=30, activeFont=None, activeFontSize=None):

		self.surface = surface
		self.throttledUpdate = ThrottledUpdate()

		self.active = 0
		self.options = options

		assert font, 'Font cannot be null'

		self.inactiveFontSize = fontSize
		self.activeFontSize = activeFontSize or (fontSize * 1.25)

		self.inactiveFont = pygame.font.Font(font, int(self.inactiveFontSize))
		self.activeFont = pygame.font.Font(activeFont or font, int(self.activeFontSize))


	def update(self, events):
		if not self.throttledUpdate.shouldUpdate(events):
			return

		if KeyState.up():
			self.active = max(self.active-1, 0)
		elif KeyState.down():
			self.active = min(self.active+1, len(self.options)-1)
		elif KeyState.enter():
			item = self.options[self.active]
			try:
				spec = inspect.getargspec(item['action'])
				args = [item] if len(spec.args) > 1 else []
				item['action'](*args)
			except Exception as e:
				item['action']()

	def draw(self, center=True, offset=(0, 0)):

		offsetX, offsetY = offset

		for index, option in enumerate(self.options):
			active = index == self.active
			font = self.activeFont if active else self.inactiveFont
			textSurface = font.render(option['title'], False, colors.ACTIVETEXT if active else colors.INACTIVETEXT)
			if center:
				cX = (window.SCREEN_WIDTH / 2) + offsetX
				cY = (window.SCREEN_HEIGHT / 2) + offsetY
				rect = textSurface.get_rect(center=(cX, cY))
				self.surface.blit(textSurface, rect)
			else:
				self.surface.blit(textSurface, (offsetX, offsetY))
			offsetY += self.activeFontSize if active else self.inactiveFontSize

