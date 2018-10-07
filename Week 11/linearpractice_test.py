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
		self.assertEqual(g.get_title(), "Linear Model")
		savefig("output.png")
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
		g.title("4")
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
		expected = "Both values are close enough!\nThe actual m value is -7 and the actual c value is -9"
		user_input = ["-8", "-7"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output2(self):
		""" Prints correct messages when only the m value is close enough."""
		random.seed(2)
		expected = "The m value is close enough, but the c value is not.\nThe actual m value is 9 and the actual c value is 13"
		user_input = ["10", "0"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output3(self):
		""" Printing all the correct values. """
		random.seed(3)
		expected = "The c value is close enough, but the m value is not.\nThe actual m value is -5 and the actual c value is -5"
		user_input = ["-10", "-7"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_output4(self):
		""" Printing all the correct values. """
		random.seed(4)
		expected = "Both values are not close enough.\nThe actual m value is -5 and the actual c value is -3"
		user_input = ["5", "5"]
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				clf()
				self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
