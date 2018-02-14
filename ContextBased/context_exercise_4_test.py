import matplotlib
matplotlib.use('Agg')
from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
import io
from contextlib import redirect_stdout

import attempt

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_Pop_a(self):
        """ First value in Phase A is correct """
        self.assertEqual(attempt.Pop[0], 15000)

    def test_Pop_a2(self):
        """ Last value in Phase A is correct """
        self.assertEqual(attempt.Pop[15], 15000)

    def test_Pop_b(self):
        """ First value in Phase B is correct """
        self.assertEqual(attempt.Pop[16], 30000)

    def test_Pop_b2(self):
        """ Last value in Phase B is correct """
        self.assertEqual(attempt.Pop[55], 1.649267441664e+16)

    def test_Pop_c(self):
        """ First value in Phase C is correct """
        self.assertEqual(attempt.Pop[56], 1.649267441664e+16)

    def test_Pop_c2(self):
        """ Last value in Phase C is correct """
        self.assertEqual(attempt.Pop[79], 1.649267441664e+16)

    def test_Pop_d(self):
        """ First value in Phase D is correct """
        self.assertEqual(attempt.Pop[80], 1.236950581248e+16)

    def test_Pop_d2(self):
        """ Last value in Phase D is correct """
        self.assertEqual(attempt.Pop[96], 1.2397455648e+14)

    def test_LPop_var(self):
        """ LPop array contains the correct values """
        self.assertEqual(attempt.LPop.tolist(), log10(attempt.Pop).tolist() )

    def test_lengths(self):
        """ Pop and LPop have the correct length """
        self.assertTrue(size(attempt.Pop)==97
                        and size(attempt.LPop)==97)

    def test_axis_title(self):
        """The graph has a title """
        g = gca()
        self.assertEqual(g.get_title(), "Bacteria Growth Curve")

    def test_axis_xlabel(self):
        """X axis is labelled """
        g = gca()
        self.assertEqual(g.get_xlabel(), "Time (hours)")

    def test_axis_ylabel(self):
        """Y axis is labelled """
        g = gca()
        self.assertEqual(g.get_ylabel(), "Population (log CFU/mL)")

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
