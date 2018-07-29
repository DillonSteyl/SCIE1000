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
		""" Height is taken as input """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_called_once()
			
	def test_tall(self):
		""" 'You are tall enough to ride.' is printed if height > 130 """
		user_input = str(randint(130, 210))
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You are tall enough to ride.")
				
	def test_small(self):
		""" 'You are not tall enough to ride!' is printed if height < 130 """
		user_input = str(randint(0, 130))
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You are not tall enough to ride!")
				
	def test_medium(self):
		""" 'You are tall enough to ride.' is printed if height == 130 """
		user_input = "130"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), "You are tall enough to ride.")
		
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
