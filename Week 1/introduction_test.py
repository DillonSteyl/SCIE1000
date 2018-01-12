from python_test_case import PythonTestCase, run_tests
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from os import devnull
import io

##with open(devnull, "w") as f:
##    with redirect_stdout(f):
##        # Redirect the stdout in case the student has global print statements
##        import attempt
f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):

	def test_output(self):
		""" Ensure the line 'SCIE1000 will be great!' is printed """
		out = f.getvalue()
		self.assertEqual("Hello World!\nPython is pretty sweet.\nSCIE1000 will be great!\n", out)

if __name__ == "__main__":
    run_tests(Tests)
