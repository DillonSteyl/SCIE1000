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
			
	def test_function_10(self):
		""" Function 'fdash' returns "0.22955" for input "10" """
		self.assertEqual(attempt.fdash(10), 0.22955)
		
	def test_function_zero(self):
		""" Function 'fdash' returns "0.25" for input "0" """
		self.assertEqual(attempt.fdash(0), 0.25)
		
	def test_function_neg15(self):
		""" Function 'fdash' returns "0.279" for input "-15" """
		self.assertEqual(attempt.fdash(-15), 0.279)
		
	def test_function_defined2(self):
		""" Function 'onestep' is defined """
		self.assertMethodDefined(attempt, "onestep", 3)
			
	def test_function_111(self):
		""" Function 'onestep' returns "1.248" for input "1,1,1" """
		self.assertEqual(attempt.onestep(1,1,1), 1.248)
		
	def test_function_101805(self):
		""" Function 'onestep' returns "18.11478" for input "10,18,0.5" """
		self.assertEqual(attempt.onestep(10,18,0.5), 18.11478)
		
	def test_function_1042036810(self):
		""" Function 'onestep' returns "205.9671" for input "10.4,203.68,10" """
		self.assertEqual(attempt.onestep(10.4,203.68,10), 205.9671)
		
	def test_function_defined3(self):
		""" Function 'eulers' is defined """
		self.assertMethodDefined(attempt, "eulers", 4)
			
	def test_function_one(self):
		""" Function 'eulers' returns "11.2223" for input "0,10,0.5,10" """
		self.assertEqual(attempt.eulers(0,10,0.5,10), 11.2223)
		
	def test_function_two(self):
		""" Function 'eulers' returns "12.26876" for input "12,12,0.1,12" """
		self.assertEqual(attempt.eulers(12,12,0.1,12), 12.26876)
		
	def test_function_three(self):
		""" Function 'eulers' returns "97.4465" for input "38.2,95.9,0.1,100" """
		self.assertEqual(attempt.eulers(38.2,95.9,0.1,100), 97.4465)
		
	def test_function_defined4(self):
		""" Function 'will_it_hit' is defined """
		self.assertMethodDefined(attempt, "will_it_hit", 1)
			
	def test_function_big(self):
		""" Function 'will_it_hit' returns "0, 149.65398" for input "1" """
		a, b = attempt.will_it_hit(1)
		self.assertEqual(a, 0)
		self.assertEqual(b, 149.65398)
		
	def test_function_medium(self):
		""" Function 'will_it_hit' returns "0, 149.96566" for input "0.1" """
		a, b = attempt.will_it_hit(0.1)
		self.assertEqual(a, 0)
		self.assertEqual(b, 149.96566)
		
	def test_function_small(self):
		""" Function 'will_it_hit' returns "1, 149.99671" for input "0.01" """
		a, b = attempt.will_it_hit(0.01)
		self.assertEqual(a, 1)
		self.assertEqual(b, 149.99671)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
