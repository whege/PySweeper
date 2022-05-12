__doc__ = """ Main game class """
__author__ = """whege"""
__all__ = ["Game"]

import re
from typing import Tuple

from board import *
from common import *


class Game:
    _Difficulties = {
        "Easy": Easy,
        "Medium": Medium,
        "Insane": Insane
    }

    def __init__(self):
        settings = self._get_settings()
        self._answers = AnswerBoard(settings.width, settings.height, settings.mines)
        self._display = DisplayBoard(settings.width, settings.height)

    @staticmethod
    def _get_settings() -> Difficulty:
        """
        Handles user input for game setup and returns the Difficulty chosen
        :return:
        """
        while True:
            choices = Game._Difficulties.keys()
            difficulty = str(input(f"Select a difficulty: {', '.join(choices)} ")).capitalize()

            if difficulty in choices:
                return Game._Difficulties[difficulty]

            else:
                print("Invalid choice! Select again...")
                continue

    def _handle_flag(self, coord: Tuple[int, int]) -> bool:
        """
        If the user flags a spot, convert the icon in that spot to a flag
        :param coord: Location on the board where the flag will be placed
        :return: None
        """
        space = self._display[coord]
        space.make_flag()
        self._display[coord] = space
        return True

    def _handle_input(self) -> bool:
        """
        Accept and handle input from the user
        :return: Boolean indicating if the game is active or not
        """
        action = str(input("Enter a command (R to reveal or F to flag), followed by a coordinate x, y: "))
        action, coord = action[:1], action[1:].strip()

        if action not in ["R", "F"]:
            print("Command not recognized! Try again...")
            self._handle_input()

        elif not re.fullmatch(r'\d,\s?\d', coord):
            print("Coordinate format not recognized, try again...")
            self._handle_input()

        x_coord, y_coord = tuple(map(lambda x: int(x.strip()), coord.split(',')))

        if action == "R":
            self._handle_reveal((y_coord, x_coord))

        elif action == "F":
            self._handle_flag((y_coord, x_coord))

        else:
            raise RuntimeError

    def _handle_reveal(self, coord: Tuple[int, int]) -> bool:
        """
        If the user has opted to reveal a space, handle the revelation
        :param coord: Tuple coordinate of the space to reveal
        :return: Boolean indicating if the game is still going
        """
        space = self._answers[coord]

        if space.is_mine():
            space.make_mine()
            playing = False

        elif space.is_flag():
            playing = True

        else:
            space.make_revealed()
            playing = False

        self._display[coord] = space

    def play(self) -> None:
        """
        Main game loop
        :return: None
        """
        self._display.show()  # show the board to start the game

        while True:
            still_playing = self._handle_input()
            self._display.show()


if __name__ == '__main__':
    g = Game()
    g.play()
