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
			
	def test7(self):
		""" Prints "This is a happy number."  with input 7"""
		user_input = "7"
		expected = "This is a happy number."
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

	def test14(self):
		""" Prints "This is a happy number."  with input 14"""
		user_input = "14"
		expected = "This is a happy number."
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test6(self):
		""" Prints "Close enough." with input 6 """
		user_input = "6"
		expected = "Close enough."
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test4(self):
		""" Prints "This is a sad number." with input 4"""
		user_input = "4"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "This is a sad number.")
				
	def test8(self):
		""" Prints "This is a sad number." with input 8"""
		user_input = "8"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "This is a sad number.")
	
	def testneg7(self):
		""" Prints "This is a happy number."  with input -7"""
		user_input = "-7"
		expected = "This is a happy number."
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def testneg8(self):
		""" Prints "Close enough." with input -8 """
		user_input = "-8"
		expected = "Close enough."
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test1234(self):
		""" Prints "This is a sad number." with input 1234"""
		user_input = "1234"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "This is a sad number.")
				
				
				

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
