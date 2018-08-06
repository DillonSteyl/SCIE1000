from python_test_case import PythonTestCase, run_tests

import attempt

class Tests(PythonTestCase):

	def test_win_loss_draw(self):
		""" 'win_loss_draw' array contains the correct values """
		self.assertEqual(attempt.win_loss_draw.tolist(), [1.0, 2.0, 1.0,\
		2.0, 1.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 1.0, 1.0, 1.0, \
		3.0, 2.0, 2.0, 2.0, 1.0, 3.0, 3.0, 1.0, 1.0, 3.0, 3.0, 2.0, 1.0, 3.0, 1.0])
		
	def test_i(self):
		""" 'i' finishes with the correct value """
		self.assertEqual(attempt.i, 30)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
