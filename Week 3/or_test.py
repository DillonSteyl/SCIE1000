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
        """Student can take the course with HELP2000 and HELP2500, so "You can take this course." is printed."""
        user_input = ["1","0","1", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You can take this course.")

    def test_allowed2(self):
        """Student can take the course with HELP2001 and HELP2500, so "You can take this course." is printed."""
        user_input = ["0","1","1", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You can take this course.")
				

    def test_00000(self):
        """ Student has taken no courses, so "You cannot take this course, sorry!" is printed."""
        user_input = ["0","0","0", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_10110(self):
        """ Student has taken HELP3001, so "You cannot take this course, sorry!" is printed."""
        user_input = ["1","0","1", "1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_11000(self):
        """ Student has taken not taken HELP2500, so "You cannot take this course, sorry!" is printed."""
        user_input = ["1","1","0", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_00100(self):
        """ Student has taken not taken HELP2000 or HELP2001, so "You cannot take this course, sorry!" is printed."""
        user_input = ["0","0","1", "0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")
				
		
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)
