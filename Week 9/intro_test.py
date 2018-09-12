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
		""" Function 'negate' is defined """
		self.assertMethodDefined(attempt, "negate", 1)
			
	def test_function_neg10(self):
		""" Function 'negate' returns "10" for input "-10" """
		self.assertEqual(attempt.negate(-10), 10)
		
	def test_function_zero(self):
		""" Function 'negate' returns "0" for zero input """
		self.assertEqual(attempt.negate(0), 0)
		
	def test_function_15(self):
		""" Function 'negate' returns "-15" for input "15" """
		self.assertEqual(attempt.negate(15), -15)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
