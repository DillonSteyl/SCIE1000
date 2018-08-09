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
                """ Correct output when the input (x) is less than 1 """
                user_input = "0"
                expected = ""
                with patch("builtins.input", return_value=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """ Correct output when the input (x) is 2 (hint- check you are looping the correct number of times) """
                user_input = "2"
                expected = "2.0 to the power of 2.0 is 4.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case3(self):
                """ Correct output when the input (x) is more than 2 """
                user_input = "5"
                expected = "2.0 to the power of 5.0 is 32.0"
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
