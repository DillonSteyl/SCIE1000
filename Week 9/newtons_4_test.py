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
		""" Function 'fdash' returns "0.12365" for input "10" """
		self.assertEqual(attempt.fdash(10), 0.12365)
		
	def test_function_zero(self):
		""" Function 'fdash' returns "0.05" for input "0""""
		self.assertEqual(attempt.fdash(0), 0.05)
		
	def test_function_neg15(self):
		""" Function 'fdash' returns "0.0059" for input "-15" """
		self.assertEqual(attempt.fdash(-15), 0.0059)
		
	def test_function_defined2(self):
		""" Function 'f' is defined """
		self.assertMethodDefined(attempt, "f", 1)
			
	def test_function_102(self):
		""" Function 'f' returns "-4.17564" for input "10" """
		self.assertEqual(attempt.f(10), -4.17564)
		
	def test_function_zero2(self):
		""" Function 'f' returns "-5" for input "0""""
		self.assertEqual(attempt.f(0), -5)
		
	def test_function_neg152(self):
		""" Function 'f' returns "-5.35427" for input "-15" """
		self.assertEqual(attempt.f(-15), -5.35427)
		
	def test_function_defined3(self):
		""" Function 'onestep' is defined """
		self.assertMethodDefined(attempt, "onestep", 1)
			
	def test_function_103(self):
		""" Function 'onestep' returns "43.76983" for input "10" """
		self.assertEqual(attempt.onestep(10), 43.76983)
		
	def test_function_zero3(self):
		""" Function 'onestep' returns "100" for input "0""""
		self.assertEqual(attempt.onestep(0), 100)
		
	def test_function_neg153(self):
		""" Function 'onestep' returns "892.50339" for input "-15" """
		self.assertEqual(attempt.onestep(-15), 892.50339)
		
	def test_function_defined4(self):
		""" Function 'newtons' is defined """
		self.assertMethodDefined(attempt, "newtons", 3)
			
	def test_function_104(self):
		""" Function 'newtons' returns "26.53469, 5" for input "10, 15, 1" """
		a,b = attempt.newtons(10,15, 1)
		self.assertEqual(a, 26.53469)
		self.assertEqual(b, 5)
		
	def test_function_zero4(self):
		""" Function 'newtons' returns "83.44563, 2" for input "0, 2, 0.5""""
		a,b = attempt.newtons(0,2,0.5)
		self.assertEqual(a, 83.44563)
		self.assertEqual(b, 2)
		
	def test_function_neg154(self):
		""" Function 'newtons' returns "26.53449, 51" for input "-15, 100, 0.1" """
		a,b = attempt.newtons(-15,100,0.1)
		self.assertEqual(a, 26.53449)
		self.assertEqual(b, 51)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
