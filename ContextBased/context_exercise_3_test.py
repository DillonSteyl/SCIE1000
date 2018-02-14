from python_test_case import PythonTestCase, run_tests
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from os import devnull
import io

f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):

    def test_S_var(self):
        """ S variable is correct """
        self.assertEqual(attempt.S.tolist(), (-0.1*(attempt.Q)+451).tolist() )

    def test_D_var(self):
        """ D variable is correct """
        self.assertEqual(attempt.D.tolist(), (0.2*(attempt.Q)-779).tolist() )

    def test_ND_var(self):
        """ ND variable is correct """
        self.assertEqual(attempt.ND.tolist(), (0.2*(attempt.Q)-785).tolist() )

    def test_i(self):
        """ i is defined, and has the correct value when the program terminates """
        self.assertDefined(attempt, "i", int)
        self.assertEqual(attempt.i, 10000)

    def test_output(self):
        """ Ensure the output is correct, and formatted as listed in the question description. """
        out = f.getvalue()
        self.assertEqual("The equilibrium quantity for game one is 41000 with a price of 41.\nIf the Broncos win game one, the equilibrium quantity will be 4120 with a price of 39.\n", out)

if __name__ == "__main__":
    run_tests(Tests)
