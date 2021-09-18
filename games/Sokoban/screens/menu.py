
import pygame

from ..constants import colors
from ..events import GOTOLEVELSELECT
from events import GOTOMAINMENU
from utils import KeyState, ThrottledUpdate, MenuList
from constants import window

class Menu:
    def __init__(self, surface):
        super().__init__()
        self.newGameEvent = pygame.event.Event(GOTOLEVELSELECT)

        self.surface = surface
        self.throttledUpdate = ThrottledUpdate()

        self.active = 0 # Active option
        self.options = [
            dict(title=u'Spela!', action=self.newGame),
            dict(title=u'Highscore', action=self.gotoHighscore),
            dict(title=u'Avsluta', action=self.quit)
        ]

        self.headerFont = pygame.font.Font('fonts/Roboto-Bold.ttf', self.getHeaderFontSize())
        self.headerSurf = self.headerFont.render('SOKOBAN!', False, colors.WHITE)

        self.menuList = MenuList(surface, options=self.options)

    def getHeaderFontSize(self):
        return int(window.SCREEN_HEIGHT * 0.15)

    def newGame(self):
        pygame.event.post(self.newGameEvent)

    def gotoHighscore(self):
        pass

    def quit(self):
        e = pygame.event.Event(GOTOMAINMENU)
        pygame.event.post(e)

    def update(self, events):
        self.menuList.update(events)

    def draw(self):
        self.surface.fill(colors.CORNFLOWERBLUE) # Should this be placed in __init__ instead?

        # Draw header
        headerRect = self.headerSurf.get_rect(center=(window.SCREEN_WIDTH/2, self.getHeaderFontSize()))
        self.surface.blit(self.headerSurf, headerRect)

        # Draw menu options
        self.menuList.draw()

