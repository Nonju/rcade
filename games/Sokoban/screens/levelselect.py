
import pygame
import os

from ..constants import colors
from ..events import GOTOGAME
from utils import KeyState, ThrottledUpdate, MenuList
from constants import window

LEVEL_DIR = '/../levels/'

class LevelSelect:
    def __init__(self, surface):
        super().__init__()

        self.surface = surface
        self.throttledUpdate = ThrottledUpdate()

        self.headerFont = pygame.font.Font('fonts/Roboto-Bold.ttf', self.getHeaderFontSize())
        self.headerSurf = self.headerFont.render('Välj nivå!', False, colors.WHITE)

        options = [dict(title=level, action=self.startGame) for level in self.listLevels()]
        self.menuList = MenuList(surface, options=options)

    def getHeaderFontSize(self):
        return int(window.SCREEN_HEIGHT * 0.13)

    def listLevels(self):
        files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + LEVEL_DIR)
        files = filter(lambda f: f.endswith('.sokoban'), files)
        return [f.split('.sokoban')[0] for f in files]

    def startGame(self, item):
        level = item.get('title')
        assert level # TODO: Add better error handling
        e = pygame.event.Event(GOTOGAME, new=True, level=level)
        pygame.event.post(e)

    def update(self, events):
        self.menuList.update(events)

    def draw(self):
        self.surface.fill(colors.CORNFLOWERBLUE)

        # Draw header
        headerRect = self.headerSurf.get_rect(center=(window.SCREEN_WIDTH/2, self.getHeaderFontSize() * 1.5))
        self.surface.blit(self.headerSurf, headerRect)

        # Draw menu options
        self.menuList.draw()
