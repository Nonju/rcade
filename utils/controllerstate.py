import pygame

# Custom joystick keys
J_UP = 1337
J_DOWN = 1338
J_RIGHT = 1339
J_LEFT = 1340

J_A = 1341
J_B = 1342
J_SELECT = 1343
J_START = 1344

class ControllerState:
	'''
		Based of the retrolink nes controller
	'''

	joystick = None

	@classmethod
	def init(cls):
		if not pygame.joystick.get_count():
			return
		print('Found joystick - Initializing')

		if not pygame.joystick.get_init():
			pygame.joystick.init()

		try:
			cls.joystick = pygame.joystick.Joystick(0)
			cls.joystick.init()
		except:
			print('Failed to initialize joystick')
			cls.joystick = None

	@classmethod
	def active(cls):
		return pygame.joystick.get_init() and bool(cls.joystick)

	@classmethod
	def getEvents(cls):
		return [pygame.JOYAXISMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP]

	@classmethod
	def getKeys(cls):
		return [J_UP, J_DOWN, J_RIGHT, J_LEFT, J_A, J_B, J_SELECT, J_START]

	@classmethod
	def getPressed(cls):
		x = [
			(cls.up, J_UP),
			(cls.down, J_DOWN),
			(cls.right, J_RIGHT),
			(cls.left, J_LEFT),
			(cls.a, J_A),
			(cls.b, J_B),
			(cls.select, J_SELECT),
			(cls.start, J_START)
		]
		return [key for f, key in x if f()]

	@classmethod
	def up(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_axis(1) <= -0.5)

	@classmethod
	def down(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_axis(1) >= 0.5)

	@classmethod
	def right(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_axis(0) >= 0.5)

	@classmethod
	def left(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_axis(0) <= -0.5)

	@classmethod
	def a(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_button(1))

	@classmethod
	def b(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_button(2))

	@classmethod
	def select(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_button(8))

	@classmethod
	def start(cls):
		if not cls.active(): return False
		return bool(cls.joystick.get_button(9))
