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

    def test_X_var(self):
        """ X array contains the correct values """
        self.assertEqual(attempt.X.tolist(), arange(0, 10.1, 0.1).tolist() )

    def test_Y1_var(self):
        """ Y1 array contains the correct values """
        self.assertEqual(attempt.Y1.tolist(), (-0.2*attempt.X + 2).tolist() )
		
    def test_Y2_var(self):
        """ Y2 array contains the correct values """
        self.assertEqual(attempt.Y2.tolist(), (0.2*attempt.X - 2).tolist() )

    def test_Y3_var(self):
        """ Y3 array contains the correct values """
        self.assertEqual(attempt.Y3.tolist(), ((-0.2*attempt.X + 2) * sin(attempt.X)).tolist() )
		
    def test_Y4_var(self):
        """ Y4 array contains the correct values """
        self.assertEqual(attempt.Y4.tolist(), ((0.2*attempt.X - 2) * sin(attempt.X)).tolist() )

    def test_file(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_axis_title(self):
        """The graph has a title """
        g = gca()
        self.assertEqual(g.get_title(), "Functions of X and Y")

    def test_axis_xlabel(self):
        """X axis is labelled """
        g = gca()
        self.assertEqual(g.get_xlabel(), "X value")

    def test_axis_ylabel(self):
        """Y axis is labelled """
        g = gca()
        self.assertEqual(g.get_ylabel(), "Y value")

    def test_two_lines(self):
        """Four lines are on the plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 4)

    def test_markers(self):
        """Y3 and Y4 use 'x' as a marker"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_marker(), 'x')
        self.assertEqual(lines[1].get_marker(), 'x')

    def test_markers(self):
        """All lines use the correct color"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_color(), 'k')
        self.assertEqual(lines[1].get_color(), 'k')
        self.assertEqual(lines[1].get_color(), 'c')
        self.assertEqual(lines[1].get_color(), 'c')

    def test_markers(self):
        """All lines use the correct linestyle"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_linestyle(), ':')
        self.assertEqual(lines[1].get_linestyle(), ':')
        self.assertEqual(lines[2].get_linestyle(), '-')
        self.assertEqual(lines[3].get_linestyle(), '-')

# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)
