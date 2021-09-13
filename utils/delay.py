import pygame

from events import DELAYCALLBACK

class Delay:

	clock = None
	elapsed = 0
	callbacks = []

	@classmethod
	def init(cls):
		cls.clock = pygame.time.Clock()

	@classmethod
	def update(cls, events):
		cls.clock.tick()
		cls.elapsed += cls.clock.get_time()

		if not any(event.type == DELAYCALLBACK for event in events):
			return

		for cb in cls.callbacks:
			if cb['time'] <= cls.elapsed:
				cls.callbacks.remove(cb)
				cb['f']()


	@classmethod
	def call(cls, f, ms=1000):
		cls.callbacks.append(dict(f=f, time=cls.elapsed + ms))
		pygame.time.set_timer(DELAYCALLBACK, ms, True)
