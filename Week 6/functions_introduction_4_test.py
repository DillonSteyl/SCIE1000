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
		""" Function 'my_sign' is defined """
		self.assertMethodDefined(attempt, "my_sign", 1)
			
	def test_function_pos(self):
		""" Function 'sign' returns "1" for positive input """
		test_val = randint(1,80)
		self.assertEqual(attempt.my_sign(test_val), 1)
		
	def test_function_zero(self):
		""" Function 'sign' returns "0" for zero input """
		self.assertEqual(attempt.my_sign(0), 0)
		
	def test_function_neg(self):
		""" Function 'sign' returns "-1" for negative input """
		test_val = randint(-80,-1)
		self.assertEqual(attempt.my_sign(test_val), -1)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
