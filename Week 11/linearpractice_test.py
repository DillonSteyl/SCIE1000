import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from io import StringIO
from unittest.mock import patch, call

INPUT = ["4", "5"]

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    @patch('builtins.input', side_effect = INPUT)
    def test_title(self, input_call):
        """ The graph has the correct title """
        import attempt
        g = gca()
        self.assertEqual(g.get_title(), "Linear Model")
        savefig("output.png")
        clf()

    @patch('builtins.input', side_effect = INPUT)
    def test_x_label(self, input_call):
        """ The x axis is labelled correctly """
        import attempt
        g = gca()
        self.assertEqual(g.get_xlabel(), "x")
        savefig("output.png")
        clf()

    @patch('builtins.input', side_effect = INPUT)
    def test_y_label(self, input_call):
        """ The y axis is labelled correctly """
        import attempt
        g = gca()
        self.assertEqual(g.get_ylabel(), "y")
        savefig("output.png")
        clf()

    @patch('builtins.input', side_effect = INPUT)
    def test_x_data(self, input_call):
        """ The plot uses the correct x values """
        import attempt
        g = gca()
        self.assertEqual(gca().get_lines()[0].get_xdata().tolist(), attempt.x.tolist())
        savefig("output.png")
        clf()

    @patch('builtins.input', side_effect = INPUT)
    def test_y_data(self, input_call):
        """ The plot uses the correct y values """
        import attempt
        g = gca()
        self.assertEqual(gca().get_lines()[0].get_ydata().tolist(), attempt.y.tolist())
        savefig("output.png")
        clf()

    @patch('builtins.input', side_effect = INPUT)
    def test_file(self, input_call):
        """Show is used to display plot"""
        import attempt
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
        savefig("output.png")
        clf()
    
    @patch('builtins.input', side_effect = INPUT)
    def test_one_line(self, input_call):
        """ One line on plot"""
        import attempt
        g = gca()
        self.assertEquals(len(g.get_lines()), 1)
        savefig("output.png")
        clf()
    
    

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
