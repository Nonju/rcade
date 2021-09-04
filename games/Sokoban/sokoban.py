import pygame
from pygame.locals import *

# import sys

# from constants import colors
from .events import *
from .states import ScreenState
from .screens import menu, levelselect, game
# from utils import KeyPressHandler, ControllerHandler

# pygame.init()
# if pygame.joystick.get_count():
#     print('Found joystick - Initializing')
#     ControllerHandler.init()

# FPS = 30
# FramePerSec = pygame.time.Clock()


# Screen
# screen_info = pygame.display.Info()
# SCREEN_WIDTH = min(screen_info.current_w, 1024)
# SCREEN_HEIGHT = min(screen_info.current_h, 800)
# DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# DISPLAYSURF.fill(colors.BROWN)
pygame.display.set_caption('Sokoban')


# def main():
#     currentState = ScreenState.MENU
#     Menu = menu.Menu(DISPLAYSURF)
#     LevelSelect = None
#     Game = None

#     while True:
#         events = pygame.event.get()
#         for event in events:
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == GOTOLEVELSELECT:
#                 LevelSelect = levelselect.LevelSelect(DISPLAYSURF)
#                 currentState = ScreenState.LEVELSELECT
#             elif event.type == GOTOGAME:
#                 if bool(event.new):
#                     Game = game.Game(DISPLAYSURF, level=event.level)
#                 currentState = ScreenState.GAME

#         if currentState == ScreenState.MENU:
#             Menu.update(events)
#             Menu.draw()
#         elif currentState == ScreenState.LEVELSELECT:
#             LevelSelect.update(events)
#             LevelSelect.draw()
#         elif currentState == ScreenState.GAME:
#             Game.update(events)
#             Game.draw()
#         else: break

#         KeyPressHandler.update(events)

#         pygame.display.update()
#         FramePerSec.tick(FPS)

# if __name__ == '__main__':
    # main()


from ..gamebase import GameBase

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


