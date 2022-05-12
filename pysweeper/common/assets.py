__doc__ = """Classes for the contents of each space on the board """
__author__ = """whege"""
__all__ = ["Asset", "Flag", "Hint", "Mine", "Empty", "Revealed"]

_unicode_box = "\u25A1"
_unicode_flag = "\u2690"
_unicode_space = "\u2002"
_unicode_star = "\u2735"


class Asset:
    __slots__ = (
        "_char"
    )

    def __init__(self, unicode_rep: str):
        self._char = unicode_rep

    def __repr__(self) -> str:
        return self._char


class _Empty(Asset):
    def __init__(self, space_icon=_unicode_box, /):
        super(_Empty, self).__init__(space_icon)


class _Flag(Asset):
    def __init__(self, flag_icon=_unicode_flag, /):
        super(_Flag, self).__init__(flag_icon)


class Hint(Asset):
    def __init__(self, num_neighbors: int = 0):
        super(Hint, self).__init__(str(num_neighbors))

    @property
    def count(self):
        return self._char

    @count.setter
    def count(self, ct, /) -> None:
        self._char = str(ct)


class _Mine(Asset):
    def __init__(self, mine_icon=_unicode_star, /):
        super(_Mine, self).__init__(mine_icon)


class _Revealed(Asset):
    def __init__(self, icon=_unicode_space, /):
        super(_Revealed, self).__init__(icon)


Empty = _Empty()
Flag = _Flag()
Mine = _Mine()
Revealed = _Revealed()
