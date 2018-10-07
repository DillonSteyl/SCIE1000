import matplotlib
matplotlib.use('Agg')

from python_test_case import PythonTestCase, run_tests
from pylab import *
import sys
from io import StringIO
from unittest.mock import patch, call
import random

INPUT = ["4", "5"]

class Tests(PythonTestCase):

	def setUp(self):
		try:
			del sys.modules["attempt"]
		except KeyError:
			pass

	@patch('builtins.input', side_effect = INPUT)
	def test_title(self, input_call):
		""" The graph has the correct title """
		import attempt
		g = gca()
		self.assertEqual(g.get_title(), "Exponential Model")
		clf()

	@patch('builtins.input', side_effect = INPUT)
	def test_x_label(self, input_call):
		""" The x axis is labelled correctly """
		import attempt
		g = gca()
		self.assertEqual(g.get_xlabel(), "x")
		clf()

	@patch('builtins.input', side_effect = INPUT)
	def test_y_label(self, input_call):
		""" The y axis is labelled correctly """
		import attempt
		g = gca()
		self.assertEqual(g.get_ylabel(), "y")
		clf()

	@patch('builtins.input', side_effect = INPUT)
	def test_x_data(self, input_call):
		""" The plot uses the correct x values """
		import attempt
		g = gca()
		self.assertEqual(gca().get_lines()[0].get_xdata().tolist(), attempt.x.tolist())
		clf()
		
	@patch('builtins.input', side_effect = INPUT)
	def test_colour(self, input_call):
		""" The plot uses the colour black """
		import attempt
		g = gca()
		self.assertIn(g.get_lines()[0].get_color(), [(0.0, 0.0, 0.0, 1), 'k', 'black'])
		clf()
		
	@patch('builtins.input', side_effect = INPUT)
	def test_marker(self, input_call):
		""" The plot uses round markers ("o")"""
		import attempt
		g = gca()
		self.assertIn(g.get_lines()[0].get_marker(), "o")
		clf()

	@patch('builtins.input', side_effect = INPUT)
	def test_y_data(self, input_call):
		""" The plot uses the correct y values """
		import attempt
		g = gca()
		self.assertEqual(gca().get_lines()[0].get_ydata().tolist(), attempt.y.tolist())
		clf()

	@patch('builtins.input', side_effect = INPUT)
	def test_file(self, input_call):
		"""Show is used to display plot"""
		import attempt
		a = False
		if "show()" in open('attempt.py').read():
			a = True
		self.assertEquals(a,True)
		savefig("output.png")
		clf()
    
	@patch('builtins.input', side_effect = INPUT)
	def test_one_line(self, input_call):
		""" One line on plot"""
		import attempt
		g = gca()
		self.assertEquals(len(g.get_lines()), 1)
		clf()
    
    
	def test_output1(self):
		""" Prints correct messages when both values are close enough. """
		random.seed(1)
		expected = "The A0 value is close enough.\nThe k value is close enough.\nThe actual A0 value is 17 and the actual k value is -0.11"
		user_input = ["14", "-0.14"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output2(self):
		""" Prints correct messages when only the k value is close enough."""
		random.seed(2)
		expected = "The A0 value is incorrect.\nThe k value is close enough.\nThe actual A0 value is 19 and the actual k value is 0.137"
		user_input = ["15", "0.14"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output3(self):
		""" Prints correct messages when only the A0 value is close enough. """
		random.seed(3)
		expected = "The A0 value is close enough.\nThe k value is incorrect.\nThe actual A0 value is 11 and the actual k value is -0.079"
		user_input = ["12", "0.1"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output4(self):
		""" Prints correct messages when both values are wrong. """
		random.seed(4)
		expected = "The A0 value is incorrect.\nThe k value is incorrect.\nThe actual A0 value is 2 and the actual k value is -0.079"
		user_input = ["6", "0.02"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
