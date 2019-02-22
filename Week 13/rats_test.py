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
        expected = "The quarter with the highest number of fish is 4 with 628.0 penguins on the island at the time."
        out = f.getvalue()
        self.assertAlmostEqual(out.strip(), expected)

    def test_fish_end(self):
        """The last value for the fish array is correct"""		
        self.assertAlmostEqual(attempt.F[-1], 0)

    def test_penguin_end(self):
        """the last value for the penguin array is correct """
        self.assertAlmostEqual(attempt.P[-1], 390.75510334276015)

    def test_fish_start(self):
        """The first value for the fish array is correct"""		
        self.assertAlmostEqual(attempt.F[0], 50)

    def test_penguin_end(self):
        """The first value for the penguin array is correct"""
        self.assertAlmostEqual(attempt.P[0], 600)

    def test_lengths(self):
        """ The arrays all have the correct lengths """
        self.assertEqual(size(attempt.P), 16)
	self.assertEqual(size(attempt.F), 16)

		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
