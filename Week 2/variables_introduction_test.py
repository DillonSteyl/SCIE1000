from python_test_case import PythonTestCase, run_tests
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from os import devnull
import io

f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):

	def test_variables_defined(self):
		""" Ensure that width and height are defined """
		self.assertDefined(attempt, 'width', int)
		self.assertDefined(attempt, 'height', int)
	
	def test_variables_values(self):
		""" Ensure that the width, height and area variables have the correct values """
		self.assertEqual(attempt.width, 13)
		self.assertEqual(attempt.height, 22)
		self.assertEqual(attempt.area, 13*22)

if __name__ == "__main__":
    run_tests(Tests)
