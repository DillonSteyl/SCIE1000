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

    def test_lines(self):
        """There are two lines and one point on the graph"""
        g = gca()
        lines = g.get_lines()
        self.assertEquals(len(lines), 3)
		
    def test_x_var(self):
        """ x has not been modified """
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEquals(attempt.x.tolist(), expected)

    def test_y1_var(self):
        """ y1 is correct """
        self.assertEqual(attempt.y1.tolist(), (attempt.x+4).tolist() )

    def test_y2_var(self):
        """ y2 is correct """
        self.assertEqual(attempt.y2.tolist(), (-0.5*attempt.x+10).tolist() )

    def test_xmark(self):
        """The point has the correct x value: 4"""
        g = gca()
        lines = g.get_lines()    
        self.assertEquals(lines[2].get_xdata()[0], 4)

    def test_ymark(self):
        """The point has the correct y value: 8"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[2].get_ydata()[0], 8)
	
    def test_marker(self):
        """The point uses an asterisk (*) as the marker"""
        g = gca()
        lines = g.get_lines() 
        self.assertEqual(lines[2].get_marker(), '*')



    '''
    def test_show_called_1(self):
        """ matplotlib.pyplot.show() method is called """
        with patch('matplotlib.pyplot.show') as mocked_show:
            import attempt
            mocked_show.assert_called()
    '''
                
    # This test causes no output to show up!!!
    def test_show_called_2(self):
        """ show() method is called """
        with patch('pylab.show') as mocked_show:
            import attempt
            mocked_show.assert_called()

# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)
