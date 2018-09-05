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

    def test_lines(self):
        """There are two lines on the graph."""
        g = gca()
        lines = g.get_lines()
        self.assertEquals(len(lines), 2)
        

    def test_X1(self):
        """The first line has the correct X values"""
		
        g = gca()
        lines = g.get_lines()    
        X = arange(-2*pi, 2*pi, 0.05)
        self.assertTrue((lines[0].get_xdata() == X).all())
		
    def test_Y1(self):
        """The first line has the correct Y values"""
		
        g = gca()
        lines = g.get_lines()    
        X = arange(-2*pi, 2*pi, 0.05)
        Y1 = X**2
        self.assertTrue((lines[0].get_ydata()== Y1).all())
		
    def test_Y2(self):
        """The second line has the correct Y values"""
		
        g = gca()
        lines = g.get_lines()    
        X = arange(-2*pi, 2*pi, 0.05)
        Y2 = X**2 + 3*sin(12*X)
        self.assertTrue((lines[1].get_ydata() == Y2).all())
		
    def test_X2(self):
        """The second line has the correct X values"""
        g = gca()
        lines = g.get_lines()    
        X = arange(-2*pi, 2*pi, 0.05)
        self.assertEquals(lines[1].get_xdata().tolist(), X.tolist())
	
    def test_file_show(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
		
    def test_file_grid(self):
        """There are grid lines."""
        a = False
        if "grid(True)" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
		
    def test_file_legend(self):
        """There is a legend"""
        a = False
        if "legend()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_xlabel(self):
        """The x axis is labelled as 'x'"""
        g = gca() 
        self.assertEqual(g.get_xlabel(), "x")
		
    def test_ylabel(self):
        """The y axis is labelled as 'y'"""
        g = gca()
        self.assertEqual(g.get_ylabel(), "y")
		
    def test_Y1_label(self):
        """The first line is labelled as 'y = x^2'"""
        g = gca()
        self.assertEqual(g.get_legend().get_texts()[0].get_text(), "y = x^2")
		
    def test_Y2_label(self):
        """The first line is labelled as 'y = x^2 + 3*sin(12x)'"""
        g = gca()
        self.assertEqual(g.get_legend().get_texts()[1].get_text(), "y = x^2 + 3*sin(12x)")
		
    def test_second_colour(self):
        """The second line is red"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[1].get_color(), (1.0, 0.0, 0.0, 1))
		
    def test_first_colour(self):
        """The first line is green"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_color(), (0.0, 0.5, 0.0, 1))
		
    def test_title(self):
        """The title is 'x^2 and x^2+3*sin(12x)'"""
        g = gca()
        self.assertEqual(g.get_title(), "x^2 and x^2+3*sin(12x)")
		
	
	
	
	
	
	
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
