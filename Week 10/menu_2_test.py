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
			
	def testearlyexit(self):
		""" User enters 0 and the program exits without printing anything."""
		user_input = "0"
		expected = ""
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testhiexit(self):
		""" User enters [1, 0] and the program greets the user before exiting"""
		user_input = ["1","0"]
		expected = "Hey, how are you?"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testnumexit(self):
		""" User enters [2, 5, 0] and the program asks for a number, prints it, then exits """
		user_input = ["2", "5", "0"]
		expected = "Wow! 5.0 is a great number!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
	def testnumhiexit(self):
		""" User enters [2, 5, 1, 0] and the program asks for a number, prints it, greets the user, then exits """
		user_input = ["2", "5", "1", "0"]
		expected = "Wow! 5.0 is a great number!\nHey, how are you?"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
				
	def testhi11exit(self):
		""" User enters [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0] and the program greets the user 11 times, then exits """
		user_input = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0"]
		expected = "Hey, how are you?\n"*10 + "Hey, how are you?"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	
	def testnum3exit(self):
		""" User enters [2, 5, 2, 8, 2, -132, 0] and the program asks and prints the users favourite number 3 times, then exits """
		user_input = ["2", "5", "2", "8", "2", "-132", "0"]
		expected = "Wow! 5.0 is a great number!\nWow! 8.0 is a great number!\nWow! -132.0 is a great number!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
				
				
				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
