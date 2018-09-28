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

	def test_function_defined(self):
		""" Function 'gcd' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "gcd", 2)
		
	def test32and48(self):
		""" Function returns 16 with input (32, 48). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(32, 48)
			self.assertEqual(a, 16)

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
