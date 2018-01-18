from python_test_case import PythonTestCase, run_tests
from contextlib import redirect_stdout
from os import devnull
import unittest

#output handling
import io
from unittest.mock import patch

f = io.StringIO()
with redirect_stdout(f):
    import attempt

# Inherit from PythonTestCase to give access to helper functions
class Tests(PythonTestCase):

    def test_quad_formula_defined(self):
        """ check you are running the loop for the correct number of times (the loop should run 10 times) """

        self.assertDefined(attempt, "i", int)

        #check output
        
        s = f.getvalue().strip()
        self.assertEqual("The population after 10 years in Queensland is 5080578", s)


# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
