from python_test_case import PythonTestCase
import unittest

# Handle capturing what the students print
from io import StringIO
from unittest.mock import patch

class HelloWorldTest(PythonTestCase):

    def test(self):
        with patch("sys.stdout", new=StringIO()) as output:
            # Import the module here, as the code will print as soon
            # as we import it
            import attempt
            self.assertEqual(output.getvalue().strip(), "Python is cool!")

if __name__ == "__main__":
    unittest.main()
