import matplotlib
matplotlib.use('Agg')
from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
from io import StringIO
from contextlib import redirect_stdout

class Tests(PythonTestCase):


    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass
        

    def test_x_SS(self):
        """The x coordinates of the first line (SS) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                a = arange(0,114.1,1)
                self.assertEquals(g.get_lines()[0].get_xdata().tolist(), a.tolist())

    def test_x_AW(self):
        """The x coordinates of the second line (AW) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                a = arange(0,114.1,1)
                self.assertEquals(g.get_lines()[1].get_xdata().tolist(), a.tolist())

    def test_y_SS(self):
        """The y coordinates of the first line (SS) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                a = arange(0,114.1,1)
                ss = 3*a**0.5
                self.assertEquals(g.get_lines()[0].get_ydata().tolist(), ss.tolist())

    def test_x_AW(self):
        """The y coordinates of the second line (AW) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                a = arange(0,114.1,1)
                ss = 3*a**0.5
                aw = ss*0.675
                self.assertEquals(g.get_lines()[1].get_ydata().tolist(), aw.tolist())

    def test_x_vSS(self):
        """The x coordinates of the first vertical line (SS at 15) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [25,25]                
                self.assertEquals(g.get_lines()[2].get_xdata().tolist(), v.tolist())

    def test_y_vSS(self):
        """The y coordinates of the first vertical line (SS at 15) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [0, 35]                
                self.assertEquals(g.get_lines()[2].get_ydata().tolist(), v.tolist())

    def test_x_vAW(self):
        """The x coordinates of the second vertical line (AW at 15) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [55,55]                
                self.assertEquals(g.get_lines()[3].get_xdata().tolist(), v.tolist())

    def test_y_vAW(self):
        """The y coordinates of the second vertical line (AW at 15) is correct."""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [0,35]                
                self.assertEquals(g.get_lines()[3].get_ydata().tolist(), v.tolist())

    def test_point1x64(self):
        """The x coordinates of the first point (SS at h=64) is correct."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [64]                
                self.assertEquals(g.get_lines()[4].get_xdata().tolist(), v.tolist())

    def test_point1x49(self):
        """The x coordinates of the first point (SS at h=49) is correct."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [49]                
                self.assertEquals(g.get_lines()[4].get_xdata().tolist(), v.tolist())

    def test_point1y64(self):
        """The y coordinates of the first point (SS at h=64) is correct."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*64**0.5]                
                self.assertEquals(g.get_lines()[4].get_ydata().tolist(), v.tolist())

    def test_point1y49(self):
        """The y coordinates of the first point (SS at h=49) is correct."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*49**0.5]                
                self.assertEquals(g.get_lines()[4].get_ydata().tolist(), v.tolist())

    def test_point1y16(self):
        """The y coordinates of the first point (SS at h=16) is correct."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*16**0.5]                
                self.assertEquals(g.get_lines()[4].get_ydata().tolist(), v.tolist())

    def test_point1x16(self):
        """The x coordinates of the first point (SS at h=16) is correct."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [16]                
                self.assertEquals(g.get_lines()[4].get_xdata().tolist(), v.tolist())

    def test_point2x64(self):
        """The x coordinates of the second point (AW at h=64) is correct."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [64]                
                self.assertEquals(g.get_lines()[5].get_xdata().tolist(), v.tolist())

    def test_point2x49(self):
        """The x coordinates of the second point (AW at h=49) is correct."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [49]                
                self.assertEquals(g.get_lines()[5].get_xdata().tolist(), v.tolist())

    def test_point2x16(self):
        """The x coordinates of the second point (AW at h=16) is correct."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [16]                
                self.assertEquals(g.get_lines()[5].get_xdata().tolist(), v.tolist())

    def test_point2y64(self):
        """The y coordinates of the second point (AW at h=64) is correct."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*64**0.5*0.675]                
                self.assertEquals(g.get_lines()[5].get_ydata().tolist(), v.tolist())

    def test_point2y49(self):
        """The y coordinates of the second point (AW at h=49) is correct."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*49**0.5*0.675]                
                self.assertEquals(g.get_lines()[5].get_ydata().tolist(), v.tolist())

    def test_point2y16(self):
        """The y coordinates of the second point (AW at h=16) is correct."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [3*16**0.5*0.675]                
                self.assertEquals(g.get_lines()[5].get_ydata().tolist(), v.tolist())


    # TEST COLOURS

    def test_point1colour64(self):
        """The colour of the first point (SS at h=64) is black."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()                
                self.assertEquals(g.get_lines()[4].get_color(), 'k')

    def test_point1colour49(self):
        """The colour of the first point (SS at h=49) is black."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                v = [49]                
                self.assertEquals(g.get_lines()[4].get_color(), 'k')


    def test_point1colour16(self):
        """The colour of the first point (SS at h=16) is red."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()                
                self.assertEquals(g.get_lines()[4].get_color(), 'r')

    def test_point2colour64(self):
        """The colour of the second point (AW at h=64) is black."""
        user_input = ["64"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[5].get_color(), 'k')

    def test_point2colour49(self):
        """The colour of the second point (AW at h=49) is red."""
        user_input = ["49"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[5].get_color(), 'r')

    def test_point2colour16(self):
        """The colour of the second point (AW at h=16) is red."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[5].get_color(), 'r')

    def test_point1_marker(self):
        """The marker for point 1 is a circle."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[4].get_marker(), 'o')

    def test_point2_marker(self):
        """The marker for point 2 is a square."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[5].get_marker(), 's')

    def test_ss_colour(self):
        """The colour for line 1 (SS) is green."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[0].get_color(), 'green')

    def test_aw_colour(self):
        """The colour for line 2 (AW) is orange."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[1].get_color(), 'orange')

    def test_v1_colour(self):
        """The colour for vertical line 1 (SS = 15) is red."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[2].get_color(), 'red')

    def test_v2_colour(self):
        """The colour for vertical line 2 (AW = 15) is red."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[3].get_color(), 'red')

    def test_v1_width(self):
        """The width of vertical line 1 (SS = 15) is 3."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[2].get_linewidth(), 3)

    def test_v2_width(self):
        """The width of vertical line 2 (AW = 15) is 3."""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[3].get_linewidth(), 3)


    def test_ss_label(self):
        """The label for line 1 (SS) is Spring/Summer"""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[0].get_label(), "Spring/Summer")

    def test_aw_label(self):
        """The label for line 2 (AW) is Autumn/Winter"""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[1].get_label(), "Autumn/Winter")


    def test_point1_label(self):
        """The label for point 1 (SS at h) is 'Number of Species in S/S'"""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[4].get_label(), 'Number of Species in S/S')


    def test_point2_label(self):
        """The label for point 2 (AW at h) is 'Number of Species in A/W'"""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_lines()[5].get_label(), 'Number of Species in A/W')


    def test_v2_linestyle(self):
        """The line style for the second vertical line is dashed"""
        user_input = ["16"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
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
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                lines = g.get_lines()
                self.assertEquals(len(lines), 6)

    def test_xlabel(self):
        """The x axis is labelled 'Area (hectares)'"""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_xlabel(), 'Area (hectares)')

    def test_ylabel(self):
        """The y axis is labelled 'Number of Species'"""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_ylabel(), 'Number of Species')

    def test_title(self):
        """The title is 'Species Area Curve in Different Seasons'"""
        user_input = ["60"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                g = gca()
                self.assertEquals(g.get_title(), 'Species Area Curve in Different Seasons')
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
