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

	def test_output(self):
		""" Program counts upwards from -3 to 3, correctly labelling whether each number is positive or negative """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "Negative: -3\nNegative: -2\nNegative: -1\nZero: 0\nPositive: 1\nPositive: 2\nPositive: 3"
			self.assertEqual(output.getvalue().strip(), expected)
			
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)