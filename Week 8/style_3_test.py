import matplotlib
matplotlib.use('Agg')
from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
import io
from contextlib import redirect_stdout

import attempt

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_a_var(self):
        """ Area array for plotting contains the correct values """
        self.assertEqual(attempt.a.tolist(), arange(0,1141,1).tolist() )

    def test_SS_var(self):
        """ SS model is correct """
        self.assertEqual(attempt.SS.tolist(), (attempt.M*(attempt.a)**attempt.p).tolist() )

    def test_AW_var(self):
        """ AW model is correct """
        self.assertEqual(attempt.AW.tolist(), (0.675*attempt.SS).tolist() )

    def test_axis_title(self):
        """The graph has a title """
        g = gca()
        self.assertEqual(g.get_title(), "Species Area Curve")

    def test_axis_xlabel(self):
        """X axis is labelled """
        g = gca()
        self.assertEqual(g.get_xlabel(), "Area (1000m square cells)")

    def test_axis_ylabel(self):
        """Y axis is labelled """
        g = gca()
        self.assertEqual(g.get_ylabel(), "Number of Species")

    def test_axis_legend(self):
        """Legend is used"""
        g = gca()
        self.assertIsNotNone(g.get_legend())

    def test_file(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_file2(self):
        """Grid is used"""
        a = False
        if "grid(True)" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_two_lines(self):
        """Both lines are on the plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 2)

    def test_labels(self):
        """All lines are labelled correctly"""
        g = gca()
        lines = g.get_lines()
        for i in range(len(lines)):     
            self.assertIn(lines[i].get_label(),
                            ["Spring/Summer", "Autumn/Winter"])

if __name__ == "__main__":
    import attempt
    run_tests(Tests)
