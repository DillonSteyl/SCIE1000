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

    def testscenario1(self):
        """ User enters [50] and the program gives the correct output """
        expected = "The number of years that have passed since the fossil was formed is approximately 5730.0"
        user_input = ["50"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def testscenario2(self):
        """ User enters [105, 25] and the program gives the correct output """
        user_input = ["105", "25"]
        expected = "Please try again as this percentage is not valid.\nThe number of years that have passed since the fossil was formed is approximately 11460.0"
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def testscenario3(self):
        """ User enters [100, 10, 8, 12.5] and the program gives the correct output """
        expected = "Please try again as this percentage is not valid.\nPlease try again as this percentage is not valid.\nPlease try again as this percentage is not valid.\nThe number of years that have passed since the fossil was formed is approximately 17190.0"
        user_input = ["100", "10", "8", "12.5"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
