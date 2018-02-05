import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *

import attempt

class Tests(PythonTestCase):

	def test_X_var(self):
		""" X array contains the correct values """
		self.assertEqual(attempt.X.tolist(), arange(-3, 3.1, 0.1).tolist() )
		
	def test_Y_var(self):
		""" Y array contains the correct values """
		self.assertEqual(attempt.Y.tolist(), (attempt.X**3).tolist() )
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
