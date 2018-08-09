from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
from pylab import *

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass

	def test_i(self):
		""" i is defined, and has the correct value when the program terminates """
		import attempt
		self.assertDefined(attempt, "i", int)
		self.assertEqual(attempt.i, 13)
		
	def test_output(self):
		""" program correctly prints all the average temperatures for Cairns """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			self.assertEqual(output.getvalue().strip(), "Average temperature for month 1 is 28.0\nAverage temperature for month 2 is\n27.598076211353316\nAverage temperature for month 3 is 26.5\nAverage temperature for month 4 is 25.0\nAverage temperature for month 5 is 23.5\nAverage temperature for month 6 is 22.401923788646684\nAverage temperature for month 7 is 22.0\nAverage temperature for month 8 is 22.401923788646684\nAverage temperature for month 9 is 23.5\nAverage temperature for month 10 is 25.0\nAverage temperature for month 11 is 26.5\nAverage temperature for month 12 is 27.598076211353316")
			
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
