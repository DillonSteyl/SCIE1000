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
		""" Function 'factorial' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "factorial", 1)
			
	def test_function_behaviour1(self):
		""" Answer 1 with input 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(1)
			self.assertEqual(n, 1)

	def test_function_behaviour2(self):
		""" Answer 2 with input 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(2)
			self.assertEqual(n, 2)
			
	def test_function_behaviour3(self):
		""" Answer 6 with input 3 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(3)
			self.assertEqual(n, 6)
			
	def test_function_behaviour4(self):
		""" Answer 24 with input 4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(4)
			self.assertEqual(n, 24)
			
	def test_function_behaviour5(self):
		""" Answer 120 with input 5 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(5)
			self.assertEqual(n, 120)
			
	def test_function_behaviour6(self):
		""" Answer 720 with input 6 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(6)
			self.assertEqual(n, 720)
			
	def test_function_behaviour7(self):
		""" Answer 5040 with input 8 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(8)
			self.assertEqual(n, 5040)
			
	def test_function_behaviour8(self):
		""" Answer 40320 with input 8 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(8)
			self.assertEqual(n, 40320)
			
	def test_function_behaviour9(self):
		""" Answer 362880 with input 9 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(9)
			self.assertEqual(n, 362880)
			
	def test_function_behaviour10(self):
		""" Answer 3628800 with input 10 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(10)
			self.assertEqual(n, 3628800)
			
	def test_function_behaviour0(self):
		""" Answer 1 with input 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			n = attempt.factorial(0)
			self.assertEqual(n, 1)
	
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
