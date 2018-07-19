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
        """Prints correct message: These two equations are not interchangeable."""
        expected = "These two equations are not interchangeable."
        out = f.getvalue()
        self.assertEqual(out.strip(), expected)

    def test_exponential_end(self):
        """Exponential's last value is correct"""		
        self.assertEqual(attempt.exponential[-1], 100*exp(attempt.k*(attempt.n-1)))

    def test_compounding_end(self):
        """ Compounding's last value is correct """
        self.assertEqual(attempt.compounding[-1], 100*(attempt.k+1)**(attempt.n-1))

    def test_exponential_start(self):
        """ Exponential's last value is correct"""
        self.assertEqual(attempt.exponential[0], 100)
		
    def test_compounding_Start(self):
        """ Compounding's last value is correct """
        self.assertEqual(attempt.compounding[0], 100)

    def test_k(self):
        """ k is a reasonable value """
        self.assertTrue(attempt.k>=0.01 and attempt.k<=0.2)

    def test_n(self):
        """ n is a reasonable value """
        self.assertTrue(attempt.n>=30 and attempt.n<=50)

    def test_lengths(self):
        """ time, exponential, and compounding all have the correct length """
        self.assertTrue(size(attempt.time)==attempt.n and size(attempt.exponential)==attempt.n and size(attempt.compounding)==attempt.n)
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
