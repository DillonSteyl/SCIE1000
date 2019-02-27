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
		""" Function 'vpw' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "vpw", 3)
		
	def test_function1(self):
		""" Function returns 2.5 with input V = [3,5,2], W = [6,2,1] and i = 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],1), 2.5)
			
	def test_function2(self):
		""" Function returns 0.5 with input V = [3,5,2], W = [6,2,1] and i = 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],0),0.5)
			
	def test_function3(self):
		""" Function returns 2 with input V = [3,5,2], W = [6,2,1] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],2), 2)
			
	def test_function4(self):
		""" Function returns 3/7 with input V = [7,6,5,4,3], W = [3,4,5,6,7] and i = 4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.vpw([7,6,5,4,3],[3,4,5,6,7],4), 3/7)
			
	def test_function5(self):
		""" Function returns 1 with input V = [7,6,5,4,3], W = [3,4,5,6,7] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.vpw([7,6,5,4,3],[3,4,5,6,7],2), 1)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests
