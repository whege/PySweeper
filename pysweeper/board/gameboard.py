__doc__ = """ Classes for creating game boards """
__author__ = """ whege """
__all__ = ["AnswerBoard", "DisplayBoard"]

from itertools import product
import random
from typing import List, Tuple

from common import *
from spaces import *


class Board:
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._board: List[List[Space]] = self._make_empty(self._width, self._height)

    def __getitem__(self, item: Tuple[int, int]) -> Space:
        return self._board[item[0]][item[1]]

    def __iter__(self):
        for row in self._board:
            yield from row

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
        return [[Space(Empty, (j, i)) for i in range(width)] for j in range(height)]

    def __repr__(self):
        return self.show()

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
        self._set_neighbors()  # Set the neighbors for each space on the board
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
                space: Space = self.__getitem__((y_coord, x_coord))  # Get the Space at that coordinate

                if not space.is_mine():  # Check that the space is not already a mine
                    space.make_mine()  # Change the space to a mine
                    self.__setitem__((y_coord, x_coord), space)  # Update the Space
                    break

    def _add_hints(self) -> None:
        """
        Add hints to the spaces based on the number of mines touching that space
        :return: None
        """
        for space in self.__iter__():  # Iterate over the spaces in the board
            if space.is_mine():
                continue  # If the Space is a mine, it won't have hints

            else:  # o.w. count the number of neighbors that are mines, and set Hint to the value
                space.hint = sum([1 if n.is_mine() else 0 for n in space.neighbors])

    def _set_neighbors(self) -> None:
        """
        Iterate over all Spaces in the board
        Set the neighboring Spaces for a given Space
        :return: None
        """
        for space in self.__iter__():  # Iterate over the spaces in the board
            coord: Tuple[int, int] = space.loc  # Get the coordinates of the Space
            _neighbors: List[Space] = []  # Set neighbors to empty list

            # Create a list of relative coordinates to the adjacent spaces, i.e.: [(-1, -1), (-1, 0)....etc]
            shifts = list(product(range(-1, 2), range(-1, 2)))
            shifts.remove((0, 0))  # Remove the Space's own coordinates
            assert len(shifts) == 8  # eight neighbors to each space

            for y_shift, x_shift in shifts:
                shifted_coord = (coord[0] + y_shift, coord[1] + x_shift)  # shift up/down/left/right on the board
                if any(i < 0 for i in shifted_coord):  # Want to avoid negative indexing. (0,0) is not next to (8,8)
                    continue
                try:
                    check_space = self.__getitem__(shifted_coord)  # Try to get an adjacent space
                except IndexError:
                    continue  # Doing this naively, so we might go off the board, in which case we skip
                else:
                    _neighbors.append(check_space)  # o.w. we append the space to the neighbors

            space.neighbors = _neighbors  # Set the Space's neighbors


class DisplayBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def reveal_neighbors(self, space: Space):
        """
        When a space is revealed, display the number of adjacent mines.
        If the space has no adjacent mines, keep checking neighbors until all spaces have at least one adjacent mine.
        For instance:
            O O O
            O O X
            O O O
        If the user uncovered the bottom-right space, a Hint of '1' would be uncovered.
            O O O
            O O X
            O O 1
        However, if the user were to uncover the top-left space,
        the game should continue revealing spaces until a space either has a Hint displayed or
        its neighbors are revealed or display their hint
            [] [] 1
            [] 1  X
            [] 1  O
        :return:
        """
        if space.hint != 0:
            pass
        pass
