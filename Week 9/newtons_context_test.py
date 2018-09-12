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
		""" Function 'fdash' returns "2473.08191" for input "10" """
		self.assertEqual(attempt.fdash(10), 2473.08191)
		
	def test_function_zero(self):
		""" Function 'fdash' returns "1000.0" for input "0" """
		self.assertEqual(attempt.fdash(0), 1000.0)
		
	def test_function_neg15(self):
		""" Function 'fdash' returns "118.09164" for input "-15" """
		self.assertEqual(attempt.fdash(-15), 118.09164)
		
	def test_function_defined2(self):
		""" Function 'f' is defined as f(x, max_voltage) """
		self.assertMethodDefined(attempt, "f", 2)
			
	def test_function_102(self):
		""" Function 'f' returns "6487.21271" for input "10, 10000" """
		self.assertEqual(attempt.f(10,10000), 6487.21271)
		
	def test_function_zero2(self):
		""" Function 'f' returns "-5000.0 for input "0, 5000" """
		self.assertEqual(attempt.f(0,5000), -5000.0)
		
	def test_function_neg152(self):
		""" Function 'f' returns "-9385.49829" for input "-15, 2300" """
		self.assertEqual(attempt.f(-15,2300), -9385.49829)
		
	def test_function_defined3(self):
		""" Function 'onestep' is defined as onestep(x, max_voltage)"""
		self.assertMethodDefined(attempt, "onestep", 2)
			
	def test_function_103(self):
		""" Function 'onestep' returns "7.37687" for input "10, 10000" """
		self.assertEqual(attempt.onestep(10,10000), 7.37687)
		
	def test_function_zero3(self):
		""" Function 'onestep' returns "5.0" for input "0, 5000" """
		self.assertEqual(attempt.onestep(0,5000), 5.0)
		
	def test_function_neg153(self):
		""" Function 'onestep' returns "64.4764" for input "-15, 2300" """
		self.assertEqual(attempt.onestep(-15, 2300), 64.4764)
		
	def test_function_defined4(self):
		""" Function 'newtons' is defined as newtons(x, n, p, max_voltage)"""
		self.assertMethodDefined(attempt, "newtons", 4)
			
	def test_function_104(self):
		""" Function 'newtons' returns "7.03468" for input "10, 15, 1, 10000". Make sure it is returning only one number. """
		self.assertEqual(attempt.newtons(10, 15, 1, 10000), 7.03468)
		
	def test_function_zero4(self):
		""" Function 'newtons' returns "2.63115" for input "1, 2, 0.5, 3000". Make sure it is returning only one number.  """
		self.assertEqual(attempt.newtons(1, 2, 0.5, 3000), 2.63115)
		
	def test_function_neg154(self):
		""" Function 'newtons' returns "6.36826" for input "5, 100, 0.01, 8756". Make sure it is returning only one number.  """
		self.assertEqual(attempt.newtons(5, 100, 0.01, 8756), 6.36826)
					
	def test_function_defined5(self):
		""" Function 'will_it_rupture' is defined """
		self.assertMethodDefined(attempt, "will_it_rupture", 2)
			
	def test_function_104(self):
		""" Function 'will_it_rupture' returns "1, 7.03467" for input "5, 10000" """
		a, b = attempt.will_it_rupture(5, 10000)
		self.assertEqual(a, 1)
		self.assertEqual(b, 7.03467)
		
	def test_function_zero4(self):
		""" Function 'will_it_rupture' returns "0, 7.56458" for input "8, 11042" """
		a, b = attempt.will_it_rupture(8, 11042)
		self.assertEqual(a, 0)
		self.assertEqual(b, 7.56458)
		
	def test_function_neg154(self):
		""" Function 'will_it_rupture' returns "0, 0.95345" for input "0.95345, 1000" """
		a, b = attempt.will_it_rupture(0.95345, 1000)
		self.assertEqual(a, 0)
		self.assertEqual(b, 0.95345)
		

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
