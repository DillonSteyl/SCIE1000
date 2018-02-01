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
                        
        def test_dilation_function_defined(self):
                """ Function 'time_dilation' is correctly defined """
                with patch("builtins.input", return_value="1") as input_call:
                        import attempt
                        self.assertMethodDefined(attempt, "time_dilation", 2)
                        
        def test_output_case1(self):
                """ Correct time dilation when velocty < speed of light """
                user_input = ["1", "10"]
                expected = "The time dilation is 1.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """Correct time dilation when velocty = speed of light  """
                user_input = ["1", "299792458"]
                expected = "The time dilation is 0.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)


# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError- Variable not defined")
        except SyntaxError:
            print("SyntaxError- Variable not defined")
