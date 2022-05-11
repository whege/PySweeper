__doc__ = """ Constants for game difficulties """
__author__ = """William Hegedusich"""
__all__ = ["Difficulty", "Easy", "Medium", "Insane"]

from collections import namedtuple

Difficulty = namedtuple("Difficulty", ["width", "height", "mines"])
Easy = Difficulty(9, 9, 10)
Medium = Difficulty(16, 16, 40)
Insane = Difficulty(16, 16, 99)
