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
		""" Function 'fill_array' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "fill_array", 1)
			
	def test_function_behaviour1(self):
		""" Answer [0] with input 1, 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(1,0).tolist(), [0])
			
	def test_function_behaviour2(self):
		""" Answer [1] with input 1, 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(1,1).tolist(), [1])
			
	def test_function_behaviour3(self):
		""" Answer [3, 3, 3] with input 3, 3 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(3,3).tolist(), [3, 3, 3])
			
	def test_function_behaviour4(self):
		""" Answer [2, 2, 2, 2, 2] with input 5, 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(5,2).tolist(), [2, 2, 2, 2, 2])
			
	def test_function_behaviour5(self):
		""" Answer [3.4, 3.4, 3.4, 3.4, 3.4, 3.4] with input 6, 3.4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(6,3.4).tolist(), [3.4, 3.4, 3.4, 3.4, 3.4, 3.4])
			
	def test_function_behaviour6(self):
		""" Answer [-8, -8, -8, -8, -8] with input 5, -8 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.fill_array(5,-8).tolist(), [-8, -8, -8, -8, -8])
		
			
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
