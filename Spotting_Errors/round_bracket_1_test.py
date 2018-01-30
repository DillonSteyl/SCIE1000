from python_test_case import PythonTestCase, run_tests
from contextlib import redirect_stdout
from os import devnull
import unittest

#output handling
import io
from unittest.mock import patch

f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):

    def test_run_i(self):
        """ check you are running the loop for the correct number of times """
        
        self.assertEqual(attempt.i, 5)

    def test_elements_array(self):
        """ check the numbers in the array are correct (each element of my_array should equal the array index plus 1, times 7) """

        #check final array value

        self.assertEqual(attempt.my_array[0], 7)
        self.assertEqual(attempt.my_array[1], 14)
        self.assertEqual(attempt.my_array[2], 21)
        self.assertEqual(attempt.my_array[3], 28)
        self.assertEqual(attempt.my_array[4], 35)

        
# Run the unit tests
if __name__ == "__main__":
        try:
            run_tests(Tests)
        except TypeError:
            print("SyntaxError- invalid syntax")
        except SyntaxError:
            print("SyntaxError- invalid syntax")
