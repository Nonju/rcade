
from constants.window import FPS
from utils import KeyState

class ThrottledUpdate:
	def __init__(self, ticks=None, refreshEvents=[]):
		self.ticks = ticks or (FPS//6) # By default, update 6 times a second
		self.last = 0
		self.refreshEvents = refreshEvents # Option to refresh on additional events

	def shouldUpdate(self, events=[]):
		self.last += 1 # Increment tick

		if self.last >= self.ticks:
			self.last = 0
			return True

		refreshEvents = KeyState.getEvents()
		if isinstance(self.refreshEvents, list):
			refreshEvents += self.refreshEvents

		if any(event.type in refreshEvents for event in events):
			self.last = 0
			return True

		return False
