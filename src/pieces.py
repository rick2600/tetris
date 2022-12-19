from constants import *
import numpy as np
import random

class Piece:
    def __init__(self, matrix, space, rotate=False):
        if rotate:
            k = random.randint(0, 4)
        else:
            k = 0

        self.matrix = np.rot90(matrix, k=k, axes=(1, 0))
        self.space = space
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.stopped = False
        self.x = 0
        self.y = (len(self.space[0]) - self.width) // 2

        #self.movable = self.can_move()


    '''
    def can_move(self):
        if self.can_go_down():
            return True

        for i in range(1, 5):
            rotated = len(np.rot90(self.matrix, k=1, axes=(1, 0)))
            if rotated < self.can_rotate(1):
                self.rotate(1)
                break

        while not self.can_go_down() and self.height > 0:
            self.matrix = self.matrix[:-1]
            self.height -= 1

        return self.height > 0
    '''



    def action(self, action):
        if action == GO_DOWN:
            if self.can_go_down():
                self.move(+1, 0)
            else:
                self.stop()

        elif action == GO_LEFT and self.can_go_left():
            self.move(0, -1)

        elif action == GO_RIGHT and self.can_go_right():
            self.move(0, +1)

        elif action == ROTATE and self.can_rotate():
            self.rotate()
            self.move(0, 0)


    def can_go_down(self):
        for i in range(self.height):
            for j in range(self.width):
                space_value = self.space[self.x+i+1][self.y+j]
                if self.matrix[i][j] != E and space_value > E:
                    return False
        return True


    def can_go_left(self):
        for i in range(self.height):
            for j in range(self.width):
                space_value = self.space[self.x+i][self.y+j-1]
                if self.matrix[i][j] != E and space_value > E:
                    return False
        return True


    def can_go_right(self):
        for i in range(self.height):
            for j in range(self.width):
                space_value = self.space[self.x+i][self.y+j+1]
                if self.matrix[i][j] != E and space_value > E:
                    return False
        return True


    def move(self, x_inc, y_inc):
        self.clear()
        self.x += x_inc
        self.y += y_inc
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] != E:
                    if self.space[self.x+i][self.y+j] == E:
                        self.space[self.x+i][self.y+j] = -self.matrix[i][j]


    def rotate(self, k=1):
        self.clear()
        self.matrix = np.rot90(self.matrix, k=k, axes=(1, 0))
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

        while self.y + self.width > len(self.space[0]) - 1:
            self.y -= 1

        while self.x + self.height > len(self.space):
            self.x -= 1


    def can_rotate(self, k=1):
        rotated_matrix = np.rot90(self.matrix, k=k, axes=(1, 0))
        rotated_height = len(rotated_matrix)
        rotated_width = len(rotated_matrix[0])
        x = self.x
        y = self.y
        while y + rotated_width > len(self.space[0]) - 1:
            y -= 1

        while x + rotated_height > len(self.space):
            x -= 1

        for i in range(rotated_height):
            for j in range(rotated_width):
                space_value = self.space[x+i][y+j]
                if rotated_matrix[i][j] != E and space_value > E:
                    return False
        return True





    def stop(self):
        self.stopped = True
        for i in range(self.height):
            for j in range(self.width):
                if self.space[self.x+i][self.y+j] < E:
                    self.space[self.x+i][self.y+j] *= -1

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.space[self.x+i][self.y+j] < E:
                    self.space[self.x+i][self.y+j] = E





class PieceI(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [I, I, I, I],
        ])
        super().__init__(matrix, space, rotate)



class PieceT(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [0, T, 0],
            [T, T, T],
        ])
        super().__init__(matrix, space, rotate)


class PieceO(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [O, O],
            [O, O]
        ])
        super().__init__(matrix, space, rotate)


class PieceZ(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [Z, Z, 0],
            [0, Z, Z]
        ])
        super().__init__(matrix, space, rotate)

class PieceS(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [0, S, S],
            [S, S, 0]
        ])
        super().__init__(matrix, space, rotate)


class PieceL(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [0, 0, L],
            [L, L, L]
        ])
        super().__init__(matrix, space, rotate)


class PieceJ(Piece):
    def __init__(self, space, rotate=False):
        matrix = np.array([
            [J, 0, 0],
            [J, J, J]
        ])
        super().__init__(matrix, space, rotate)