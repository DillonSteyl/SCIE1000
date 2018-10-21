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
        self.assertEqual(g.get_title(), "Disease X with Vaccinations")

    def test_axis_xlabel(self):
        """X axis is labelled correctly"""
        g = gca()
        self.assertEqual(g.get_xlabel(), "Time")

    def test_axis_ylabel(self):
        """Y axis is labelled correctly"""
        g = gca()
        self.assertEqual(g.get_ylabel(), "Population")

    def test_axis_legend(self):
        """Legend is used"""
        g = gca()
        self.assertIsNotNone(g.get_legend())
        
    def test_four_lines(self):
        """All four lines on plot"""
        g = gca()
        self.assertEquals(len(g.get_lines()), 4)

    def test_labels(self):
        """All lines are labelled correctly"""
        g = gca()
        lines = g.get_lines()
        for i in range(len(lines)):     
            self.assertIn(lines[i].get_label(),
                            ["Susceptible", "Infected", "Recovered", "Deceased"])
        

    def test_output(self):
        """Prints correct values."""
        expected = "The total number of deaths is 1813.0136186384832\nThe maximum number of people infected at once is 3457442.7227383545"
        out = f.getvalue()
        self.assertEqual(out.strip(), expected)

    def test_susceptible_end(self):
        """Susceptible's last value is correct"""		
        self.assertAlmostEqual(attempt.S[-1], 0)

    def test_infected_end(self):
        """Infected's last value is correct """
        self.assertAlmostEqual(attempt.I[-1], 163289.28738586543)

    def test_recovered_end(self):
        """Recovered's last value is correct"""		
        self.assertAlmostEqual(attempt.R[-1], 24834897.698995512)

    def test_deceased_end(self):
        """Deceased's last value is correct"""
        self.assertAlmostEqual(attempt.D[-1], 1813.0136186384832)

    def test_susceptible_start(self):
        """Susceptible's first value is correct"""		
        self.assertAlmostEqual(attempt.S[0], 24999999)

    def test_infected_start(self):
        """Infected's first value is correct """
        self.assertAlmostEqual(attempt.I[0], 1)

    def test_recovered_start(self):
        """Recovered's first value is correct"""		
        self.assertAlmostEqual(attempt.R[0], 0)

    def test_deceased_start(self):
        """Deceased's first value is correct"""
        self.assertAlmostEqual(attempt.D[0], 0)

    def test_lengths(self):
        """ time, S, I, R, and D all have the correct length """
        self.assertTrue(size(attempt.time)==201
                        and size(attempt.S)==201
                        and size(attempt.I)==201
                        and size(attempt.R)==201
                        and size(attempt.D)==201)
		
# Run the unit tests
if __name__ == "__main__":
    import attempt
    run_tests(Tests)


