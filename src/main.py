from constants import *
import pygame
import random
import gui
import theme
import pieces
import glob
import os
import sys
from pathlib import Path



class Tetris:
    def __init__(self):
        self.running = True
        self.cols = COLS
        self.rows = ROWS
        self.themes = self.get_themes()
        self.theme_idx = 0
        self.theme = theme.Theme('monokai')

        self.gui = gui.GUI(self.rows, self.cols, self.theme)

        self.score = 0
        self.queue = []

        self.pieces_types = [
            pieces.PieceI, pieces.PieceT,
            pieces.PieceO, pieces.PieceZ,
            pieces.PieceS, pieces.PieceL,
            pieces.PieceJ
        ]

        self.fps = FPS
        self.playing = False


    def get_themes(self):
        dirname = os.path.dirname(__file__)
        path = os.path.realpath(os.path.join(dirname, '..', 'themes'))
        themes = [Path(theme).stem for theme in glob.glob(f"{path}/*.json")]
        return sorted(themes)


    def reset_space(self):
        self.space = [
            [W] + [E]*(self.cols-2) + [W] for i in range(self.rows-1)
        ]
        self.space.append([W]*self.cols)


    def reset_space_sample(self):
        self.space = [
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, E, E, T, E, E, E, W],
            [W, E, E, E, E, E, T, T, T, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, E, I, E, S, E, E, E, J, E, E, W],
            [W, E, I, E, S, S, E, E, J, E, E, W],
            [W, E, I, E, E, S, E, J, J, E, E, W],
            [W, E, I, E, E, E, E, E, E, E, E, W],
            [W, E, E, E, E, L, E, E, E, Z, E, W],
            [W, E, O, O, E, L, E, E, Z, Z, E, W],
            [W, E, O, O, E, L, L, E, Z, E, E, W],
            [W, E, E, E, E, E, E, E, E, E, E, W],
            [W, W, W, W, W, W, W, W, W, W, W, W]
        ]
        self.score = 1234
        self.queue.append(pieces.PieceT(self.space, rotate=False))
        #self.next_piece()


    def update_screen(self):
        self.gui.draw_space(self.space)
        self.gui.draw_score_value(self.score)
        self.gui.draw_next_piece(self.queue[0])
        self.gui.update()


    def print_space(self):
        for rows in self.space:
            print(rows)
        print("\n")


    def next_piece(self):
        #self.pieces_types = [pieces.PieceI]

        if not self.queue:
            piece_type = random.choice(self.pieces_types)
            self.queue.append(piece_type(self.space))

        piece_type = random.choice(self.pieces_types)
        self.queue.append(piece_type(self.space))
        self.piece = self.queue.pop(0)


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.fps = FPS
                else:
                    self.action = GO_DOWN

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.fps = FPS + 5

                elif event.key == pygame.K_LEFT:
                    self.action = GO_LEFT

                elif event.key == pygame.K_RIGHT:
                    self.action = GO_RIGHT

                elif event.key == pygame.K_UP:
                    if self.action != ROTATE:
                        self.action = ROTATE

                elif event.key == pygame.K_KP_PLUS:
                    self.next_theme()

                elif event.key == pygame.K_KP_MINUS:
                    self.prev_theme()

                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused


    def next_theme(self):
        self.theme_idx += 1
        if self.theme_idx == len(self.themes):
            self.theme_idx = 0
        self.theme.load(self.themes[self.theme_idx])
        self.gui.reset_layout()
        self.update_screen()


    def prev_theme(self):
        self.theme_idx -= 1
        if self.theme_idx < 0:
            self.theme_idx = len(self.themes) - 1
        self.theme.load(self.themes[self.theme_idx])
        self.gui.reset_layout()
        self.update_screen()


    def merge(self):
        changed = True
        merged = 0
        bonus = 100
        while changed:
            changed = False
            for i in range(len(self.space) - 1):
                if self.space[i].count(E) == 0:
                    changed = True
                    self.space.pop(i)
                    self.space.insert(0, [W] + [E]*(self.cols-2) + [W])

                    self.score += bonus
                    merged += 1
                    bonus += 100

        if merged > 0:
            #self.score += merged * 100 + bonus
            self.update_screen()


    def new_game(self):
        self.score = 0
        self.reset_space()
        self.next_piece()
        self.action = GO_DOWN
        self.playing = True
        self.paused = False
        self.delay = 1000
        self.rate = RATE


    def game_over(self):
        print("Game over")
        self.piece.action(self.action)
        self.playing = False

    def run(self, debug_theme=False):
        clock = pygame.time.Clock()

        if debug_theme:
            self.reset_space_sample()
        else:
            self.new_game()

        self.update_screen()

        while self.running:
            self.process_events()

            if self.playing and not self.paused:
                if self.action != GO_DOWN:
                    self.piece.action(self.action)
                    self.update_screen()
                    if self.action == ROTATE:
                        self.action = GO_DOWN

                if self.rate <= 0 or self.fps > FPS:
                    self.piece.action(GO_DOWN)
                    self.update_screen()
                    self.rate = RATE

                    if self.piece.stopped:
                        self.action = GO_DOWN
                        self.merge()
                        self.next_piece()
                        self.score += 10
                        if not self.piece.movable:
                            self.game_over()
                            self.update_screen()

                self.rate -= 1

            clock.tick(self.fps)


debug_theme = False
tetris = Tetris()

if len(sys.argv) > 1 and sys.argv[1] == 'debugtheme':
    debug_theme = True

tetris.run(debug_theme)

