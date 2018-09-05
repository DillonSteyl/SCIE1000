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
        

    def test_x(self):
        """The x coordinates of the square are correct."""
        g = gca()
        lines = g.get_lines()    
        self.assertEquals(lines[0].get_xdata()[0].tolist(), [3, 5, 5, 3, 3])
	
    def test_file(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 

    def test_y(self):
        """The y coordinates of the square are correct."""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[0].get_ydata()[0], [3, 3, 1, 1, 3])
	
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
