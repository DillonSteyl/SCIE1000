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

    def test_one_line(self):
        """One line on the plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 1)

    def test_x_var(self):
        """ X array contains the correct values """
        self.assertEqual(attempt.x.tolist(), array([0,1,2,3,4,5]).tolist() )

    def test_y_var(self):
        """ Y array contains the correct values """
        self.assertEqual(attempt.y.tolist(), (2**attempt.x).tolist() )

    def test_plot(self):
        """Correct line is plotted"""
        with patch('pylab.plot') as mock_plot:
            import attempt
            callargs = mock_plot.call_args
            self.assertEqual(callargs[0][0].tolist(), attempt.x.tolist())
            self.assertEqual(callargs[0][1].tolist(), attempt.y.tolist())

# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)
