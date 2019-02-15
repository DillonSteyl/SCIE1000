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
                """ Correct value for x is calculated and printed (case 1, initial=100, years=100) """
                user_input = ["100", "100"]
                expected = "The number of fish after 100 years is 12524"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """ Correct value for x is calculated and printed (case 2, initial=10, years=20) """
                user_input = ["10", "20"]
                expected = "The number of fish after 20 years is 25"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)


# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError- invalid syntax")
        except SyntaxError:
            print("SyntaxError- invalid syntax")
