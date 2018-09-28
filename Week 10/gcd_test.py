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
			
	def test15and25(self):
		""" Function returns 5 with input (15, 25). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(15, 25)
			self.assertEqual(a, 5)
			
	def test21and7(self):
		""" Function returns 7 with input (21, 7). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(21, 7)
			self.assertEqual(a, 7)
			
	def test9and5(self):
		""" Function returns 1 with input (9, 5). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(9, 5)
			self.assertEqual(a, 1)
			
	def test8and12(self):
		""" Function returns 4 with input (8, 12). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(8, 12)
			self.assertEqual(a, 4)
			
	def testbig2(self):
		""" Function returns 992250000 with input (74418750000, 5445468000000). """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.gcd(74418750000, 5445468000000)
			self.assertEqual(a, 992250000)
			


# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
