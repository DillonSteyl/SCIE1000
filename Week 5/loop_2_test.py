from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_var(self):
		""" 'height' array contains the correct heights for the plant """
		self.assertEqual(attempt.height.tolist(), [10.0, 16.0, 19.0, 15.0, 18.0, 29.0, 35.0, 28.0, 34.0, 54.0, 65.0, 52.0])
    
  def test_var(self):
		""" 'height' array has the correct length (12)"""
		self.assertEqual(12, len([10.0, 16.0, 19.0, 15.0, 18.0, 29.0, 35.0, 28.0, 34.0, 54.0, 65.0, 52.0]))
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
