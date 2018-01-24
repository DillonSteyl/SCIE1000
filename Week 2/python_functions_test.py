from python_test_case import PythonTestCase, run_tests
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from os import devnull
from pylab import *
import io

f = io.StringIO()
with redirect_stdout(f):
    import attempt

class Tests(PythonTestCase):

	def test_output(self):
		""" All proper values must be printed, in the correct order"""
		out = f.getvalue()
		expected = str(sqrt(6)) + "\n" + str(exp(3)) + "\n" + str(sin(2)) + "\n" + str(log(5)) + "\n"
		self.assertEqual(out, expected)

if __name__ == "__main__":
    run_tests(Tests)
