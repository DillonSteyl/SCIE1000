import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from unittest.mock import patch, call
import unittest
from io import StringIO

import attempt

class Tests(PythonTestCase):

	def test_X_var(self):
		""" X array contains the correct values """
		self.assertEqual(attempt.X.tolist(), arange(-2*pi, 2*pi, 0.1).tolist() )
		
	def test_Y1_var(self):
		""" Y1 array contains the correct values """
		self.assertEqual(attempt.Y1.tolist(), (attempt.X**2).tolist() )
		
	def test_Y2_var(self):
		""" Y2 array contains the correct values """
		self.assertEqual(attempt.Y2.tolist(), (attempt.X**2 + sin(12*attempt.X)).tolist() )
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
