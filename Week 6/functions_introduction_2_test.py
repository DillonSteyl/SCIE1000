from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
from io import StringIO
from os import devnull

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass

	def test_function_defined(self):
		""" Function 'double' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "double", 1)
			
	def test_function_behaviour(self):
		""" Function 'double' behaves as expected """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			test_val = randint(0,80)
			self.assertEqual(attempt.double(test_val), test_val*2)

	def test_output(self):
		""" Correctly uses the 'double' function to print double the inputted number """
		user_input = randint(0,100)
		with patch("builtins.input", return_value=str(user_input)) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = str(attempt.double(user_input))
				self.assertEqual(output.getvalue().strip(), expected)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
