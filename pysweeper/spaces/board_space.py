__doc__ = """ Class for each space on the board """
__author__ = """whege"""
__all__ = ["Space"]

from common.assets import *


class Space:
    __slots__ = (
        "_content",
        "_hint"
    )

    def __init__(self, contents: Asset):
        self._content: Asset = contents
        self._hint = 0

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
        return Space(contents=self._content)

    def get_neighbors(self):
        # TODO
        raise NotImplementedError

    @property
    def item(self):
        return self._content

    @item.setter
    def item(self, new_item: Asset, /):
        self._content = new_item

    def is_empty(self) -> bool:
        return isinstance(self._content, Empty)

    def is_flag(self) -> bool:
        return isinstance(self._content, Flag)

    def is_mine(self) -> bool:
        return isinstance(self._content, Mine)

    def is_revealed(self) -> bool:
        return isinstance(self._content, Revealed)

    def make_empty(self):
        self._content = Empty()

    def make_flag(self):
        self._content = Flag()

    def make_mine(self):
        self._content = Mine()

    def make_revealed(self):
        self._content = Revealed()

    @property
    def neighbors(self):
        raise NotImplementedError

    def __repr__(self):
        return repr(self._content)
