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
        self._hint = 0
        self._loc = loc
        self._neighbors: List[Space] = []

    def add_hint(self) -> None:
        """
        Increase the hint counter
        :return: None
        """
        if self._hint == 6:
            raise RuntimeError("More than six adjacent mines is impossible, wtf is going on?")
        else:
            self._hint += 1

    def copy(self):
        """
        Create a copy of the space
        :return:
        """
        return Space(contents=self._content, loc=self._loc)

    @property
    def item(self):
        return self._content

    @item.setter
    def item(self, new_item: Asset, /):
        self._content = new_item

    def is_empty(self) -> bool:
        return type(self._content).__name__ == "_Empty"

    def is_flag(self) -> bool:
        return type(self._content).__name__ == "_Flag"

    def is_mine(self) -> bool:
        return type(self._content).__name__ == "_Mine"

    def is_revealed(self) -> bool:
        return type(self._content).__name__ == "_Revealed"

    @property
    def loc(self) -> Tuple[int, int]:
        """ Return tuple of coordinates for the space on the board"""
        return self._loc

    def make_empty(self):
        self._content = Empty

    def make_flag(self):
        self._content = Flag

    def make_mine(self):
        self._content = Mine

    def make_revealed(self):
        self._content = Revealed

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, nbrs: List, /):
        if not all(isinstance(i, self.__class__) for i in nbrs):
            raise TypeError("Neighbors must all be instances of Space")
        else:
            self._neighbors = nbrs

    def __repr__(self):
        return repr(self._content)
