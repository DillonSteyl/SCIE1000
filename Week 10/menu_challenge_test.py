from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
import random

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
			
				
	def testscenario1(self):
		""" User enters [5, 5, 5] and the program exits with the user not finding the treasure"""
		random.seed(1)
		user_input = ["5", "5", "5"]
		expected = "Your position is 1 1\nYour detector says the treasure is 10 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Sorry, there is no treasure here.\nYou have 2 of your lives remaining.\n"
		expected += "Your position is 1 1\nYour detector says the treasure is 11 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Sorry, there is no treasure here.\nYou have 1 of your lives remaining.\n"
		expected += "Your position is 1 1\nYour detector says the treasure is 10 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Sorry, there is no treasure here.\nYou have 0 of your lives remaining.\n"
		expected += "You are out of lives, better luck next time!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testscenario2(self):
		""" User enters [4, 3, 3, 5] and the program exits with the user finding the treasure after digging once."""
		random.seed(1)
		user_input = ["4", "3", "3", "5"]
		expected = "Your position is 1 1\nYour detector says the treasure is 10 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 10\nYour detector says the treasure is 2 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 2 10\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 3 10\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "You found the treasure!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
				
	def testscenario3(self):
		""" User enters [8, 8, 8, 2, 8, 8, 8, 5] and the program exits with the user finding the treasure, with lots of staying"""
		random.seed(2)
		user_input = ["8", "8", "8", "2", "8", "8", "8", "5"]
		expected = "Your position is 1 1\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 1\nYour detector says the treasure is 1 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 1\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 1\nYour detector says the treasure is 2 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 2\nYour detector says the treasure is 1 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 2\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 2\nYour detector says the treasure is 0 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "Your position is 1 2\nYour detector says the treasure is 1 moves away.\n"
		expected += "Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.\n"
		expected += "You found the treasure!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				

				
				
				
				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
