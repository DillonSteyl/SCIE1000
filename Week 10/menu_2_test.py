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
		""" User enters [100, 3] and the program exits with a final balance of 103"""
		user_input = ["100","3"]
		expected = "Your balance is 103.0\nYou have closed your bank account with a final balance of 103.0"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testscenario2(self):
		""" User enters [100, 1, 50, 2, 20, 3] and the program exits with a final balance of 103"""
		user_input = ["100","1", "50", "2", "20", "3"]
		expected = "Your balance is 103.0\nYour balance is 157.59\nYour balance is 141.7177\n"
		expected += "You have closed your bank account with a final balance of 141.7177"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testscenario3(self):
		""" User enters [100, 2, 103, 2, 100, 2, 100, 3] and the program exits with a final balance of 103"""
		user_input = ["100","2", "103", "2", "100", "2", "100", "3"]
		expected = "Your balance is 103.0\nYour balance is 0.0\nYour balance is -103.0\nYour balance is -209.09\n"
		expected += "You have closed your bank account with a final balance of -209.09"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				

				
				
				
				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
