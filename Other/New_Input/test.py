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


    def test_works_for_positive(self):
        """ Passing possitive number worked"""
        user_input = "2"
        expected = "2"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_works_for_negative(self):
        """Passing negative number worked"""
        user_input = "-2"
        expected = "2"

        with patch("builtins.input", return_value=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                input_call.assert_called_with('Please enter a number: ')
                self.assertEqual(output.getvalue().strip(), expected)



    def test_works_for_zero(self):
        """Passing zero number worked"""
        user_input = "0"
        expected = "0"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
