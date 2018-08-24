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
		""" Function 'toCentimetres' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "toCentimetres", 1)
		
	def test_function_behaviour(self):
		""" Function 'toCentimetres' behaves as expected """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			test_val = randint(60,80)
			self.assertEqual(attempt.toCentimetres(test_val), test_val*2.54)
