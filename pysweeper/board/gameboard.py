__doc__ = """ Classes for creating game boards """
__author__ = """ whege """
__all__ = ["AnswerBoard", "DisplayBoard"]

from itertools import permutations, product
import random
from typing import List, Tuple

from common import *
from spaces import *


class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._board = self._make_empty(self._width, self._height)

    def __getitem__(self, item: Tuple[int, int]) -> Space:
        return self._board[item[0]][item[1]]

    @property
    def height(self) -> int:
        return self._height

    @staticmethod
    def _make_empty(width: int, height: int, /) -> List[List[Space]]:
        """
        Create an empty game board of the specified dimensions
        :param width: Width of board
        :param height: Height of board
        :return: (width, height)-shaped array of Empty Space instances
        """
        return [[Space(Empty()) for _ in range(height)] for _ in range(width)]

    def __setitem__(self, key: Tuple[int, int], value: Space) -> None:
        self._board[key[0]][key[1]] = value

    def show(self) -> None:
        """
        Print the board
        :return: None
        """
        for col in self._board:
            print(" ", end="")  # Add space to beginning of the board to separate it from the edge of the screen
            for row in col:
                print(row, end="  ")  # Print individual space on board and stay on the same line
            print("", end="\n")  # Move to the next line
        print("\n")  # Add space after the board to separate game board from the next line of input

    @property
    def width(self) -> int:
        return self._width


class AnswerBoard(Board):
    def __init__(self, width: int, height: int, n_mines: int, /):
        super().__init__(width, height)  # Create a new board
        self._n_mines = n_mines
        self._add_mines()  # Add mines to the board
        self._add_hints()  # Add number of adjacent mines to each space

    def _add_mines(self):
        """
        Add mines to the answer board
        Chooses random coordinates. If there is no mine there
        :return:
        """
        for _ in range(0, self._n_mines):  # Iterate over the number of mines to be added
            while True:
                x_coord = random.randrange(0, self._width)  # Pick a random x coordinate
                y_coord = random.randrange(0, self._height)  # Pick a random y coordinate
                space: Space = self._board[y_coord][x_coord]  # Get the Space at that coordinate

                if not space.is_mine():  # Check that the space is not already a mine
                    space.make_mine()  # Change the space to a mine
                    self._board[y_coord][x_coord] = space  # Update the Space
                    break

    def _add_hints(self):
        """
        Add hints to the spaces based on the number of mines touching that space
        :return: None
        """
        for coord in product(range(self.height), range(self.width)):
            if (space := self.__getitem__(coord)).is_mine():  # Get the current space
                continue  # If the Space is a mine, it won't have hints

            # Create a list of relative coordinates to the adjacent spaces, i.e.: [(-1, -1), (-1, 0)....etc]
            for y_shift, x_shift in list(permutations(range(-1, 2), 2)):
                try:
                    shifted_coord = (coord[0] + y_shift, coord[1] + x_shift)
                    check_space = self.__getitem__(shifted_coord)  # Try to get the adjacent space
                except IndexError:
                    continue  # Doing this naively, so we might go off the board, in which case we skip
                else:
                    if check_space.is_mine():
                        space.add_hint()  # If the adjacent space is a mine, increment the hints


class DisplayBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
