
from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO

class Tests(PythonTestCase):
	
	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass

	def test_primes(self):
		""" 'final' array is correct """
		import attempt
		self.assertEqual(attempt.final.tolist(), [87.5,  65.05, 57.4,  75.65])
		
	def test_out(self):
		""" Output is correct """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "The final marks out of 100 are: [87.5 65.05 57.4 74.8]"
			self.assertEqual(output.getvalue().strip(), expected)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
