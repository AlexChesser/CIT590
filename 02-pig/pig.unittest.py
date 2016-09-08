import unittest
from pig import *

class NameOfClass(unittest.TestCase):

# You can define variables
# and functions here
# Test methods go here--
# the name of each test method
# begins with “test_”

# def main():
    """This is where your program will start execution. """
# def instructions():
    """Tell the user the rules of the game. """
# def human_move(computer_score, human_score):
    """
Tells the user both her current score and the computer's score, and how far behind (or ahead) she is.
Then repeatedly asks whether the user wants to roll again. This continues until either:
The user decides not to roll again. The function should return the total of the rolls made
during this move. The user rolls a 1. The function should return 0.
    """

# def computer_move(computer_score, human_score):
    """
The computer rolls some number of times, displays the result of each roll, and the function returns
the result (either 0 or the total of the rolls). The function may use its parameters in order to
play more intelligently (for example, it may wish to gamble more agressively if it is behind).
    """
# def is_game_over(computer_score, human_score):
    """Returns True if either player has 100 or more, and the players are not tied,
otherwise it returns False. (Call this  only after the human's move.)   """
    def test_is_game_over(self):
        self.assertTrue(is_game_over(100, 50))
        self.assertTrue(is_game_over(50, 100))
        self.assertFalse(is_game_over(50, 50))
        self.assertFalse(is_game_over(100, 100))
        self.assertFalse(is_game_over(1000, 1000))

# def roll():
    """Returns a random number in the range 1 to 6, inclusive. To do this, find the random module on https://docs.python.org/3/library/index.html and follow the link to find the randint method.   """
# def ask_yes_or_no(prompt):
    """Prints the prompt as a question to the user, for example, "Roll again? ". If the user responds with a string whose first character is 'y' or 'Y', the function returns True. If the user responds with a string whose first character is 'n' or 'N', the function returns False. Any other response will cause the question to be repeated until the user provides an acceptable response.   """
# def show_results(computer_score, human_score):
    """Tells whether the human won or lost, and by how much. (Call this when the game has ended.)   """





unittest.main()