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
        """ Answer 1000.0 with input 2018, 0"""
        user_input = ["2018","0"]
        year = 1
        string = ""
        string+="The purchasing power: "+ str(1000*(1.03)**(2018-2018))+  "in year "+ str(2018)
        string+="\nThanks, and have a good day!"
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),string)			
                
    def test2(self):
        """ Answer 942.5959091337544, 701.3798801929728 with input 2020, 2030, 0"""
        user_input = ["2020","2030","0"]
        year = 1
        string = ""
        string+="The purchasing power: "+ str(1000*(1.03)**(2018-2020))+ " in year "+ str(2020)
        string+="\nThe purchasing power: "+ str(1000*(1.03)**(2018-2030))+ " in year "+ str(2030)
        string+="\nThanks, and have a good day!"
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),string)	
               
    def test3(self):
        """ Answer 19218.6319808563, 1000.0, 52.032839850208966 with input 1918, 2018, 2118, 0"""
        user_input = ["1918","2018","2118","0"]
        year = 1
        string = ""
        string+="The purchasing power: "+ str(1000*(1.03)**(2018-1918))+ " in year "+ str(1918)
        string+="\nThe purchasing power: "+str(1000*(1.03)**(2018-2018))+ " in year "+ str(2018)
        string+="\nThe purchasing power: "+str(1000*(1.03)**(2018-2118))+" in year "+ str(2118)
        string+="\nThanks, and have a good day!"
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),string)
    	
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)
