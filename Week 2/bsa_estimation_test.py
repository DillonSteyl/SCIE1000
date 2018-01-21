from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
import unittest
from pylab import *

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
				
	def test_calls(self):
		""" Correct input messages are used """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_has_calls([call("Enter mass: "), call("Enter height: ")])
			
	def test_var_values(self):
		""" Calcultion of all BSA estimates are correct """
		user_input = ["70", "180"]
		with patch("builtins.input", side_effect=user_input):
			import attempt
			self.assertEqual(attempt.mostellar_bsa, 0.0167*sqrt(attempt.mass*attempt.height))
			self.assertEqual(attempt.dubois_bsa, 0.007184 * attempt.mass**0.425 * attempt.height**0.725)
			self.assertEqual(attempt.haycock_bsa, 0.024265 * attempt.height**0.3964 * attempt.mass**0.5378)
			
	def test_output(self):
		""" Output is correct """
		user_input = ["42", "162"]
		with patch("builtins.input", side_effect=user_input):
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				mostellar_string = "Mostellar BSA Estimate: " + str(attempt.mostellar_bsa)
				dubois_string = "Dubois BSA Estimate: " + str(attempt.dubois_bsa)
				haycock_string = "Haycock BSA Estimate: " + str(attempt.haycock_bsa)
				expected = mostellar_string + "\n" + dubois_string + "\n" + haycock_string
				self.assertEqual(output.getvalue().strip(), expected)
				
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)