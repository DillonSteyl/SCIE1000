import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from unittest.mock import patch, call

import attempt

class Tests(PythonTestCase):
    
    def test_t_var(self):
	""" t array contains the correct values """
        self.assertEqual(attempt.t.tolist(), arange(0,10.01,0.01).tolist() )

    def test_x_var(self):
        """ x array contains the correct values """
	self.assertEqual(attempt.x.tolist(), (0.5*sin(4*pi*(attempt.t-0.125)).tolist() )

    def test_plot_called(self):
        """ plot function called - only works if matplotlib.pyplot.plot is called, not just 'plot' """

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
