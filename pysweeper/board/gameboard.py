__doc__ = """ Classes for creating game boards """
__author__ = """ whege """
__all__ = ["AnswerBoard", "DisplayBoard"]

import random
from typing import List, Tuple

from common import *
from spaces import *


class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._board = self._make_empty(self._width, self._height)

    def __getitem__(self, item: Tuple[int, int]):
        return self._board[item[0]][item[1]]

    @property
    def height(self):
        return self._height

    @staticmethod
    def _make_empty(width: int, height: int, /) -> List[List[Space]]:
        return [[Space(Empty()) for _ in range(height)] for _ in range(width)]

    def __setitem__(self, key: Tuple[int, int], value: Space):
        self._board[key[0]][key[1]] = value

    def show(self):
        for _ in self._board:
            print(" ", end="")
            for i in _:
                print(i, end="  ")
            print()
        print("\n")

    @property
    def width(self):
        return self._width


class AnswerBoard(Board):
    def __init__(self, width: int, height: int, n_mines: int, /):
        super().__init__(width, height)
        self._n_mines = n_mines
        self._add_mines()

    def _add_mines(self):
        for _ in range(0, self._n_mines):
            while True:
                x_coord = random.randrange(0, self._width)
                y_coord = random.randrange(0, self._height)
                space: Space = self._board[y_coord][x_coord]

                if not space.is_mine():
                    space.make_mine()
                    self._board[y_coord][x_coord] = space
                    break


class DisplayBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
