import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from unittest.mock import patch, call

import attempt

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass

	def test_X_var(self):
		""" X array has not been modified """
		self.assertEqual(attempt.X.tolist(), arange(0,2*pi,0.1).tolist())
		
	def test_Y_var(self):
		""" Y array contains the correct values """
		self.assertEqual(attempt.Y.tolist(), sin(attempt.X).tolist())
		
	def test_plot_called(self):
		""" plot function called - only works if matplotlib.pyplot.plot is called, not just 'plot' """
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
