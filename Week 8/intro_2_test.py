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

    def test_one_line(self):
        """One line on the plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 1)

    def test_x_var(self):
        """ x array contains the correct values """
        self.assertEqual(attempt.x.tolist(), array([0,1,2,3,4,5]).tolist() )

    def test_y_var(self):
        """ Y array contains the correct values """
        self.assertEqual(attempt.y.tolist(), (2**attempt.x).tolist() )

# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)
