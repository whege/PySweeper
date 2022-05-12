__doc__ = """ Main game class """
__author__ = """whege"""
__all__ = ["Game"]

import re
import sys
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
        self._flag_locs = []  # Variable for storing the coordinates a user has flagged
        # Store location of all mines
        self._mine_locs = sorted(
            [s.loc for s in self._answers if s.is_mine()], key=lambda x: x[0]
        )
        self._win = False  # Flag for whether use has won

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
        space = self._display[coord].copy()  # Get the Space to be flagged
        space.make_flag()  # Convert the Space to a flag
        self._display[coord] = space  # Update the space
        self._flag_locs.append(coord)  # Update the flagged locations

        # Check if the locations the user flagged exactly match the mine locations
        if sorted(self._flag_locs, key=lambda x: x[0]) == self._mine_locs:
            self._win = True  # If so, flag a win
            return False  # Return False to end game
        else:
            return True  # Return True to continue game

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

        if (x_coord < 0) or (x_coord > self._answers.width) or (y_coord < 0) or (y_coord > self._answers.height):
            print("That space is out of bounds! Pick again")
            self._handle_input()

        if action == "R":
            return self._handle_reveal((y_coord, x_coord))

        elif action == "F":
            return self._handle_flag((y_coord, x_coord))

        else:
            raise RuntimeError

    def _handle_reveal(self, coord: Tuple[int, int]) -> bool:
        """
        If the user has opted to reveal a space, handle the revelation
        :param coord: Tuple coordinate of the space to reveal
        :return: Boolean indicating if the game is still going
        """
        answer_space = self._answers[coord].copy()
        display_space = self._display[coord].copy()

        if display_space.is_revealed():
            print(f"Space {coord} has already been revealed! Please pick a new space.")
            return True

        elif answer_space.is_mine():  # If the user revealed a mine, display the mine
            display_space.make_mine()
            self._display[coord] = display_space
            return False  # Return False to end the game

        else:
            self._display.reveal_neighbors(answer_space)  # Update the display board to reveal empty spaces
            return True  # Reveal True to continue the game

    def play(self) -> None:
        """
        Main game loop
        :return: None
        """
        self._display.show()  # show the board to start the game

        while True:
            if not self._handle_input():  # Handle user input, which returns True if user is still playing
                break
            self._display.show()  # If the game is still going, show the board again

        print("\n")  # Add space between last line and ending output
        if self._win:
            print("Congrats! You win!", end="\n")
        else:
            print("Game over! ** w o m p  w o m p **", end="\n")

        self._answers.show()  # Show the answers

        sys.exit(0)


if __name__ == '__main__':
    g = Game()
    g.play()
