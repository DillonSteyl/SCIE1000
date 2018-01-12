from python_test_case import PythonTestCase, run_tests
import unittest

# Handle capturing what the students print
from io import StringIO
from unittest.mock import patch

class HelloWorldTest(PythonTestCase):

    def test(self):
        """ Should print 'Hello, World!' """
        # The above docstring is used as the description
        # of the test to the student

        with patch("sys.stdout", new=StringIO()) as output:

            # Import the module here, as the code will print as soon
            # as we import it
            import attempt
            self.assertEqual(output.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    run_tests(HelloWorldTest)
