from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_var(self):
		""" 'squares' array contains the first 5 square numbers """
		self.assertEqual(attempt.squares.tolist(), [1,4,9,16,25])
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)