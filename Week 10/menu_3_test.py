from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
			
				
	def testscenario1(self):
		""" User enters [1, 3, 2, 3, 3, 3, 1, 0] and the program exits with a total of 13.0"""
		user_input = ["1", "3", "2", "3", "3", "3", "1", "0"]
		expected = "The total is 0\nThe total is 2.5\nThe total is 5.5\nThe total is 13.0\nThe final total is 13.0"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testscenario2(self):
		""" User enters [2, 5, 3, 2, 1, 2, 6, 0] and the program exits with a total of 11.0"""
		user_input = ["2", "5", "3", "2", "1", "2", "6", "0"]
		expected = "The total is 0\nThe total is 3.0\nThe total is 9.0\nThe total is 11.0\nThe final total is 11.0"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
				
	def testscenario3(self):
		""" User enters [3, 0, 3, 2, 0, 1, 0, 0] and the program exits with a total of 11.5"""
		user_input = ["3", "0", "3", "2", "0", "1", "0", "0"]
		expected = "The total is 0\nThe total is 4.0\nThe total is 8.5\nThe total is 11.5\nThe final total is 11.5"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
