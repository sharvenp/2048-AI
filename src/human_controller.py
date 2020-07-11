
from controller import Controller

import pygame as pg

class HumanController(Controller):

    def __init__(self, board):
        Controller.__init__(self, board)

    def handle(self, event):

        controls_dict = {pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 2, pg.K_RIGHT: 3}
        
        if event.type == pg.KEYDOWN and event.key in controls_dict:
            self.board.move(controls_dict[event.key])

        if self.board.state == 0:
            print(f"Game Over. Score: {self.board.score}")
        elif self.board.state == 2:
            print(f"Win! Score: {self.board.score}")