
from constants.window import FPS
from utils import KeyState, ControllerState

class ThrottledUpdate:
	def __init__(self, ticks=None, refreshEvents=[]):
		self.ticks = ticks or (FPS//6) # By default, update 6 times a second
		self.last = 0

		self.refreshEvents = KeyState.getEvents()
		# self.refreshEvents += ControllerState.getEvents() # Pygame spams controller events --> disable for now
		if isinstance(refreshEvents, list): # Option to refresh on additional events
			self.refreshEvents += refreshEvents

	def shouldUpdate(self, events=[]):
		self.last += 1 # Increment tick

		if self.last >= self.ticks:
			self.last = 0
			return True

		if any(event.type in self.refreshEvents for event in events):
			self.last = 0
			return True

		return False
