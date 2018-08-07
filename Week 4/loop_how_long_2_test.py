from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
from pylab import *

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass
			
    def test1(self):
        """ Answer is 40 with input 2, 5, 4, 0"""
        user_input = ["2","5","4","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"The final answer is 40.0")			
    def test2(self):
        """ Answer is 1 with input 1, 0"""
        user_input = ["1", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"The final answer is 1.0")
               
    def test3(self):
        """ Answer is -32 with input 4, -8, 0"""
        user_input = ["4", "-8", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"The final answer is -32.0")
    
    def test4(self):
        """ Answer is 362880 for input 1, 2, 3, 4, 5, 6, 7, 8, 9, 0"""
        user_input = [str(i) for i in range(1,10)]+["0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"The final answer is 362880.0")
   
		
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)
