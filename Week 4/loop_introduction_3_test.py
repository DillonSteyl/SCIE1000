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
		""" Program counts down from 3, before printing 'Happy New Year!' """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			self.assertEqual(output.getvalue().strip(), "3\n2\n1\nHappy New Year!")
			
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
