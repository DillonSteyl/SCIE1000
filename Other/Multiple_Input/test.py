from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch
import sys
from io import StringIO

# Inherit from PythonTestCase to give access to helper functions
class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass
			
	def test_pos_pos(self):
		""" Passing both positive worked """
		user_input = ["2", "3"]
		expected = "2\n3\nSum: 5"
		with patch("builtins.input", side_effect=user_input):
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

	def test_neg_neg(self):
		""" Passing both negative worked """
		user_input = ["-2", "-4"]
		expected = "2\n-4\nSum: -2"
		with patch("builtins.input", side_effect=user_input):
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
