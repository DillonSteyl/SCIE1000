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
			
	def test_function_knapsack(self):
		""" Function 'knapsack' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "knapsack", 3)
		
	def test_function1(self):
		""" Function vpw returns 2.5 with input V = [3,5,2], W = [6,2,1] and i = 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,2],[6,2,1],1), 2.5)
			
	def test_function2(self):
		""" Function vpw returns 0.5 with input V = [3,5,2], W = [6,2,1] and i = 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,2],[6,2,1],0),0.5)
			
	def test_function3(self):
		""" Function vpw returns 2 with input V = [3,5,2], W = [6,2,1] and i = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.vpw([3,5,2],[6,2,1],2), 2)
			
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
			self.assertEqual(attempt.best_item([3,5,2],[6,2,1],0), -1)
			
	def test_function7(self):
		""" Function best_item returns 2 with input V = [3,5,2], W = [6,2,1] and space = 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([3,5,2],[6,2,1],1), 2)
			
	def test_function8(self):
		""" Function best_item returns 1 with input V = [3,5,2], W = [6,2,1] and space = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([3,5,2],[6,2,1],2), 1)
			
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
			
	def test_function11(self):
		""" Function best_item returns 0 with input V = [4,7], W = [2,3] and space = 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.best_item([4,7],[2,3],2), 0)
			
	def test_knapsack1(self):
		""" Knapsack function has correct output for example scenario 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.knapsack([5, 11, 7],[2,4,3],5)
			self.assertEqual(a.tolist(), [11])
			self.assertEqual(b.tolist(), [4])
			self.assertEqual(c, 11)
			
	def test_knapsack2(self):
		""" Knapsack function has correct output for example scenario 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.knapsack([1, 3, 4, 5, 6, 7],[20, 1, 2, 1, 2, 3],6)
			self.assertEqual(a.tolist(), [5, 6, 3, 4])
			self.assertEqual(b.tolist(), [1, 2, 1, 2])
			self.assertEqual(c, 18)
			
	def test_knapsack3(self):
		""" Knapsack function has correct output for example scenario 3 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.knapsack([25, 64, 16, 4],[4, 8, 3.5, 1],16.5)
			self.assertEqual(a.tolist(), [64, 25, 16, 4])
			self.assertEqual(b.tolist(), [8, 4, 3.5, 1])
			self.assertEqual(c, 109)
			
	def test_knapsack5(self):
		""" Knapsack function has correct output for example scenario 4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.knapsack([15, 13, 13, 12, 11, 9, 9, 9, 4, 3, 2],[5, 2, 7, 3, 5, 2, 4, 6, 1, 1, 1],10)
			self.assertEqual(a.tolist(), [13, 9, 4, 12, 3, 2])
			self.assertEqual(b.tolist(), [2, 2, 1, 3, 1, 1])
			self.assertEqual(c, 43)
			
	def test_knapsack4(self):
		""" Knapsack function has correct output for a mystery scenario """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.knapsack([15, 13, 13, 12, 11, 9, 9, 9, 4, 3, 2, 64, 16, 4, 25],[5, 2, 7, 3, 5, 2, 4, 6, 1, 1, 1, 4, 8, 3.5, 1],20)
			self.assertEqual(a.tolist(), [25.0, 64.0, 13.0, 9.0, 4.0, 12.0, 3.0, 15.0, 2.0])
			self.assertEqual(b.tolist(), [1.0, 4.0, 2.0, 2.0, 1.0, 3.0, 1.0, 5.0, 1.0])
			self.assertEqual(c, 147)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
