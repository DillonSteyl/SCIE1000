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
		""" 'squares' array has been modified correctly """
		import attempt
		self.assertEqual(attempt.squares.tolist(), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
		
	def test_out(self):
		""" Output is correct, prints squares before and after updating """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = ("[  0   4   9  15  25  36  49  64  81 121]\n"
			"[  1   4   9  16  25  36  49  64  81 100]")
			self.assertEqual(output.getvalue().strip(), expected)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
