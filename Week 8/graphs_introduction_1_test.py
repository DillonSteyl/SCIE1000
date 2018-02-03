from python_test_case import PythonTestCase, run_tests
from pylab import *
from io import StringIO

class Tests(PythonTestCase):

	def test_var(self):
		""" X contains values from 0 to 10 with a spacing of 0.5 """
		import attempt
		self.assertEqual(attempt.X, arange(0,10.1,0.5))
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
