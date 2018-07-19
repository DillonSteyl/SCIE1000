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
    def test_base_scenario(self):
        """Tests base scenario"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.5, 0.5, 0.0001, 1000000, 0.1),
                         1813.0136186384832)
        
    def test_different_weeks(self):
        """Tests base scenario but with weeks=10"""
        self.assertAlmostEqual(attempt.runSimulation(10, 25000000,
                                               2.5, 0.5, 0.0001, 1000000, 0.1),
                         101.92694936449374)

    def test_different_pop(self):
        """Tests base scenario but with pop=20mil"""
        self.assertAlmostEqual(attempt.runSimulation(20, 20000000,
                                               2.5, 0.5, 0.0001, 1000000, 0.1),
                         680.9757185541044)

    def test_different_a(self):
        """Tests base scenario but with a = 2.0"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.0, 0.5, 0.0001, 1000000, 0.1),
                         299.01462222477153)

    def test_different_b(self):
        """Tests base scenario but with b = 0.25"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.5, 0.25, 0.0001, 1000000, 0.1),
                         4565.697940179704)

    def test_different_d(self):
        """Tests base scenario but with d = 0.001"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.5, 0.5, 0.001, 1000000, 0.1),
                         18068.975929710017)

    def test_different_v(self):
        """Tests base scenario but with v = 500000"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.5, 0.5, 0.0001, 500000, 0.1),
                         3564.819319142185)

    def test_different_step(self):
        """Tests base scenario but with stepSize = 0.2"""
        self.assertAlmostEqual(attempt.runSimulation(20, 25000000,
                                               2.5, 0.5, 0.0001, 1000000, 0.2),
                         1597.0609896692674)

    def test_output(self):
        """Prints nothing."""
        expected = ""
        out = f.getvalue()
        self.assertEqual(out.strip(), expected)

		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)

