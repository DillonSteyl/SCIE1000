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

	def test_function_defined(self):
		""" Function 'displacement' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "displacement", 3)
		
	def test_function_behaviour(self):
		""" Function 'displacement' behaves as expected """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			v0 = uniform(1,20)
			a = uniform(-20,20)
			t = randint(1, 6)
			self.assertEqual(attempt.displacement(v0, a, t), (v0 * t) + (0.5 * a * t**2))
			
	def test_input_exists(self):
		""" Program takes 3 inputs """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertEqual(3, input_call.call_count)

	def test_output(self):
		""" Correctly uses the 'displacement' function to calculate displacement and print the required output """
		v0 = uniform(1,20)
		a = uniform(-20,20)
		t = randint(1, 6)
		user_input = [ str(v0), str(a), str(t) ]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				expected = "The displacement of this object at " + str(float(t)) + " seconds is: " + str(attempt.displacement(v0, a, t)) + " metres."
				self.assertEqual(output.getvalue().strip(), expected)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
