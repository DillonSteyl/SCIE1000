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

    def test_call(self):
        """ Correct input message is used """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            input_call.assert_has_calls([call("Enter the tumour size (mm): "), call("Enter the patient weight (kg): ")])

    def test_function_behaviour(self):
        """ Function 'ratio' behaves as expected """
        with patch("builtins.input", return_value="1") as input_call:
            import attempt
            val1 = 3
            val2 = 60
            self.assertEqual(attempt.ratio(val1,val2), (val1/(val2/20)))

    def test_output(self):
        """ Correct output is printed for stage I """
        user_input = ["3", "61"]
        expected = "The chance of receiving a true positive and negative result from the FOBT screen are 50% and 95% respectively."
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_output_2(self):
        """ Correct output is printed for stage II """
        user_input = ["3", "60"]
        expected = "The chance of receiving a true positive and negative result from the FOBT screen are 75% and 95% respectively."
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

    def test_output_3(self):
        """ Correct output is printed for stage III/IV"""
        user_input = ["10", "60"]
        expected = "e FOBT screen are 75% and 95% respectively."
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
