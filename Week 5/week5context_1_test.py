from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO

import attempt

class Tests(PythonTestCase):
    
    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass
    
    def test_group1(self):
        """ 'group1' array contains the correct values """
        self.assertEqual(attempt.group1.tolist(), [115., 125., 135., 145., 155., 165.])
		
    def test_group2(self):
        """ 'group2' array contains the correct values """
        self.assertEqual(attempt.group2.tolist(), [134.78489153, 148.26338069, 161.74186984, 175.22035899, 188.69884815, 202.1773373 ])
        
    def test_group3(self):
        """ 'group3' array contains the correct values """
        self.assertEqual(attempt.group3.tolist(), [118., 128., 138., 148., 158., 168.])

    def test_growth_diff(self):
        """ 'growth_diff' array contains the correct values """
        self.assertEqual(attempt.growth_diff.tolist(), [16.78489153, 20.26338069, 23.74186984, 27.22035899, 30.69884815,
       34.1773373 ])

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
