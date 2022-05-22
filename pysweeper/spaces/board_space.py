__doc__ = """ Class for each space on the board """
__author__ = """whege"""
__all__ = ["Space"]

from typing import List, Tuple

from common.assets import *


class Space:
    __slots__ = (
        "_content",
        "_hint",
        "_loc",
        "_neighbors"
    )

    def __init__(self, contents: Asset, loc: Tuple[int, int]):
        self._content: Asset = contents
        self._hint: Hint = Hint()
        self._loc = loc
        self._neighbors: List[Space] = []

    @property
    def hint(self):
        """
        Set the number of spaces adjacent to the current space that contain a mine
        :return:
        """
        return int(self._hint.count)

    @hint.setter
    def hint(self, num):
        """
        Set the number of spaces adjacent to the current space that contain a mine
        :param num:
        :return:
        """
        self._hint.count = num

    @property
    def item(self):
        """
        Get the content of the space
        :return:
        """
        return self._content

    @item.setter
    def item(self, new_item: Asset, /):
        """
        Change the item's content
        :param new_item:
        :return:
        """
        self._content = new_item

    @property
    def loc(self) -> Tuple[int, int]:
        """ Return tuple of coordinates for the space on the board"""
        return self._loc

    @property
    def neighbors(self):
        """
        Get all spaces adjacent to the current space
        :return:
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, nbrs: List, /):
        """
        Set the current space's neighboring spaces
        :param nbrs:
        :return:
        """
        if not all(isinstance(i, self.__class__) for i in nbrs):
            raise TypeError("Neighbors must all be instances of Space")
        else:
            self._neighbors = nbrs

    def is_empty(self) -> bool:
        """
        Check if the space is empty
        :return:
        """
        return type(self._content).__name__ == "_Empty"

    def is_flag(self) -> bool:
        """
        Check if the space has been flagged
        :return:
        """
        return type(self._content).__name__ == "_Flag"

    def is_mine(self) -> bool:
        """
        Check if the space is a mine
        :return:
        """
        return type(self._content).__name__ == "_Mine"

    def is_revealed(self) -> bool:
        """
        Check if the space has been revealed
        :return:
        """
        return type(self._content).__name__ == "_Revealed"

    def make_empty(self):
        """
        convert the space to empty
        :return:
        """
        self._content = Empty

    def make_flag(self):
        """
        Convert the space to a flag
        :return:
        """
        self._content = Flag

    def make_mine(self):
        """
        Convert the space to a mine
        :return:
        """
        self._content = Mine

    def make_revealed(self):
        self._content = Revealed

    def show_hint(self):
        """
        Show the number of mines adjacent to the space
        :return:
        """
        self._content = self._hint

    def __repr__(self):
        """
        Return the content of the space as a string
        :return:
        """
        return repr(self._content)
