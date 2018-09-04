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
        """There is something on the graph"""
        g = gca()
        lines = g.get_lines()
        self.assertEquals(len(lines), 1)
        
    def test_point(self):
        """It is a single point on the graph"""
        g = gca()
        self.assertEquals(len(g.get_lines()[0].get_xdata()), 1)

    def test_x(self):
        """The point has the correct x value: 4"""
        g = gca()
        lines = g.get_lines()    
        self.assertEquals(lines[0].get_xdata()[0], 4)
	
    def test_file(self):
        """TESTING FILE THINGO YO"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_y(self):
        """The point has the correct y value: 2.5"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_ydata()[0], 2.5)
	
    def test_ymarker(self):
        """The point uses an asterisk (*) as the marker"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_marker(), '*')
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
