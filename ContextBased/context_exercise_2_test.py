import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from unittest.mock import patch, call

import attempt

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_axis_title(self):
        """The graph has a title """
        g = gca()
        self.assertEqual(g.get_title(), "Oscillation of a spring")

    def test_axis_xlabel(self):
        """X axis is labelled """
        g = gca()
        self.assertEqual(g.get_xlabel(), "t")

    def test_axis_ylabel(self):
        """Y axis is labelled """
        g = gca()
        self.assertEqual(g.get_ylabel(), "x")
    
    def test_t_var(self):
        """ t array contains the correct values """
        self.assertEqual(attempt.t.tolist(), arange(0,10.01,0.01).tolist() )

    def test_x_var(self):
        """ x array contains the correct values """
        self.assertEqual(attempt.x.tolist(), (0.5*sin(4*pi*(attempt.t-0.125)).tolist() ))

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
