
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

	def test_IBW_defined(self):
		""" Function 'IBW' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "IBW", 2)
		
	def test_ibw_behaviour1(self):
		""" Function 'IBW' outputs 61.7 with input 1, 170 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			aattempt.getLinearEquation(1,170)
			self.assertEqual(a, 61.7)
			
	def test_ibw_behaviour2(self):
		""" Function 'IBW' outputs 66.2 with input 0, 170 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			aattempt.getLinearEquation(0,170)
			self.assertEqual(a, 66.2)
			
	def test_output1(self):
		""" Program prints the correct value 57.2 with input 0, 160"""
		user_input = ["0", "160"]
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "Ideal weight: 57.2 kg."
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output2(self):
		""" Program prints the correct value 52.7 with input 1, 160"""
		user_input = ["1", "160"]
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "Ideal weight: 52.7 kg."
				self.assertEqual(output.getvalue().strip(), expected)
				

				
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
