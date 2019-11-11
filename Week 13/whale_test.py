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
        expected = "The whale population reaches its peak of 26.0 whales during step 134\nThe zooplankton population reaches its peak of 45.0 thousand tonnes during step 113\nThe number of steps between these peaks is 21"
        out = f.getvalue()
        self.assertAlmostEqual(out.strip(), expected)

    def test_W_end(self):
        """The last value for the W array is correct"""		
        self.assertAlmostEqual(attempt.W[-1], 9.494852380803035)
		
    def test_Z_end(self):
        """The last value for the Z array is correct"""		
        self.assertAlmostEqual(attempt.Z[-1], 41.47999849170943)

    def test_W_start(self):
        """The first value for the W array is correct"""		
        self.assertAlmostEqual(attempt.W[0], 12)
		
    def test_Z_start(self):
        """The first value for the Z array is correct"""		
        self.assertAlmostEqual(attempt.Z[0], 40)

    def test_lengths(self):
        """The arrays all have the correct lengths """
        self.assertEqual(size(attempt.Z), 201)
        self.assertEqual(size(attempt.W), 201)
		
    def test_maxIndex(self):
        """The maxIndex variables are correct"""		
        self.assertEqual(attempt.maxIndexZ, 113)
        self.assertEqual(attempt.maxIndexW, 134)

		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
