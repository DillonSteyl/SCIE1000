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
			
	def test_coprime(self):
		""" Input 14 and 1231"""
		user_input = ["14", "1231"]
		expected = "The gcd is 1.0\nThese two numbers are co-prime."
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_big(self):
		""" Input 312119483544 657767616 """
		user_input = ["312119483544", "657767616"]
		expected = "The gcd is 66792.0"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_1_1(self):
		""" Input 1 and 1 """
		user_input = ["1","1"]
		expected = "The gcd is 1.0\nThese two numbers are co-prime."
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)

