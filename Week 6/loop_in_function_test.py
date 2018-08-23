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
		""" Function 'powers' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "powers", 1)
			
	def test_function_behaviour1(self):
		""" Answer 0.1, 100, 1000 with input 10 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.powers(10)
			self.assertEqual([a,b,c], [0.1, 100, 1000])

	def test_function_behaviour2(self):
		""" Answer 1, 1, 1 with input 1 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.powers(1)
			self.assertEqual([a,b,c], [1, 1, 1])
      
	def test_function_behaviour3(self):
		""" Answer 0.5, 4, 8 with input 2 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.powers(2)
			self.assertEqual([a,b,c], [0.5, 4, 8])
      
	def test_function_behaviour4(self):
		""" Answer 0.25, 16, 64 with input 4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.powers(4)
			self.assertEqual([a,b,c], [0.25, 16, 64])
      
	def test_function_behaviour5(self):
		""" Answer 0.2, 25, 125 with input 5 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b, c = attempt.powers(5)
			self.assertEqual([a,b,c], [0.2, 25, 125])
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
