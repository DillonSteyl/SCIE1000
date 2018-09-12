from python_test_case import PythonTestCase, run_tests
from pylab import *
from contextlib import redirect_stdout
from os import devnull

with open(devnull, "w") as f:
    with redirect_stdout(f):
        # Redirect the stdout in case the student has global print statements
        import attempt

class Tests(PythonTestCase):

	def test_function_defined(self):
		""" Function 'fdash' is defined """
		self.assertMethodDefined(attempt, "fdash", 1)
			
	def test_function_pos(self):
		""" Function 'fdash' returns "0.82436" for input "10" """
		self.assertEqual(attempt.negate(10), 0.82436)
		
	def test_function_zero(self):
		""" Function 'fdash' returns "0" for input "0""""
		self.assertEqual(attempt.negate(0), 0)
		
	def test_function_neg(self):
		""" Function 'fdash' returns "-0.35427" for input "-15" """
		self.assertEqual(attempt.negate(-15), -0.35427)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
