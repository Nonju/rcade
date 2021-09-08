import pygame

class Delay:

	clock = None
	elapsed = 0
	callbacks = []

	@classmethod
	def init(cls):
		cls.clock = pygame.time.Clock()

	@classmethod
	def update(cls):
		cls.clock.tick()
		cls.elapsed += cls.clock.get_time()

		for cb in cls.callbacks:
			if (cb['time'] + cb['ms']) < cls.elapsed:
				cls.callbacks.remove(cb)
				cb['f']()


	@classmethod
	def call(cls, f, ms=1000):
		cls.callbacks.append(dict(f=f, ms=ms, time=cls.elapsed))
