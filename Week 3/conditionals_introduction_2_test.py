from python_test_case import PythonTestCase, run_tests
from pylab import *
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

	def test_true(self):
		""" Prints the message 'Don't be so negative!' if the input is less than 0 """
		user_input = str(randint(-100,0)) # random negative number >-100
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "Don't be so negative!")
				
	def test_false_1(self):
		""" Prints nothing if the input is 0 """
		user_input = "0"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")
				
	def test_false_2(self):
		""" Prints nothing if the input is greater than 0 """
		user_input = str(randint(0,100)) # random number between 0 and 100
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)