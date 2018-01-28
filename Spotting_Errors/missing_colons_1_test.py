from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch
import sys
from io import StringIO

# Inherit from PythonTestCase to give access to helper functions
class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass

    def test_works_for_negative(self):
        """ Test case 1: negative input"""
        user_input = "-1"
        expected = "The weight is negative, this is not valid"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_works_for_small(self):
        """ Test case 2: small breed"""
        user_input = "1"
        expected = "The weight of this dog is that of a small breed dog"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_works_for_medium(self):
        """ Test case 3: medium breed"""
        user_input = "20"
        expected = "The weight of this dog is that of a medium breed dog"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_works_for_medium(self):
        """ Test case 4: large breed"""
        user_input = "50"
        expected = "The weight of this dog is that of a large breed dog"
        with patch("builtins.input", return_value=user_input):
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

