from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
						
	def test_output_1(self):
		"""For 1, 0, -4, the value of x1 is 2.0 , and the value of x2 is -2.0"""
		user_input = ["1", "0", "-4"]
		expected1 = "The value of x1 is 2.0 , and the value of x2 is -2.0"
		expected2 = "The value of x1 is -2.0 , and the value of x2 is 2.0"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				answer = output.getvalue().strip()
				self.assertTrue(answer== expected1 or answer == expected2)

	def test_output_2(self):
		"For 2, 18 and -380, the value of x1 is 10.0 , and the value of x2 is -19.0"
		user_input = ["2", "18", "-380"]
		expected1 = "The value of x1 is 10.0 , and the value of x2 is -19.0"
		expected2 = "The value of x1 is -19.0 , and the value of x2 is 10.0"
		
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				answer = output.getvalue().strip()
				self.assertTrue(answer== expected1 or answer == expected2)
	def test_output_3(self):
		"""For 5, 3, and -48 the value of x1 is 2.812876483254676 , and the value of x2 is -3.4128764832546765"""
		user_input = ["5", "3", "-48"]
		expected1 = "The value of x1 is 2.812876483254676 , and the value of x2 is -3.4128764832546765"
		expected2 = "The value of x1 is -3.4128764832546765 , and the value of x2 is 2.812876483254676"
		
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				answer = output.getvalue().strip()
				self.assertTrue(answer== expected1 or answer == expected2)


# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
