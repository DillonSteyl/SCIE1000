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
		

	def test_output(self):
		""" Printing all the correct values. """
		expected = "Friend A -- Avg: 49.25 Max: 73.0 Sum: 394.0\nFriend B -- Avg: 49.5 Max: 69.0 Sum: 396.0\nThe maximum difference is 6.0\nFriend B will have the most popular party."
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_meanA(self):
		""" avgA is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.avgA, 49.25)
        
	def test_meanB(self):
		""" avgB is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.avgB, 49.5)
        
	def test_maxA(self):
		""" maxA is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.maxA, 73.0)
        
	def test_maxB(self):
		""" maxB is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.maxB, 69.0)
        
	def test_sumA(self):
		""" sumA is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.sumA, 394.0)
        
	def test_sumB(self):
		""" sumB is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.sumB, 396.0)
        
	def test_maxDiff(self):
		""" maxDiff is the correct value."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.maxDiff, 6.0)
        
	def test_friendA(self):
		""" friendA has the correct values."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.friendA.tolist(), [10., 26., 40., 51., 59., 65., 70., 73.])
        
	def test_friendB(self):
		""" friendB has the correct values."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.friendB.tolist(), [10., 32., 44., 53., 59., 63., 66., 69.])
        
	def test_diff(self):
		""" diff has the correct values, which are all positive."""		
		with patch("builtins.input") as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.diff.tolist(), [0., 6., 4., 2., 0., 2., 4., 4.])

	
# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)
