__doc__ = """Classes for the contents of each space on the board """
__author__ = """William Hegedusich"""
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


class Empty(Asset):
    def __init__(self, space_icon=_unicode_box, /):
        super().__init__(space_icon)


class Flag(Asset):
    def __init__(self, flag_icon=_unicode_flag, /):
        super().__init__(flag_icon)


class Hint(Asset):
    def __init__(self, num_neighbors: int):
        super(Hint, self).__init__(str(num_neighbors))


class Mine(Asset):
    def __init__(self, mine_icon=_unicode_star, /):
        super().__init__(mine_icon)


class Revealed(Asset):
    def __init__(self, icon=_unicode_space, /):
        super().__init__(icon)
