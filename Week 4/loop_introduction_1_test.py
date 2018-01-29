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
		self.assertEqual(attempt.i, 5)
		
	def test_output(self):
		""" program correctly prints the squares of all numbers from 1 to 4 """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			self.assertEqual(output.getvalue().strip(), "1 squared: 1\n2 squared: 4\n3 squared: 9\n4 squared: 16")
			
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)