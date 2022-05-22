__doc__ = """ Entry point for the game """
__author__ = """ whege """
__all__ = []

from .game import Game


def main():
    Game().play()


if __name__ == "__main__":
    main()
