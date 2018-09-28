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
		""" User enters [1, 0] and the program prints 'Hey, how are you?' before exiting"""
		user_input = ["1","0"]
		expected = "Hey, how are you?"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testnumexit(self):
		""" User enters [2, 5, 0] and the program asks for a number, prints it, then exits """
		user_input = ["2", "5", "0"]
		expected = "Hey, how are you?"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
				
				
				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
