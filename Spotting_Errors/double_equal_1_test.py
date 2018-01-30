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
                """ Correct output when number = 0 """
                user_input = "0"
                expected = "Zero is a special case"
                with patch("builtins.input", return_value=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """ Correct output when number = 1 """
                user_input = "1"
                expected = "One is a special case"
                with patch("builtins.input", return_value=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case3(self):
                """ Correct output when the number is a perfect square"""
                user_input = "16"
                expected = "The number 16 is a perfect square of 4.0"
                with patch("builtins.input", return_value=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)
                                
        def test_output_case4(self):
                """ Correct output when the number is NOT a perfect square"""
                user_input = "10"
                expected = ""
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

