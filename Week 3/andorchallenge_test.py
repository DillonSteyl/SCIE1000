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
			
    def test_allowed1(self):
        """Can ride with height=170, so "Enjoy your ride!" is printed."""
        user_input = ["170","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Enjoy your ride!")

    def test_allowed2(self):
        """Can ride with height=120 and adult=1, so "Enjoy your ride!" is printed."""
        user_input = ["120","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Enjoy your ride!")
                
    def test_edge_case_1(self):
        """Can ride with height=200, so "Enjoy your ride!" is printed."""
        user_input = ["200","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Enjoy your ride!")

    def test_edge_case_2(self):
        """Can ride with height=130, so "Enjoy your ride!" is printed."""
        user_input = ["130","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Enjoy your ride!")
                
     def test_edge_case_3(self):
        """Can ride with height=100 and adult=1, so "Enjoy your ride!" is printed."""
        user_input = ["100","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Enjoy your ride!")
				

    def test_not_allowed1(self):
        """Cannot ride with height=90, so "Sorry, you cannot ride this rollercoaster." is printed."""
        user_input = ["90","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Sorry, you cannot ride this rollercoaster.")

    def test_not_allowed2(self):
        """ Cannot ride with height=201, so "Sorry, you cannot ride this rollercoaster." is printed."""
        user_input = ["201","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Sorry, you cannot ride this rollercoaster.")

    def test_not_allowed3(self):
        """ Cannot ride with height=129 and adult=0, so "Sorry, you cannot ride this rollercoaster." is printed."""
        user_input = ["129","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Sorry, you cannot ride this rollercoaster.")

    def test_not_allowed4(self):
        """ Cannot ride with height=220 and adult=1, so "Sorry, you cannot ride this rollercoaster." is printed."""
        user_input = ["220","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Sorry, you cannot ride this rollercoaster.")
				
		
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)
