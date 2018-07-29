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
			
    def test_allowed(self):
        """Student can take the course if they have completed HELP1000 and HELP1500 only."""
        user_input = ["1","1","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You can take this course.")
				
    def test_000(self):
        """ Student has taken no courses, so they cannot take the course."""
        user_input = ["0","0","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")
				
    def test_001(self):
        """ Student has taken only HELP2001, so they cannot take the course."""
        user_input = ["0","0","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_010(self):
        """ Student has taken only HELP1500, so they cannot take the course."""
        user_input = ["0","1","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_011(self):
        """ Student has taken HELP1500 and HELP2000, so they cannot take the course"""
        user_input = ["0","1","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_100(self):
        """ Student has taken only HELP1000, so they cannot take the course."""
        user_input = ["1","0","0"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")

    def test_101(self):
        """ Student has taken only HELP1000 and HELP2001, so they cannot take the course."""
        user_input = ["1","0","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")
                    
    def test_111(self):
        """ Student has taken all courses, so they cannot take the course."""
        user_input = ["1","1","1"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"You cannot take this course, sorry!")
		
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)

