from python_test_case import PythonTestCase, run_tests
from contextlib import redirect_stdout
from os import devnull

with open(devnull, "w") as f:
    with redirect_stdout(f):
        # Redirect the stdout in case the student has global print statements
        import attempt


# Inherit from PythonTestCase to give access to helper functions
class Tests(PythonTestCase):

    def test_is_even_defined(self):
        """ is_even is defined """
        # Test that is_even is defined with 1 parameter
        self.assertMethodDefined(attempt, "is_even", 1)

    def test_works_for_even(self):
        """ is_even(2) == True and is_even(4) == True"""
        self.assertEqual(attempt.is_even(2), True)
        self.assertEqual(attempt.is_even(4), True)

    def test_works_for_odd(self):
        """ is_event(3) == False and is_even(5) == False """
        self.assertEqual(attempt.is_even(3), False)
        self.assertEqual(attempt.is_even(5), False)


# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
