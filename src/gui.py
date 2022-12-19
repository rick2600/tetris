import pygame
import pygame.font
from constants import *
import base64
import io


class GUI:
    def __init__(self, rows, cols, theme):
        pygame.init()
        pygame.display.set_caption('Tetris Game')
        self.rect_size = RECT_SIZE
        self.space_rows = rows
        self.space_cols = cols
        self.r_side_width = 10 * self.rect_size

        self.width = self.space_cols * self.rect_size + self.r_side_width
        self.height = self.space_rows * self.rect_size
        self.theme = theme
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.theme.get('bg-color'))

        self.init_layout()
        self.draw_r_side()
        self.update()


    def reset_layout(self):
        self.screen.fill(self.theme.get('bg-color'))
        self.draw_r_side()
        self.update()


    def draw_r_side(self):
        self.draw_score_label()
        self.draw_score_box()
        self.draw_score_value(0)
        self.draw_next_piece_label()
        self.draw_next_piece_box()
        self.draw_controls_label()
        self.draw_controls_box()
        self.draw_controls_value()
        self.draw_status_value()


    def draw_cell(self, x, y, value):
        theme = self.theme.get(abs(value))
        radius = theme.get('border-radius', 0)

        rect = pygame.Rect(y, x, self.rect_size, self.rect_size, border_radius=radius)
        pygame.draw.rect(self.screen, theme['bg-color'], rect, 0, border_radius=radius)

        img_src = theme.get('img', None)
        if img_src != None:
            img_src = io.BytesIO(base64.b64decode(img_src))
            img = pygame.image.load(img_src)
            img = pygame.transform.scale(img, (RECT_SIZE, RECT_SIZE))
            self.screen.blit(img, rect)


        if theme['border-size']:
            pygame.draw.rect(
                self.screen,
                theme['border-color'],
                rect,
                theme['border-size']
            )


    def draw_space(self, space):
        for i in range(1, len(space)):
            for j in range(len(space[i])):
                self.draw_cell(
                    i*self.rect_size,
                    j*self.rect_size,
                    space[i][j]
                )


    def init_layout(self):
        size = self.rect_size
        r_width = self.r_side_width - 2 * size

        x = 1 * size
        y = (self.space_cols + 1) * size
        self.score_label = pygame.Rect(y, x, r_width, size)
        prev_y, prev_x, prev_w, prev_h = self.score_label

        self.score_box = pygame.Rect(prev_y, prev_x + 1 * size, r_width, size * 2)
        prev_y, prev_x, prev_w, prev_h = self.score_box

        self.next_piece_label = pygame.Rect(prev_y, prev_x + prev_h + 1 * size, prev_w, size)
        prev_y, prev_x, prev_w, prev_h = self.next_piece_label

        self.next_piece_box =  pygame.Rect(prev_y, prev_x + 1 * size, r_width, size * 3)
        prev_y, prev_x, prev_w, prev_h = self.next_piece_box

        self.controls_label = pygame.Rect(prev_y, prev_x + prev_h + 1 * size, r_width, size)
        prev_y, prev_x, prev_w, prev_h = self.controls_label

        self.controls_box = pygame.Rect(prev_y, prev_x + 1 * size, r_width, size * 6)
        prev_y, prev_x, prev_w, prev_h = self.controls_box

        self.status_value = pygame.Rect(prev_y, prev_x + prev_h + 1 * size, r_width, size)




    def draw_score_label(self):
        theme = self.theme.get('score')['label']
        font = pygame.font.SysFont(None, theme['font-size'])
        text = font.render("Score", True, theme['font-color'])
        text_rect = text.get_rect(center=self.score_label.center)
        self.screen.blit(text, text_rect)


    def draw_score_box(self):
        theme = self.theme.get('score')['box']
        border_color = theme['border-color']
        border_size = theme['border-size']
        pygame.draw.rect(self.screen, theme['bg-color'], self.score_box, 0)
        pygame.draw.rect(self.screen, border_color, self.score_box, border_size)


    def draw_score_value(self, score):
        self.draw_score_box()
        theme = self.theme.get('score')['value']
        font = pygame.font.SysFont(None, theme['font-size'])
        text = font.render(str(score), True, theme['font-color'])
        text_rect = text.get_rect(center=self.score_box.center)
        self.screen.blit(text, text_rect)


    def draw_next_piece_label(self):
        theme = self.theme.get('next-piece')['label']
        font = pygame.font.SysFont(None, theme['font-size'])
        text = font.render("Next", True, theme['font-color'])
        text_rect = text.get_rect(center=self.next_piece_label.center)
        self.screen.blit(text, text_rect)


    def draw_next_piece_box(self):
        theme = self.theme.get('next-piece')['box']
        border_color = theme['border-color']
        border_size = theme['border-size']
        pygame.draw.rect(self.screen, theme['bg-color'], self.next_piece_box, 0)
        pygame.draw.rect(self.screen, border_color, self.next_piece_box, border_size)


    def draw_next_piece(self, next_piece):
        self.draw_next_piece_box()
        center = self.next_piece_box.center
        pos_x = center[1] - (next_piece.height * self.rect_size) // 2
        pos_y = center[0] - (next_piece.width * self.rect_size)  // 2

        for i in range(next_piece.height):
            for j in range(next_piece.width):
                value = next_piece.matrix[i][j]
                if value != 0:
                    x = pos_x + (i * self.rect_size)
                    y = pos_y + (j * self.rect_size)
                    self.draw_cell(x, y, value)


    def draw_controls_label(self):
        theme = self.theme.get('controls')['label']
        font = pygame.font.SysFont(None, theme['font-size'])
        text = font.render("Controls", True, theme['font-color'])
        text_rect = text.get_rect(center=self.controls_label.center)
        self.screen.blit(text, text_rect)


    def draw_controls_box(self):
        theme = self.theme.get('controls')['box']
        border_color = theme['border-color']
        border_size = theme['border-size']
        pygame.draw.rect(self.screen, theme['bg-color'], self.controls_box, 0)
        pygame.draw.rect(self.screen, border_color, self.controls_box, border_size)


    def draw_status_value(self, status=None):
        if status != None:
            bg_color = self.theme.get('bg-color')
            theme = self.theme.get('status')
            pygame.draw.rect(self.screen, bg_color, self.status_value, 0)

            font = pygame.font.SysFont(None, theme['value']['font-size'])
            text = font.render(str(status), True, theme['value']['font-color'])
            text_rect = text.get_rect(center=self.status_value.center)
            self.screen.blit(text, text_rect)


    def update(self):
        pygame.display.update()



    def draw_controls_value(self):
        theme = self.theme.get('controls')['value']
        font = pygame.font.SysFont(None, theme['font-size'])
        text = font.render("Controls", True, theme['font-color'])
        start_y = self.controls_box[0] + 10
        start_x = self.controls_box[1] + 10

        controls_texts = [
            ['Go Left',    'Arrow Left'],
            ['Go Right',   'Arrow Right'],
            ['Rotate',     'Arrow Up'],
            ['Speed++',    'Arrow Down'],
            ['Pause',      'Space'],
            ['Next Theme', '+'],
            ['Prev Theme', '-'],
            ['New Game',   'CTRL+N']
        ]

        for legend, key in controls_texts:
            font = pygame.font.SysFont(None, theme['font-size'])
            text = font.render(legend, True, theme['font-color'])
            self.screen.blit(text, (start_y, start_x))

            text = font.render(key, True, theme['font-color'])
            self.screen.blit(text, (start_y+5*theme['font-size'], start_x))
            start_x += theme['font-size']
