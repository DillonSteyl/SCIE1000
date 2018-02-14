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
    def test_seconds(self):
        """Tests correct seconds_in_a_year"""
        self.assertEqual(attempt.seconds_in_a_year, 60*60*24*365)
        
    def test_rabbits(self):
        """Tests correct rabbits"""
        self.assertEqual(attempt.rabbits, 2**6)

    def test_accuracy(self):
        """Tests correct accuracy"""
        self.assertEqual(attempt.accuracy, (45+38)/(45+5+12+38))

    def test_money(self):
        """Tests correct money"""
        self.assertEqual(attempt.money, 100*(1+0.05)**12)

    def test_interest(self):
        """Tests correct interest"""
        self.assertEqual(attempt.interest, attempt.money - 100)

    def test_output(self):
        """Prints nothing."""
        expected = ""
        out = f.getvalue()
        self.assertEqual(out.strip(), expected)

		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
