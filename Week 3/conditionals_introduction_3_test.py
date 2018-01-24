from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
from pylab import *

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
			
	def test_input_exists(self):
		""" Radius is taken as input """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_called_once()

	def test_true(self):
		""" Prints the message 'This is the unit circle!' if the radius is exactly 1 """
		user_input = "1"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "Area: " + str(attempt.area) + "\nThis is the unit circle!")
				#assert("This is the unit circle!" in output.getvalue().strip())

	def test_false(self):
		""" Does not print the message 'This is the unit circle!' if the radius is not 1 """
		user_input = str(randint(2,100)) # pick a random number between 2 and 100
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				assert("This is the unit circle!" not in output.getvalue())
		
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)