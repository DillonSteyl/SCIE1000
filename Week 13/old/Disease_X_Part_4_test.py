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
    def test_axis_title(self):
        """The Title of the graph is correct"""
        g = gca()
        self.assertEqual(g.get_title(), "Effect of Vaccinations p/w on Deaths")

    def test_axis_xlabel(self):
        """X axis is labelled correctly"""
        g = gca()
        self.assertEqual(g.get_xlabel(), "Vaccinations per week")

    def test_axis_ylabel(self):
        """Y axis is labelled correctly"""
        g = gca()
        self.assertEqual(g.get_ylabel(), "Deaths")
        
    def test_one_line(self):
        """Only one line on plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 1)
        

    def test_output(self):
        """Prints nothing."""
        expected = ""
        out = f.getvalue()
        self.assertEqual(out.strip(), expected)

    def test_death_array(self):
        """Correct values in Deceased array."""
        expected = [1813.01361864, 1605.21968792,
                                     1393.80818152,
                                     1181.86932546,  974.31377284, 777.77213167,
                                     599.92732733,  447.5890334,   324.6456883,
                                     230.82503121, 162.41766473,  114.0866949,
                                     80.5307905,    57.3790955,    41.37585224,
                                     30.23462915,   22.39970194,   16.82266552,
                                     12.80246927,    9.86713619, 7.69720163]
        self.assertEqual(size(attempt.D), len(expected))
        for i in range(len(expected)):         
            self.assertAlmostEqual(attempt.D[i], expected[i])
		
# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)



