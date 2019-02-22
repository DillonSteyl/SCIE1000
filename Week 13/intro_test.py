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
		""" Function 'toCentimetres' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "toCentimetres", 1)
		
	def test_function_behaviour(self):
		""" Function 'toCentimetres' behaves as expected """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			test_val = randint(60,80)
			self.assertEqual(attempt.toCentimetres(test_val), test_val*2.54)

	def test_output(self):
		""" Correctly uses the toCentimetres function to convert the inputted height """
		user_input = randint(50,90)
		with patch("builtins.input", return_value=str(user_input)) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "You are " + str(attempt.toCentimetres(user_input)) + " cm tall!"
				self.assertEqual(output.getvalue().strip(), expected)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
