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
		""" Function 'primes' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "primes", 1)
			
	def test_function_behaviour1(self):
		""" Answer -1, -1 with input 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(1)
			self.assertEqual([a,b], [-1, -1])
			
	def test_function_behaviour2(self):
		""" Answer -1, -1 with input -3 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(-3)
			self.assertEqual([a,b], [-1, -1])
			
	def test_function_behaviour3(self):
		""" Answer 2, 3 with input 6 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(6)
			self.assertEqual([a,b], [2, 3])
			
	def test_function_behaviour4(self):
		""" Answer 3, 5 with input 15 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(15)
			self.assertEqual([a,b], [3, 5])
			
	def test_function_behaviour5(self):
		""" Answer 5, 13 with input 65 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(65)
			self.assertEqual([a,b], [5, 13])
			
	def test_function_behaviour6(self):
		""" Answer 17, 29 with input 493 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(493)
			self.assertEqual([a,b], [17, 29])
			
	def test_function_behaviour7(self):
		""" Answer 11, 23 with input 253 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b= attempt.primes(253)
			self.assertEqual([a,b], [11, 23])

	
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
