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
		""" Function 'circleArea' is defined """
		self.assertMethodDefined(attempt, "circleArea", 1)
			
	def test_function_behaviour(self):
		""" Function 'circleArea' behaves as expected """
		test_val = randint(0,80)
		self.assertEqual(attempt.circleArea(test_val), pi*test_val**2)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
