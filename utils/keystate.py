import pygame
from pygame.locals import K_RETURN, K_UP, K_DOWN, K_LEFT, K_RIGHT


class KeyState:

	lastPressed = set()

	@classmethod
	def update(cls, events):
		for event in events:
			if event.type == pygame.KEYDOWN:
				cls.lastPressed.add(event.key)
			elif event.type == pygame.KEYUP:
				cls.lastPressed.remove(event.key)

	@classmethod
	def getEvents(cls):
		return [pygame.KEYDOWN, pygame.KEYUP]

	@classmethod
	def pressed(cls, keys, single=False):
		if not isinstance(keys, list):
			keys = [keys]

		pressed_keys = pygame.key.get_pressed()
		if single:
			return any(pressed_keys[key] for key in keys if key not in cls.lastPressed)
		return any(pressed_keys[key] for key in keys)


	# Shorthands

	@classmethod
	def enter(cls, single=False):
		keys = [K_RETURN]
		return cls.pressed(keys, single=single)

	@classmethod
	def up(cls):
		keys = [K_UP]
		return cls.pressed(keys)

	@classmethod
	def down(cls):
		keys = [K_DOWN]
		return cls.pressed(keys)

	@classmethod
	def left(cls):
		keys = [K_LEFT]
		return cls.pressed(keys)

	@classmethod
	def right(cls):
		keys = [K_RIGHT]
		return cls.pressed(keys)
