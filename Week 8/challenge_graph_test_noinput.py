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
        
    def test_SS_colour(self):
        """The first line (SS) has colour green."""
        g = gca()               
        self.assertEquals(g.get_lines()[0].get_color(), 'green')
        
    def test_AW_colour(self):
        """The second line (AW) has colour orange."""
        g = gca()               
        self.assertEquals(g.get_lines()[1].get_color(), 'orange')
        
    def test_v1_colour(self):
        """The first vertical line (SS = 15) has colour red."""
        g = gca()               
        self.assertEquals(g.get_lines()[2].get_color(), 'r')
        
    def test_v2_colour(self):
        """The second vertical line (AW = 15) has colour red."""
        g = gca()               
        self.assertEquals(g.get_lines()[2].get_color(), 'r')
        
    def test_point1_colour(self):
        """The first point (SS at h) is black if SS>=15, red otherwise"""
        g = gca()
        h = attempt.h
        if 3*h**0.5<15:
            self.assertEquals(g.get_lines()[4].get_color(), 'r')
        else:
            self.assertEquals(g.get_lines()[4].get_color(), 'k')
            
            
    def test_point2_colour(self):
        """The second point (AW at h) is black if AW>=15, red otherwise"""
        g = gca()
        h = attempt.h
        if 3*h**0.5*0.675<15:
            self.assertEquals(g.get_lines()[5].get_color(), 'r')
        else:
            self.assertEquals(g.get_lines()[5].get_color(), 'k')
            
            
    def test_v1_width(self):
        """The first vertical line (SS = 15) has width 3."""
        g = gca()               
        self.assertEquals(g.get_lines()[2].get_linewidth(), 3)
        
    def test_v2_width(self):
        """The second vertical line (AW = 15) has width 3."""
        g = gca()               
        self.assertEquals(g.get_lines()[3].get_linewidth(), 3)
        
        
    def test_ss_label(self):
        """The first line (SS) has label 'Spring/Summer'."""
        g = gca()               
        self.assertEquals(g.get_lines()[0].get_label(), 'Spring/Summer')
        
        
    def test_aw_label(self):
        """The second line (AW) has label 'Autumn/Winter'."""
        g = gca()               
        self.assertEquals(g.get_lines()[1].get_label(), 'Autumn/Winter')
        
    def test_point1_label(self):
        """The label for point 1 (SS at h) is 'Number of Species in S/S'"""
        g = gca()
        self.assertEquals(g.get_lines()[4].get_label(), 'Number of Species in S/S')


    def test_point2_label(self):
        """The label for point 2 (AW at h) is 'Number of Species in A/W'"""
        g = gca()
        self.assertEquals(g.get_lines()[5].get_label(), 'Number of Species in A/W')
        
        
    def test_v2_linestyle(self):
        """The line style for the second vertical line is dashed"""
        g = gca()
        self.assertEquals(g.get_lines()[3].get_linestyle(), '--')
        
    def test_show(self):
        """Show is used to display plot"""
        a = False
        if "show()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True)

    def test_grid(self):
        """Show is used to display plot"""
        a = False
        if "grid(True)" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True)

    def test_legend(self):
        """Show is used to display plot"""
        a = False
        if "legend()" in open('attempt.py').read():
            a = True
        self.assertEquals(a,True) 
        
    def test_num_lines(self):
        """There are 6 lines."""
        g = gca()
        lines = g.get_lines()
        self.assertEquals(len(lines), 6)

    def test_xlabel(self):
        """The x axis is labelled 'Area (hectares)'"""
        g = gca()
        self.assertEquals(g.get_xlabel(), 'Area (hectares)')

    def test_ylabel(self):
        """The y axis is labelled 'Number of Species'"""
        g = gca()
        self.assertEquals(g.get_ylabel(), 'Number of Species')

    def test_title(self):
        """The title is 'Species Area Curve in Different Seasons'"""
        g = gca()
        self.assertEquals(g.get_title(), 'Species Area Curve in Different Seasons')
        
     
        
    
        
    
        
        
    

if __name__ == "__main__":
    import attempt
    run_tests(Tests)

