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
                        
        def test_power_function_defined(self):
                """ Function 'power' is correctly defined """
                with patch("builtins.input", return_value="1") as input_call:
                        import attempt
                        self.assertMethodDefined(attempt, "power", 2)
                        
        def test_output_case1(self):
                """ Correct answer when a = 2 and b = 10"""
                user_input = ["2", "10"]
                expected = "The answer is 1024"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(output.getvalue().strip(), expected)

        def test_output_case2(self):
                """Correct answer when a = 4 and b = 4"""
                user_input = ["4", "4"]
                expected = "The answer is 256"
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
