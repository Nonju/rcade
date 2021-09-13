import pygame
from pygame.locals import K_RETURN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d, K_k, K_j, K_h, K_l

from .controllerstate import ControllerState, J_UP, J_DOWN, J_RIGHT, J_LEFT, J_A, J_B, J_SELECT, J_START

class KeyState:

	lastPressed = set()

	@classmethod
	def update(cls, events):
		for event in events:
			if event.type == pygame.KEYDOWN:
				cls.lastPressed.add(event.key)
			elif event.type == pygame.KEYUP:
				cls.lastPressed.remove(event.key)
			elif ControllerState.active() and event.type in ControllerState.getEvents():
				for key in ControllerState.getKeys():
					if key in cls.lastPressed:
						cls.lastPressed.remove(key)
				cls.lastPressed.update(ControllerState.getPressed())

	@classmethod
	def getEvents(cls):
		return [pygame.KEYDOWN, pygame.KEYUP]

	@classmethod
	def pressed(cls, keys, single=False):
		if not isinstance(keys, list):
			keys = [keys]

		pressed_keys = pygame.key.get_pressed()
		controller_pressed_keys = ControllerState.getPressed()

		if single:
			return any(pressed_keys[key] or key in controller_pressed_keys for key in keys if key not in cls.lastPressed)
		return any(pressed_keys[key] or key in controller_pressed_keys for key in keys)


	# Shorthands

	@classmethod
	def any(cls):
		return len(cls.lastPressed) > 0

	@classmethod
	def enter(cls, single=True):
		keys = [K_RETURN, J_A]
		return cls.pressed(keys, single=single)

	@classmethod
	def up(cls):
		keys = [K_UP, K_w, K_k, J_UP]
		return cls.pressed(keys)

	@classmethod
	def down(cls):
		keys = [K_DOWN, K_s, K_j, J_DOWN]
		return cls.pressed(keys)

	@classmethod
	def left(cls):
		keys = [K_LEFT, K_a, K_h, J_LEFT]
		return cls.pressed(keys)

	@classmethod
	def right(cls):
		keys = [K_RIGHT, K_d, K_l, J_RIGHT]
		return cls.pressed(keys)
