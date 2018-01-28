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
		""" Age is taken as input """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_called_once()
			
	def test_under18(self):
		""" 'You are under the legal drinking age.' is printed if age < 18 """
		user_input = str(randint(0,17)) # random number under 18
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You are under the legal drinking age.")
				
	def test_exact18(self):
		""" 'You can legally drink in Australia!' is printed if age = 18 """
		user_input = "18"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You can legally drink in Australia!")
				
	def test_under21(self):
		""" 'You can legally drink in Australia!' is printed if 18 <= age <= 21 """
		user_input = str(randint(19, 21)) # 18 or over, but under 21
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You can legally drink in Australia!")
				
	def test_exact21(self):
		""" 'You can legally drink, even in America!' is printed if age = 21 """
		user_input = "21"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You can legally drink, even in America!")
				
	def test_over21(self):
		""" 'You can legally drink, even in America!' is printed if age >= 21 """
		user_input = str(randint(22, 100)) # over 21
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You can legally drink, even in America!")
				
	
		
		
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)