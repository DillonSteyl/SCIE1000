import matplotlib
matplotlib.use('Agg')
from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):


    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_output(self):
        """Prints correct values."""
        expected = "The final number of rats in each cage are:\nA - 1.0\nB - 1.0\nC - 0.0\nD - 98.0\nThe largest number of rats in a cage A is 42.0 at step 1\nThe largest number of rats in a cage B is 26.0 at step 3\nThe largest number of rats in a cage C is 30.0 at step 0\nThe largest number of rats in a cage D is 98.0 at step 50"
        out = f.getvalue()
        self.assertAlmostEqual(out.strip(), expected)

    def test_A_end(self):
        """The last value for the A array is correct"""		
        self.assertAlmostEqual(attempt.A[-1], 0.7681781208002938)
		
	def test_B_end(self):
        """The last value for the B array is correct"""		
        self.assertAlmostEqual(attempt.B[-1], 0.6612439216799161)
		
	def test_C_end(self):
        """The last value for the C array is correct"""		
        self.assertAlmostEqual(attempt.C[-1], 0.2605369800631443)
		
	def test_D_end(self):
        """The last value for the D array is correct"""		
        self.assertAlmostEqual(attempt.D[-1], 98.31004097745667)

    def test_B_start(self):
        """The first value for the B array is correct"""		
        self.assertAlmostEqual(attempt.B[0], 20)
		
	def test_C_start(self):
        """The first value for the C array is correct"""		
        self.assertAlmostEqual(attempt.C[0], 30)
		
	def test_D_start(self):
        """The first value for the D array is correct"""		
        self.assertAlmostEqual(attempt.D[0], 10)
		
	def test_A_start(self):
        """The first value for the A array is correct"""		
        self.assertAlmostEqual(attempt.A[0], 40)

    def test_lengths(self):
        """The arrays all have the correct lengths """
        self.assertEqual(size(attempt.A), 51)
		self.assertEqual(size(attempt.B), 51)
		self.assertEqual(size(attempt.C), 51)
		self.assertEqual(size(attempt.D), 51)
		
	def test_maxIndex(self):
        """The maxIndex variables are correct"""		
        self.assertEqual(attempt.maxIndexA, 1)
		self.assertEqual(attempt.maxIndexB, 3)
		self.assertEqual(attempt.maxIndexC, 0)
		self.assertEqual(attempt.maxIndexD, 50)

		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
