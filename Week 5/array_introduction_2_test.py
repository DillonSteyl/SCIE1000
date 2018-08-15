from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_squares(self):
		""" 'squares' array contains the first 4 square numbers """
		self.assertEqual(attempt.squares.tolist(), [ 1,  4,  9, 16])
		
	def test_cubes(self):
		""" 'cubes' array contains the first 4 cube numbers """
		self.assertEqual(attempt.cubes.tolist(), [ 1,  8, 27, 64])
	
	def test_result(self):
		""" 'result' array contains the first 4 result numbers """
		self.assertEqual(attempt.result.tolist(), [2., 4., 6., 8.])
		
		
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
