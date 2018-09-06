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
        
    def test_file(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
        
    def test_five_lines(self):
        """Five lines are on the plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 5)

    def test_markers(self):
        """Lines use the correct markers"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[1].get_marker(), 's')
        self.assertEqual(lines[2].get_marker(), '8')
        self.assertEqual(lines[4].get_marker(), '.')

    def test_widths(self):
        """Lines use the correct linewidth"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_linewidth(), 1.5)
        self.assertEqual(lines[1].get_linewidth(), 0.5)
        self.assertEqual(lines[3].get_linewidth(), 5)
        self.assertEqual(lines[4].get_linewidth(), 2)

    def test_colors(self):
        """Lines use the correct color"""
        g = gca()
        lines = g.get_lines() 
        self.assertIn(lines[1].get_color(), [(1.0, 0.0, 0.0, 1), 'r', 'red'])
        self.assertIn(lines[0].get_color(), [(0.0, 0.5, 0.0, 1), 'g', 'green'])
        self.assertIn(lines[1].get_color(), [(0.5, 0.0, 0.5, 1), 'purple'])
        self.assertIn(lines[2].get_color(), [(0.0, 0.0, 0.0, 1), 'k', 'black'])
        self.assertIn(lines[4].get_color(), ['xkcd:blood orange'])

    def test_styles(self):
        """Lines use the correct linestyle"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_linestyle(), '--')
        self.assertEqual(lines[1].get_linestyle(), '-')
        self.assertEqual(lines[2].get_linestyle(), 'None')
        self.assertEqual(lines[3].get_linestyle(), '-')
        self.assertEqual(lines[4].get_linestyle(), '-.')

# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)
