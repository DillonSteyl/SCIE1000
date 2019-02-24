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
		""" Function 'calculate_age' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "calculate_age", 1)
		
	def test_1(self):
		""" The function returns the value 11460 with input 25 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.calculate_age(25), 11460)
			
	def test_2(self):
		""" The function returns the value 5730 with input 50 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.calculate_age(50), 5730)
			
	def test_3(self):
		""" The function returns the value 17190 with input 12.5 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(attempt.calculate_age(12.5), 17190)
			
	def test_4(self):
		""" The function returns the value 13728.671315377427 with input 19 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertAlmostEqual(attempt.calculate_age(19), 13728.671315377427)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
