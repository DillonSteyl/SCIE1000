from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO

class Tests(PythonTestCase):

        def setUp(self):
                try:
                        del sys.modules["attempt"]
                except KeyError:
                        pass
                        
        def test_output_case1(self):
                """ Correct output for input 10, 50, 10."""
                user_input = ["10", "50", "10"]
                expected = "This is a program to model the population of fish over time, with a growth rate of 0.05.\nYear - Number of Fish\n1   -   10\n2   -   11\n3   -   11\n4   -   12\n5   -   12\n6   -   13\n7   -   13\n8   -   14\n9   -   14\n10   -   15\nThe fish population changed by 5 fish in 10.0 years."
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)
                                
        def test_variables_case1(self):
                """ With input 10, 50, 10, correct final values for init and fish: 10 and 14.528283255165872"""
                user_input = ["10", "50", "10"]
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(attempt.init, 10)
                                self.assertEqual(attempt.fish, 14.528283255165872)

        def test_output_case2(self):
                """ Correct output for input 100, 10, 5."""
                user_input = ["100", "10", "5"]
                expected = "This is a program to model the population of fish over time, with a growth rate of 0.05.\nYear - Number of Fish\n1   -   55\n2   -   43\n3   -   36\n4   -   31\n5   -   28\nThe fish population changed by 72 fish in 5.0 years."
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)
                                
        def test_variables_case2(self):
                """ With input 100, 10, 5, correct final values for init and fish: 100 and 27.813777684228047 """
                user_input = ["10", "50", "10"]
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(attempt.init, 100)
                                self.assertEqual(attempt.fish, 27.813777684228047)


# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError: invalid syntax")
        except SyntaxError:
            print("SyntaxError: invalid syntax")
