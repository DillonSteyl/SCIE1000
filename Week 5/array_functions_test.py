from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_mean(self):
		""" average has the correct value """
		self.assertEqual(attempt.average, [1,4,9,16,25])
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
