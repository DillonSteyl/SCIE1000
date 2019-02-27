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
		""" Function 'cylVolume' is defined """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			self.assertMethodDefined(attempt, "cylVolume", 2)
		
	def test_function(self):
		""" Funtion 'cylVolume' behaves as expected """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			r = randint(1,15)
			h = randint(5,20)
			self.assertEqual(attempt.cylVolume(r, h), pi*r**2 * h )
			
	def test_output(self):
		""" Program correctly prints the volume of the cylinder with radius and height specified by the user """
		user_input = [str(randint(1,15)), str(randint(5,20))]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), str( attempt.cylVolume(int(user_input[0]), int(user_input[1])) ) )
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
