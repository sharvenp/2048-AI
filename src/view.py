

from settings import Settings
from observer import Observer

import pygame as pg
import time

class View(Observer):

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings.WIDTH, Settings.WIDTH))
        pg.display.set_caption('2048')

    def attach_controller(self, controller):
        self.controller = controller

    def update(self, model):

        self.screen.fill(Settings.BACKGROUND_COLOR)

        calc_width = Settings.WIDTH // model.width
        font = pg.font.SysFont(Settings.NUMBER_FONT[0], Settings.NUMBER_FONT[1])

        for i in range(model.width):
            for j in range(model.width):
                if model.board[i][j] != 0:
                    font_color = Settings.NUMBER_COLOR_1
                    square_color = Settings.SQUARE_COLORS[model.board[i][j]]

                    if model.board[i][j] > 2:
                        font_color = Settings.NUMBER_COLOR_2
    
                    pg.draw.rect(self.screen, square_color, (j * calc_width, i * calc_width, calc_width, calc_width))
                    font_surface = font.render(str(2**model.board[i][j]), True, font_color)
                    font_rect = font_surface.get_rect(center=((j * calc_width) + calc_width // 2, (i * calc_width) + calc_width // 2))
                    self.screen.blit(font_surface, font_rect)

        
        for k in range(model.width + 1):
            pg.draw.line(self.screen, Settings.LINE_COLOR, (k * calc_width, 0), (k * calc_width, Settings.WIDTH), Settings.LINE_WIDTH)
            pg.draw.line(self.screen, Settings.LINE_COLOR, (0, k * calc_width), (Settings.WIDTH, k * calc_width), Settings.LINE_WIDTH)

        if model.state != 1:
            self.game_over = True
            self.draw_message_screen(model.state, model.score)
            time.sleep(2)
            model.reset_game()

        pg.display.update()

    def draw_message_screen(self, state, score):

        font = pg.font.SysFont(Settings.MESSAGE_FONT[0], Settings.MESSAGE_FONT[1])

        color = Settings.MESSAGE_WIN_COLOR
        if state == 0:
            color = Settings.MESSAGE_LOSE_COLOR
            
        pg.draw.rect(self.screen, color, (50, 200, Settings.WIDTH - 100, Settings.WIDTH - 400))
        font_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        font_rect = font_surface.get_rect(center=(Settings.WIDTH // 2, Settings.WIDTH // 2))
        self.screen.blit(font_surface, font_rect)
        pg.display.update()

    def launch(self):

        self.game_over = False
        while True:
            while not self.game_over:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        quit(0)

                    self.controller.handle(event)
            
            self.game_over = False