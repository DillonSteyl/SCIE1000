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
			
	def test_true_1(self):
		""" Prints 'You are not tall enough to ride' when height is less than 130 (1)"""
		user_input = "112"
		expected = "You are not tall enough to ride!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_true_2(self):
		""" Prints 'You are not tall enough to ride' when height is less than 130 (2)"""
		user_input = "129"
		expected = "You are not tall enough to ride!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_false_1(self):
		""" Prints nothing if height is not less than 130 (1)"""
		user_input = "130"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")
				
	def test_false_2(self):
		""" Prints nothing if height is not less than 130 (2)"""
		user_input = "156"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
