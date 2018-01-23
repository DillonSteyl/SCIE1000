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
                        
        def test_quad_formula_defined(self):
                """ Function 'quad_formula_pos' is correctly defined """
                with patch("builtins.input", return_value="1") as input_call:
                        import attempt
                        self.assertMethodDefined(attempt, "quad_formula_pos", 3)
                        
        def test_output(self):
                """ Correct value for x is calculated and printed """
                user_input = ["1", "2", "1"]
                expected = "The solution for x is -1.0"
                with patch("builtins.input", side_effect=user_input) as input_call:
                        with patch("sys.stdout", new=StringIO()) as output:
                                import attempt
                                self.assertEqual(attempt.quad_pos, -1.0)
                                self.assertEqual(output.getvalue().strip(), expected)


# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError- invalid syntax")
        except SyntaxError:
            print("SyntaxError- invalid syntax")
