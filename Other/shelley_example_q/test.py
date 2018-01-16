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

    def test_a_is_defined(self):
        """ is_even is defined """
        # check the variable a is defined

        self.assertDefined(attempt, "a", int)

    def test_a_is_2(self):
        """ make a = 2"""

        self.assertEqual(attempt.a, 2)

    def test_orint_a(self):
        """ check print a = 2"""
        s = f.getvalue().strip()
        self.assertEqual("a = 2", s)


# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
