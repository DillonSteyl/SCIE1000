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
			
	def test_calls(self):
		""" Correct input messages are used """
		with patch("builtins.input", return_value="1") as input_call:
			import attempt
			input_call.assert_has_calls([call("Enter width: "), call("Enter height: ")])
			
	def test_output(self):
		""" Correct area is printed """
		user_input = ["2", "8"]
		expected = "The area of the rectangle is: 16"
		with patch("builtins.input", side_effect=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

# Run the unit tests
if __name__ == "__main__":
	run_tests(Tests)