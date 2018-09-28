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
		""" Function 'travel' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "travel", 2)
		
	def test0and50(self):
		""" Function returns 1 with input (0, 50). Answer: month 2 -> season 1.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(0, 50)
			self.assertEqual(a, 1)
			
	def test5andneg6(self):
		""" Function returns 0 with input (5, -6). Answer: month 11 -> season 0.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(5, -6)
			self.assertEqual(a, 0)
			
	def test8andneg136(self):
		""" Function returns 1 with input (8, -136). Answer: month 4 -> season 1.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(8, -136)
			self.assertEqual(a, 1)
			
	def test9andneg1(self):
		""" Function returns 0 with input (9, -1). Answer: month 8 -> season 3.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(9, -1)
			self.assertEqual(a, 3)
			
	def test6and0(self):
		""" Function returns 1 with input (6, 0). Answer: month 6 -> season 2.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(6, 0)
			self.assertEqual(a, 2)
			
	def test7and1024(self):
		""" Function returns 1 with input (7, 1024). Answer: month 11 -> season 0.  """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.travel(7, 1024)
			self.assertEqual(a, 0)
			
			

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
