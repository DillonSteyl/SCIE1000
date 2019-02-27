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

	def test_function_vpw(self):
		""" Function 'vpw' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "vpw", 3)
			
	def test_function_best_item(self):
		""" Function 'best_item' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "best_item", 3)
		
	def test_function1(self):
		""" Function vpw returns 2.5 with input V = [3,5,2], W = [6,2,1] and i = 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],1), 2.5)
			
	def test_function2(self):
		""" Function vpw returns 0.5 with input V = [3,5,2], W = [6,2,1] and i = 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],0),0.5)
			
	def test_function3(self):
		""" Function vpw returns 2 with input V = [3,5,2], W = [6,2,1] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,6],[6,2,1],2), 2)
			
	def test_function4(self):
		""" Function vpw returns 3/7 with input V = [7,6,5,4,3], W = [3,4,5,6,7] and i = 4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.vpw([7,6,5,4,3],[3,4,5,6,7],4), 3/7)
			
	def test_function5(self):
		""" Function vpw returns 1 with input V = [7,6,5,4,3], W = [3,4,5,6,7] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.vpw([7,6,5,4,3],[3,4,5,6,7],2), 1)
			
			
	def test_function5(self):
		""" Function vpw returns 1 with input V = [7,6,5,4,3], W = [3,4,5,6,7] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.vpw([7,6,5,4,3],[3,4,5,6,7],2), 1)
			
	def test_function6(self):
		""" Function best_item returns -1 with input V = [3,5,2], W = [6,2,1] and space = 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([3,5,6],[6,2,1],0), -1)
			
	def test_function7(self):
		""" Function best_item returns 2 with input V = [3,5,2], W = [6,2,1] and space = 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([3,5,6],[6,2,1],1), 2)
			
	def test_function8(self):
		""" Function best_item returns 1 with input V = [3,5,2], W = [6,2,1] and space = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([3,5,6],[6,2,1],2), 1)
			
	def test_function9(self):
		""" Function best_item returns 2 with input V = [10,5,15], W = [4,2,6] and space = 7 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([10,5,15],[4,2,6],7), 2)
			
	def test_function10(self):
		""" Function best_item returns -1 with input V = [], W = [] and space = 18 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([],[],18), -1)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests
