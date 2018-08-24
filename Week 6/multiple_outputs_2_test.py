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

	def test_linear_defined(self):
		""" Function 'getLinearEquation' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "getLinearEquation", 4)
			
	def test_exponential_defined(self):
		""" Function 'getExponentialEquation' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "getExponentialEquation", 4)
		
	def test_linear_behaviour2(self):
		""" Function 'getLinearEquation' outputs 1.0, 1.0 with input 1,2,3,4 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a,b = attempt.getLinearEquation(1,2,3,4)
			self.assertEqual([a,b], [1.0, 1.0])
						
	def test_linear_behaviour1(self):
		""" Function 'getLinearEquation' outputs 5.0, 7.5 with input 4.5, 30, 5.5, 35 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a,b = attempt.getLinearEquation(4.5, 30, 5.5, 35)
			self.assertEqual([a,b], [5.0, 7.5])
			
	def test_exponential_behaviour1(self):
		""" Function 'getExponentialEquation' outputs 100, -0.06931 with input 0, 100, 10, 50"""
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a,b = attempt.getExponentialEquation(0, 100, 10, 50)
			self.assertEqual([a,b], [100.0, -0.06931])
			
			
	def test_exponential_behaviour2(self):
		""" Function 'getExponentialEquation' outputs 3.0, 0.10986 with input 10, 10, 20, 30"""
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a,b = attempt.getExponentialEquation(10, 10, 20, 30)
			self.assertEqual([a,b], [3.0, 0.10986])
			

	def test_output1(self):
		""" Program prints the correct values -1.0 and 5.0 with input -5, 10, 5, 0, and 1"""
		user_input = ["-5", "10", "5", "0", "1"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "The value of m is -1.0 and the value of c is 5.0\nThanks for using this program!"
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output2(self):
		""" Program prints the correct values 10000.0 and 0.01833 with input 0, 10000, 50, 25000 and 0"""
		user_input = ["0", "10000", "50", "25000", "0"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "The value of A0 is 10000.0 and the value of k is 0.01833\nThanks for using this program!"
				self.assertEqual(output.getvalue().strip(), expected)
				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
