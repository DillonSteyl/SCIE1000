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
			
	def test1(self):
		""" Prints ":)" once with input 1"""
		user_input = "1"
		expected = ":)"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test2(self):
		""" Prints ":)" twice with input 2 """
		user_input = "2"
		expected = ":)\n:)"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test0(self):
		""" Prints nothing with input 0"""
		user_input = "0"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "")
				
	def test8(self):
		""" Prints ":)" 8 times with input 8"""
		user_input = "8"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), ":)\n:)\n:)\n:)\n:)\n:)\n:)\n:)")

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
