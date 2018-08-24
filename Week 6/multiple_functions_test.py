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

	def test_tokilos_defined(self):
		""" Function 'toKilograms' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "toKilograms", 1)
			
	def test_mars_defined(self):
		""" Function 'weightOnMars' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "weightOnMars", 1)
			
	def test_moon_defined(self):
		""" Function 'weightOnMoon' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "weightOnMoon", 1)
			
	def test_function_behaviour1(self):
		""" Answer 1 with call toKilograms(2.2) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.toKilograms(2.2)
			self.assertEqual(a, 1.0)
			
	def test_function_behaviour2(self):
		""" Answer 70.0 with call toKilograms(154) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.toKilograms(154)
			self.assertEqual(a, 70.0)
			
	def test_function_behaviour1(self):
		""" Answer 0.16 with call weightOnMoon(2.2) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.weightOnMoon(2.2)
			self.assertEqual(a, 0.16)
			
	def test_function_behaviour1(self):
		""" Answer 0.38 with call weightOnMars(2.2) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.weightOnMars(2.2)
			self.assertEqual(a, 0.38)
			
	def test_function_behaviour1(self):
		""" Answer 8.16 with call weightOnMoon(112.2) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.weightOnMoon(112.2)
			self.assertEqual(a, 8.16)
			
	def test_function_behaviour1(self):
		""" Answer 19.38 with call weightOnMars(112.2) """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			a = attempt.weightOnMars(112.2)
			self.assertEqual(a, 19.38)
			
	


				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
