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
		""" Function 'highest' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "highest", 1)
		
	def test_function_behaviour1(self):
		""" Returns 0 with input [8] """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.toCentimetres([8]), 0)
			
	def test_function_behaviour2(self):
		""" Returns 2 with input [0, 0, 4, 1, 4, 4] """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.toCentimetres([0,0,4,1,4,4]), 2)
			
	def test_function_behaviour3(self):
		""" Returns 4 with input [3.3, 82, 1.46, 1.66, 82.2, 4.354, -13] """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.toCentimetres([3.3, 82, 1.46, 1.66, 82.2, 4.354, -13]), 4)
			
	def test_function_behaviour4(self):
		""" Returns 7 with input [2, 4, 6, 8, 10, 12, 14, 16] """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.toCentimetres([2,4,6,8,10,12,14,16]), 7)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
