
from observable import Observable

import random
import numpy as np

class Board(Observable):

    def __init__(self):
        Observable.__init__(self)
        self.width = 4
        self.reset_game()
        
    def reset_game(self):
        self.state = 1
        self.score = 0
        self.board = []
        for i in range(self.width):
            a = []
            for j in range(self.width):
                a.append(0)
            self.board.append(a)

        self._spawn_number()
        self._spawn_number()

        self.notify_observers()

    def set_board(self, board):

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.board[i][j] = board[i][j]

        self.notify_observers()

    def _update_game_state(self):
        """
        0: Game over
        1: Game continue
        2: Game won
        """
        cont = False
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] == 11:
                    self.state = 2
                    return
                if self.board[i][j] == 0 or self._can_merge((i, j)):
                    cont = True

        self.state = int(cont)

        if int(cont) != 1:
            self.notify_observers()

    def _spawn_number(self):
        """
        Spawn a number randomly
        90% Chance - Spawns 2
        10% Chance - Spawns 4
        """
        possible_squares = []
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    possible_squares.append((i, j))
        
        if len(possible_squares) == 0:
            return

        i, j = random.choice(possible_squares)
        
        if random.random() < 0.9:
            self.board[i][j] = 1
        else:
            self.board[i][j] = 2

    def _check_valid(self, coord):
        """
        Check if coord is within the board
        """
        i, j = coord
        return (0 <= i < self.width) and (0 <= j < self.width)

    def _can_merge(self, coord):
        """
        Check if value at coord can merge with adjacent values
        """
        i, j = coord
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + d[0]
            nj = j + d[1]
            if self._check_valid((ni, nj)):
                if self.board[i][j] == self.board[ni][nj]:
                    return True
        return False

    def _get_sign(self, x):
        """
        Return the sign of x
        (Return 1 if x == 0)
        """
        if x == 0: return 1

        return abs(x) // x

    def _move_left(self):
        for i in range(self.width):
            k = 0
            for j in range(self.width):

                val = self.board[i][j]
                
                if val == 0:
                    continue

                w = j
                while self._check_valid((i, w - 1)) and w > k:

                    if self.board[i][w] == self.board[i][w - 1]:
                        k = w
                        self.board[i][w - 1] += 1
                        self.score += 2**self.board[i][w - 1]
                        self.board[i][w] = 0
                    elif self.board[i][w - 1] == 0:
                        self.board[i][w - 1] = self.board[i][w]
                        self.board[i][w] = 0

                    w -= 1

    def _rotate_left_90(self, times):
        a = np.array(self.board, int)
        a = np.rot90(a, times)
        self.board = a.tolist()

    def _move_right(self):
        self._rotate_left_90(2)
        self._move_left()
        self._rotate_left_90(2)

    def _move_up(self):
        self._rotate_left_90(1)
        self._move_left()
        self._rotate_left_90(3)
    
    def _move_down(self):
        self._rotate_left_90(3)
        self._move_left()
        self._rotate_left_90(1)

    def move(self, direction):
        """
        Make a 2048 move towards direction and spawn a number
        """
        copy = []
        for row in self.board:
            a = []
            for col in row:
                a.append(col)
            copy.append(a)
    
        if direction == 0:
            self._move_up()
        elif direction == 1:
            self._move_down()
        elif direction == 2:
            self._move_left()
        elif direction == 3:
            self._move_right()

        # If board hasn't changed, don't spawn
        if copy != self.board:
            self._spawn_number()
            self._update_game_state()
            self.notify_observers()

    def print_board(self):
        """
        Print the board
        Example print:
        -------
        0 0 2 0
        0 2 0 0
        0 0 0 0
        0 0 0 0
        -------
        """
        print("-"*7)
        for row in self.board:
            for i in row:
                print(i, end=' ')
            print("")
        print("-"*7)
