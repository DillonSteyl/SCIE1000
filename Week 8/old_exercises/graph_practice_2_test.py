import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *

import attempt

class Tests(PythonTestCase):

	def test_X_var(self):
		""" X array contains the correct values """
		self.assertEqual(attempt.X.tolist(), arange(0, 10.1, 0.1).tolist() )
		
	def test_Y1_var(self):
		""" Y1 array contains the correct values """
		self.assertEqual(attempt.Y1.tolist(), (-0.2*attempt.X + 2).tolist() )
		
	def test_Y2_var(self):
		""" Y2 array contains the correct values """
		self.assertEqual(attempt.Y2.tolist(), (0.2*attempt.X - 2).tolist() )
		
	def test_Y3_var(self):
		""" Y3 array contains the correct values """
		self.assertEqual(attempt.Y3.tolist(), ((-0.2*attempt.X + 2) * sin(attempt.X)).tolist() )
		
	def test_Y4_var(self):
		""" Y4 array contains the correct values """
		self.assertEqual(attempt.Y4.tolist(), ((0.2*attempt.X - 2) * sin(attempt.X)).tolist() )
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
