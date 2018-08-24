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
		""" Function 'how_many' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "how_many", 2)
			
	def test_function_behaviour1(self):
		""" Answer 1 with input [1], 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([1], 1)
			self.assertEqual(a, 1)
			
			
	def test_function_behaviour2(self):
		""" Answer 2 with input [1,1], 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([1,1], 1)
			self.assertEqual(a, 2)
			
	def test_function_behaviour3(self):
		""" Answer 1 with input [0, 5, 7, 2, 6, 8], 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([0,5,7,2,6,8], 2)
			self.assertEqual(a, 1)
			
	def test_function_behaviour4(self):
		""" Answer 3 with input [0, 5, 6, 7, 2, 6, 6, 8], 6 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([0, 5, 6, 7, 2, 6, 6, 8], 6)
			self.assertEqual(a, 3)
			
	def test_function_behaviour5(self):
		""" Answer 0 with input [0, 5, 6, 7, 2, 6, 6, 8], 3 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([0, 5, 6, 7, 2, 6, 6, 8], 3)
			self.assertEqual(a, 0)
			
			
	def test_function_behaviour5(self):
		""" Answer 2 with input [8, 5, 6, 7, 2, 6, 6, 8], 8 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a= attempt.how_many([8, 5, 6, 7, 2, 6, 6, 8], 8)
			self.assertEqual(a, 2)
			
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
