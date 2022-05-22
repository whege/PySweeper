__doc__ = """Classes for the contents of each space on the board """
__author__ = """whege"""
__all__ = ["Asset", "Flag", "Hint", "Mine", "Empty", "Revealed"]

_unicode_box = "\u25A1"
_unicode_flag = "\u2690"
_unicode_space = "\u2002"
_unicode_star = "\u2735"

_BLUE = '\033[34m{}\033[0m'
_GREEN = '\033[32m{}\033[0m'
_ORANGE = '\033[33m{}\033[0m'
_RED = '\033[31m{}\033[0m'


class Asset:
    __slots__ = (
        "_char",
        "_color"
    )

    def __init__(self, unicode_rep: str, color: str = "{}"):
        self._char = unicode_rep
        self._color = color

    def __repr__(self) -> str:
        return self._color.format(self._char)


class _Empty(Asset):
    def __init__(self, space_icon=_unicode_box, /):
        super(_Empty, self).__init__(space_icon, color=_GREEN)


class _Flag(Asset):
    def __init__(self, flag_icon=_unicode_flag, /):
        super(_Flag, self).__init__(flag_icon, color=_BLUE)


class Hint(Asset):
    def __init__(self, num_neighbors: int = 0):
        super(Hint, self).__init__(str(num_neighbors), color=_ORANGE)

    @property
    def count(self):
        return self._char

    @count.setter
    def count(self, ct, /) -> None:
        self._char = str(ct)

    def __eq__(self, other: int or str):
        if not isinstance(other, (int, str)):
            raise TypeError

        return self._char == str(other)


class _Mine(Asset):
    def __init__(self, mine_icon=_unicode_star, /):
        super(_Mine, self).__init__(mine_icon, color=_RED)


class _Revealed(Asset):
    def __init__(self, icon=_unicode_space, /):
        super(_Revealed, self).__init__(icon)


Empty = _Empty()
Flag = _Flag()
Mine = _Mine()
Revealed = _Revealed()
