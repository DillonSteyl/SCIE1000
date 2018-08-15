from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_mean(self):
		""" average has the correct value """
		self.assertEqual(attempt.average, 1509.05)
		
	def test_maximum(self):
		""" maximum has the correct value """
		self.assertEqual(attempt.maximum, 6701)
		
	def test_minimum(self):
		""" minimum has the correct value """
		self.assertEqual(attempt.minimum, -148)
		
	def test_total(self):
		""" total has the correct value """
		self.assertEqual(attempt.total, 1509050)
		
	def test_length(self):
		""" length has the correct value """
		self.assertEqual(attempt.length, 1000)
		
	def test_difference(self):
		""" difference has the correct value """
		self.assertEqual(attempt.difference, 6849)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
