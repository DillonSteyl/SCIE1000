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

  def test_call(self):
		""" Correct input message is used """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_has_calls([call("Enter length: ")])
      
      
	def test_array1(self):
		""" array1 is correct"""
		import attempt
		self.assertEqual(attempt.array1.tolist(), [3., 3.1, 3.2, 3.3, 3.4, 3.5,\
    3.6, 3.7, 3.8, 3.9, 4., 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5., \
    5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6., 6.1, 6.2, 6.3, 6.4, 6.5,\
    6.6, 6.7, 6.8, 6.9, 7., 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.])
    
    
  def test_array2(self):
		""" array2 is correct"""
		import attempt
		self.assertEqual(attempt.array2.tolist(), [-3, -2, -1, 0, 1, 2, 3])
  
  def test_array3(self):
		""" array3 is correct"""
		import attempt
		self.assertEqual(attempt.array3.tolist(), [0, 0, 0, 0, 0])
		
	def test_out(self):
		""" Output is correct """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "[3. 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4. 4.1 4.2 4.3 4.4 4.5 4.6 4.7
 4.8 4.9 5. 5.1 5.2 5.3 5.4 5.5 5.6 5.7 5.8 5.9 6. 6.1 6.2 6.3 6.4 6.5
 6.6 6.7 6.8 6.9 7. 7.1 7.2 7.3 7.4 7.5 7.6 7.7 7.8 7.9 8.] [-3. -2. -1. 0. 1. 2. 3.] [0. 0. 0. 0. 0.]"
			self.assertEqual(output.getvalue().strip(), expected)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
