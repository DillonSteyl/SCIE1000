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
        self.assertEqual(attempt.group2.tolist(), [134.78489153329062, 148.26338068661966, 161.74186983994872, 175.22035899327778, 188.69884814660685, 202.1773372999359])
        
    def test_group3(self):
        """ 'group3' array contains the correct values """
        self.assertEqual(attempt.group3.tolist(), [118., 128., 138., 148., 158., 168.])

    def test_growth_diff(self):
        """ 'growth_diff' array contains the correct values """
        self.assertEqual(attempt.growth_diff.tolist(), [16.78489153329062, 20.263380686619655, 23.74186983994872, 27.220358993277785, 30.69884814660685, 34.177337299935914])

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
