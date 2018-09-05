import matplotlib
matplotlib.use('Agg')
from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
import io
from contextlib import redirect_stdout

class Tests(PythonTestCase):


    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass
        

    def test_x_SS(self):
        """The x coordinates of the first line (SS) is correct."""
        g = gca()
        a = arange(0,114.1,1)
        self.assertEquals(g.get_lines()[0].get_xdata().tolist(), a.tolist())

    def test_x_AW(self):
        """The y coordinates of the second line (AW) is correct."""
        g = gca()
        a = arange(0,114.1,1)
        self.assertEquals(g.get_lines()[1].get_xdata().tolist(), a.tolist())

    def test_y_SS(self):
        """The y coordinates of the first line (SS) is correct."""
        g = gca()
        a = arange(0,114.1,1)
        ss = 3*a**0.5
        self.assertEquals(g.get_lines()[0].get_ydata().tolist(), ss.tolist())

    def test_x_AW(self):
        """The y coordinates of the second line (AW) is correct."""
        g = gca()
        a = arange(0,114.1,1)
        ss = 3*a**0.5
        aw = ss*0.675
        self.assertEquals(g.get_lines()[1].get_ydata().tolist(), aw.tolist())

    def test_x_vSS(self):
        """The x coordinates of the first vertical line (SS at 15) is correct."""
        g = gca()
        v = [25,25]                
        self.assertEquals(g.get_lines()[2].get_xdata().tolist(), v)

    def test_y_vSS(self):
        """The y coordinates of the first vertical line (SS at 15) is correct."""
        g = gca()
        v = [0, 35]                
        self.assertEquals(g.get_lines()[2].get_ydata().tolist(), v)

    def test_x_vAW(self):
        """The x coordinates of the second vertical line (AW at 15) is correct."""
        g = gca()
        v = [55,55]                
        self.assertEquals(g.get_lines()[3].get_xdata().tolist(), v)

    def test_y_vAW(self):
        """The y coordinates of the second vertical line (AW at 15) is correct."""
        g = gca()
        v = [0,35]                
        self.assertEquals(g.get_lines()[3].get_ydata().tolist(), v)

    def test_point1x(self):
        """ The x coordinate of the first point is correct."""
        g = gca()
        v = [attempt.h]                
        self.assertEquals(g.get_lines()[4].get_xdata().tolist(), v)

    def test_point2x(self):
        """The x coordinate of the second point is correct."""
        g = gca()
        v = [attempt.h]                
        self.assertEquals(g.get_lines()[5].get_xdata().tolist(), v)

    def test_point1y(self):
        " The y coordinate of the first point is correct."""
        g = gca()
        v = [3*attempt.h**0.5]                
        self.assertEquals(g.get_lines()[4].get_ydata().tolist(), v)

    def test_point2y(self):
        """The y coordinate of the second point is correct."""
        g = gca()
        v = [3*attempt.h**0.5*0.675]                
        self.assertEquals(g.get_lines()[5].get_ydata().tolist(), v)

if __name__ == "__main__":
    import attempt
    run_tests(Tests)

