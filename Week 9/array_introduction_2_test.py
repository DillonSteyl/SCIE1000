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
		""" 'primes' array has not been modified """
		import attempt
		self.assertEqual(attempt.primes.tolist(), [2,3,5,7,11])
		
	def test_out(self):
		""" Output is correct """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "First prime: 2\nFourth prime: 7"
			self.assertEqual(output.getvalue().strip(), expected)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)