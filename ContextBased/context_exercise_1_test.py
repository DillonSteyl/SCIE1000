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
	
    def test_function_behaviour(self):
        """ Function 'calc' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            val1 = 1
            val2 = 3
            val3 = 34
            val4 = 48
            self.assertEqual(attempt.calc(val1,val2,val3,val4), ((val2-val1)*((val3+val4)/2)))

    def test_i(self):
        """ i is defined, and has the correct value when the program terminates """
        self.assertDefined(attempt, "i", int)
        self.assertEqual(attempt.i, 7)

    def test_AUC_var(self):
        """ AUC variable is correct """
        self.assertEqual(attempt.AUC, 116.6)

    def test_CO_var(self):
        """ CO variable is correct """
        self.assertEqual(attempt.CO, (8/(attempt.AUC)*60) )

    def test_output(self):
        """ Output is formatted as listed in the question description. """
        out = f.getvalue()
        self.assertEqual("AUC = 116.6\nCardiac Output = 4.11663807890223\n", out)
        
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
