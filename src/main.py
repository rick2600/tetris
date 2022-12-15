from constants import *
import pygame
import random
import gui
import theme
import pieces
import os
import sys



class Tetris:
    def __init__(self):
        self.running = True
        self.cols = COLS
        self.rows = ROWS

        self.theme = theme.Theme()
        self.theme.load('monokai')

        self.gui = gui.GUI(self.rows, self.cols, self.theme)

        self.playing = False
        self.restart = False
        self.paused = True
        self.score = 0
        self.pieces_queue = []
        self.fps = FPS

        self.pieces_types = [
            pieces.PieceI, pieces.PieceT,
            pieces.PieceO, pieces.PieceZ,
            pieces.PieceS, pieces.PieceL,
            pieces.PieceJ
        ]


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
        self.pieces_queue.append(pieces.PieceT(self.space, rotate=False))
        #self.next_piece()


    def update_screen(self):
        self.gui.draw_space(self.space)
        self.gui.draw_score_value(self.score)
        self.gui.draw_next_piece(self.pieces_queue[0])

        status = None

        if self.paused:
            status = 'Paused'
        elif self.playing:
            status = 'Playing'

        self.gui.draw_status_value(status)
        self.gui.update()


    def print_space(self):
        for rows in self.space:
            print(rows)
        print("\n")


    def next_piece(self):
        #self.pieces_types = [pieces.PieceI]

        if not self.pieces_queue:
            piece_type = random.choice(self.pieces_types)
            self.pieces_queue.append(piece_type(self.space))

        piece_type = random.choice(self.pieces_types)
        self.pieces_queue.append(piece_type(self.space))
        self.piece = self.pieces_queue.pop(0)


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
                    self.fps = FPS + FPS_INC

                elif event.key == pygame.K_LEFT:
                    self.action = GO_LEFT

                elif event.key == pygame.K_RIGHT:
                    self.action = GO_RIGHT

                elif event.key == pygame.K_UP:
                    if self.action != ROTATE:
                        self.action = ROTATE

                elif event.key == pygame.K_KP_PLUS:
                    self.theme.load_next()
                    self.gui.reset_layout()
                    self.update_screen()

                elif event.key == pygame.K_KP_MINUS:
                    self.theme.load_prev()
                    self.gui.reset_layout()
                    self.update_screen()

                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused

                elif event.key == pygame.K_n:
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.playing = False
                        self.restart = True


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
        self.playing = True
        self.paused = False
        self.restart = False
        self.rate = RATE
        self.action = GO_DOWN
        self.score = 0
        self.pieces_queue.clear()
        self.reset_space()
        self.next_piece()



    def game_over(self):
        self.gui.draw_status_value('Game Over')
        #self.piece.action(self.action)
        self.playing = False


    def run(self):
        clock = pygame.time.Clock()

        self.reset_space_sample()

        while self.running:
            self.update_screen()
            self.process_events()

            if self.playing and not self.paused:
                if self.action != GO_DOWN:
                    self.piece.action(self.action)
                    self.update_screen()
                    if self.action == ROTATE:
                        self.action = GO_DOWN

                if self.rate <= 0 or self.fps > FPS:
                    self.piece.action(GO_DOWN)
                    #self.update_screen()
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

            elif self.restart:
                self.new_game()

            clock.tick(self.fps)


tetris = Tetris()
tetris.run()

