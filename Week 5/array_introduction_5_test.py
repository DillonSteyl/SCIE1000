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
      
	def test_array1(self):
		""" array1 is correct"""
		user_input = "5"
		with patch("builtins.input", return_value=user_input) as input_call:
				with patch("sys.stdout", new=StringIO()) as output:
					import attempt
					self.assertEqual(attempt.array1.tolist(), [3,3.25,3.5,3.75,\
					4,4.25,4.5,4.75,5,5.25,5.5,5.75,6,6.25,6.5,6.75,7,7.25,\
					7.5,7.75,8])
    
    
	def test_array2(self):
		""" array2 is correct"""
		user_input = "5"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.array2.tolist(), [-3, -2, -1, 0, 1, 2, 3])
		
	def test_array3(self):
		""" array3 is correct"""
		user_input = "5"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.array3.tolist(), [0, 0, 0, 0, 0])
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
