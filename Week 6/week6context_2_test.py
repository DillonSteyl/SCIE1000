from python_test_case import PythonTestCase, run_tests
from pylab import *
from unittest.mock import patch, call
import sys
from io import StringIO


class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_function_behaviour(self):
        """ Function 'get_new_savings' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            savings = uniform(1,100)
            interest_rate = uniform(0.01,0.1)
            debts = uniform(1,100)
            self.assertEqual(attempt.get_new_savings(savings, interest_rate, debts), ((1+interest_rate)*savings - debts))

    def test_function_behaviour2(self):
        """ Function 'check_goal' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            savings = 100
            goal = 100
            self.assertEqual(attempt.check_goal(savings, goal), 1)

    def test_function_behaviour3(self):
        """ Function 'check_goal' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            savings = 99
            goal = 100
            self.assertEqual(attempt.check_goal(savings, goal), 0)

    def test_function_behaviour4(self):
        """ Function 'get_new_savings' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            savings = uniform(1,100)
            goal = uniform(100,1000)
            self.assertEqual(attempt.get_difference(savings, goal), (goal - savings))

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)	
