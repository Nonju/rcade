import pygame

from ..gamebase import GameBase

from .events import GOTOLEVELSELECT, GOTOGAME
from .states import ScreenState
from .screens import menu, levelselect, game


class Sokoban(GameBase):
    def __init__(self, surface):
        super().__init__(surface)

        # Screens # TODO: Combine these into a single variable?
        self.menu = None
        self.levelSelect = None
        self.game = None

        self.state = ScreenState.MENU
        self.loaded = False


    def load(self):
        pygame.display.set_caption('Sokoban')
        self.menu = menu.Menu(self.surface)
        self.loaded = True

    def update(self, events=[]):
        if not self.loaded:
            self.load()
            return

        for event in events:
            if event.type == GOTOLEVELSELECT:
                self.levelSelect = levelselect.LevelSelect(self.surface)
                self.state = ScreenState.LEVELSELECT
            elif event.type == GOTOGAME:
                if bool(event.new):
                    self.game = game.Game(self.surface, level=event.level)
                self.state = ScreenState.GAME

        if self.state == ScreenState.MENU:
            self.menu.update(events)
        elif self.state == ScreenState.LEVELSELECT:
            self.levelSelect.update(events)
        elif self.state == ScreenState.GAME:
            self.game.update(events)

    def draw(self):
        if not self.loaded:
            return

        if self.state == ScreenState.MENU:
            self.menu.draw()
        elif self.state == ScreenState.LEVELSELECT:
            self.levelSelect.draw()
        elif self.state == ScreenState.GAME:
            self.game.draw()


