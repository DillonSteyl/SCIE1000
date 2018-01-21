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
			
	def test_input_exists(self):
		""" Takes some number as input """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_called_once()

	def test_true_1(self):
		""" Prints the message 'Don't be so negative!' if the input is less than 0 (1) """
		user_input = "-0.2"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "Don't be so negative!")
				
	def test_true_2(self):
		""" Prints the message 'Don't be so negative!' if the input is less than 0 (2) """
		user_input = "-23"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "Don't be so negative!")
				
	def test_false_1(self):
		""" Prints nothing if the input is not less than 0 (1) """
		user_input = "0"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")
				
	def test_false_2(self):
		""" Prints nothing if the input is not less than 0 (2) """
		user_input = "12"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)