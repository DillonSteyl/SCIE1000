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
                """ Correct value for the hypotenuse is calculated and printed (case 1)"""
                user_input = ["3", "4"]
                expected = "The third side length of the triangle is 5.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(attempt.h, 5.0)
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """ Correct value for the hypotenuse is calculated and printed (case 2)"""
                user_input = ["6", "8"]
                expected = "The third side length of the triangle is 10.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(attempt.h, 10.0)
                                self.assertEqual(output.getvalue().strip(), expected)


# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError: invalid syntax")
        except SyntaxError:
            print("SyntaxError: invalid syntax")
