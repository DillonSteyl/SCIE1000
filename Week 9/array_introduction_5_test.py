from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_squares(self):
		""" 'squares' array contains the correct values """
		self.assertEqual(attempt.squares.tolist(), [0,1,4,9,16,25,36,49,64,81])
		
	def test_i(self):
		""" 'i' finishes with the correct value """
		self.assertEqual(attempt.i, 10)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
