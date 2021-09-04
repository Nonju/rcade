import pygame

class GameBase:
	def __init__(self, surface):
		self.surface = surface

	def quit(self):
		e = pygame.event.Event(pygame.locals.QUIT)
		pygame.event.post(e)

	def update(self, events=[]):
		pass

	def draw(self):
		pass

