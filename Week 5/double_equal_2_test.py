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
                """ Correct output when the number doesn't exist in the array """
                user_input = "2"
                expected = "The number 2.0 appears in the array 0 times"
                with patch("builtins.input", return_value=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """ Correct output when the number exists multiple times in the array """
                user_input = "5"
                expected = "The number 5.0 appears in the array 3 times"
                with patch("builtins.input", return_value=user_input) as input_call:
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

