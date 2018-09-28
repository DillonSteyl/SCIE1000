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
		""" Function 'convert_to_hours' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "convert_to_hours", 1)
		
	def test135(self):
		""" Function returns (2.0, 15) with input 135 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(135)
			self.assertEqual([a,b], [2.0, 15])
			
	def test35(self):
		""" Function returns (0, 35) with input 35 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(35)
			self.assertEqual([a,b], [0, 35])
			
	def test315(self):
		""" Function returns (5.0, 15) with input 315 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(315)
			self.assertEqual([a,b], [5.0, 15])
			
	def test360(self):
		""" Function returns (6.0, 0) with input 360 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(360)
			self.assertEqual([a,b], [6.0, 0])
			
	def test168(self):
		""" Function returns (2.0, 48) with input 168 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(168)
			self.assertEqual([a,b], [2.0, 48])
			
	def test0(self):
		""" Function returns (0.0, 0) with input 0 """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a, b = attempt.convert_to_hours(0)
			self.assertEqual([a,b], [0.0, 0])


# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
