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
		""" Program counts down from 20, printing 'Only one digit now...' when 10 is reached """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "20"
			i = 19
			while i >= 0:
				expected += "\n" + str(i)
				if i == 10:
					expected += "\nOnly one digit now..."
				i = i - 1
			
			self.assertEqual(output.getvalue().strip(), expected)
			
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)