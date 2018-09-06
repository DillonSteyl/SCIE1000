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
        """The graph has the correct title """
        g = gca()
        self.assertEqual(g.get_title(), "Oscillation of a spring")

    def test_axis_xlabel(self):
        """X axis is labelled correctly """
        g = gca()
        self.assertEqual(g.get_xlabel(), "Time (s)")
    
    def test_t1_var(self):
        """ The first line contains the corrext y values """
        self.assertEqual(gca().get_lines()[0].get_ydata().tolist(), arange(0,10.51,0.01).tolist() )

    def test_t2_var(self):
        """ The second line contains the correct y values """
        self.assertEqual(gca().get_lines()[1].get_ydata().tolist(), arange(0,10.65,.15).tolist() )

    def test_t3_var(self):
        """ The third line contains the correct y values """
        self.assertEqual(gca().get_lines()[2].get_ydata().tolist(), arange(0,11,0.5).tolist() )

    def test_x1_var(self):
        """ The first line contains the correct x values """
        self.assertEqual(gca().get_lines()[0].get_xdata().tolist(), ((0.5*sin(4*pi*(attempt.t1-0.125))).tolist() ))

    def test_x2_var(self):
        """ The second line contains the correct x values """
        self.assertEqual(gca().get_lines()[0].get_xdata().tolist(), ((0.5*sin(4*pi*(attempt.t2-0.125))+2).tolist() ))

    def test_x3_var(self):
        """ The third line contains the correct x values """
        self.assertEqual(gca().get_lines()[0].get_xdata().tolist(), ((0.5*sin(4*pi*(attempt.t3-0.125))+4).tolist() ))

    '''
    def test_file(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
    '''

    def test_show_called(self):
        """Show() method is called"""
        with patch('pylab.show') as mock_show:
            import attempt
            mock_show.assert_called()

    def test_three_lines(self):
        """All three lines on plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 3)

    def test_axis_legend(self):
        """Legend is used"""
        g = gca()
        self.assertIsNotNone(g.get_legend())

    def test_labels(self):
        """All lines are labelled correctly"""
        g = gca()
        lines = g.get_lines()
        for i in range(len(lines)):     
            self.assertIn(lines[i].get_label(),
                            ["0.01s Samples", "0.15s Samples", "0.5s Samples"])

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
