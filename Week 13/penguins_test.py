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
        expected = "The total number of deaths is 4943.620965569647\nThe maximum number of people infected at once is 12299582.792824812 which occurred at step 100"
        out = f.getvalue()
        self.assertAlmostEqual(out.strip(), expected)

    def test_susceptible_end(self):
        """Susceptible's last value is correct"""		
        self.assertAlmostEqual(attempt.S[-1], 144987.81334934343)

    def test_infected_end(self):
        """Infected's last value is correct """
        self.assertAlmostEqual(attempt.I[-1], 131963.73783686993)

    def test_recovered_end(self):
        """Recovered's last value is correct"""		
        self.assertAlmostEqual(attempt.R[-1], 24718104.827848207)

    def test_deceased_end(self):
        """Deceased's last value is correct"""
        self.assertAlmostEqual(attempt.D[-1], 4943.620965569647)

    def test_susceptible_start(self):
        """Susceptible's first value is correct"""		
        self.assertAlmostEqual(attempt.S[0], 24999999)

    def test_infected_start(self):
        """Infected's first value is correct """
        self.assertAlmostEqual(attempt.I[0], 1)

    def test_recovered_start(self):
        """Recovered's first value is correct"""		
        self.assertAlmostEqual(attempt.R[0], 0)

    def test_deceased_start(self):
        """Deceased's first value is correct"""
        self.assertAlmostEqual(attempt.D[0], 0)

    def test_lengths(self):
        """ time, S, I, R, and D all have the correct length """
        self.assertTrue(size(attempt.time)==201
                        and size(attempt.S)==201
                        and size(attempt.I)==201
                        and size(attempt.R)==201
                        and size(attempt.D)==201)
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
