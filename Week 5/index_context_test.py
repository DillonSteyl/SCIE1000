
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
		

	def test_mercury_out(self):
		""" Input: Mercury (0). Expected Output: 18 13, Excellent choice! """
		user_input = "0"
		expected = "18 13\nExcellent choice!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
	
	def test_venus_out(self):
		""" Input: Venus (1). Expected Output: 18 13 5, Excellent choice! """
		user_input = "1"
		expected = "18 13 5\nExcellent choice!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
      
	def test_earth_out(self):
		""" Input: Earth (2). Expected Output: 13 5 25, A popular destination! """
		user_input = "2"
		expected = "13 5 25\nA popular destination!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

	def test_mars_out(self):
		""" Input: Mars (3). Expected Output: 5 25 20, Excellent choice! """
		user_input = "3"
		expected = "5 25 20\nExcellent choice!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
      
	def test_jupiter_out(self):
		""" Input: Jupiter (4). Expected Output: 25 20 17, Excellent choice! """
		user_input = "4"
		expected = "25 20 17\nExcellent choice!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
      
	def test_saturn_out(self):
		""" Input: Saturn (5). Output: 20 17 8, Excellent choice! """
		user_input = "5"
		expected = "20 17 8\nExcellent choice!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
      
	def test_uranus_out(self):
		""" Input: Uranus (6). Output: 17 8 7, A popular destination! """
		user_input = "6"
		expected = "17 8 7\nA popular destination!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)

	def test_neptune_out(self):
		""" Input: Neptune (7). Output: 8 7, A popular destination! """
		user_input = "7"
		expected = "8 7\nA popular destination!"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(output.getvalue().strip(), expected)
				
	def test_mercury_costs(self):
		""" Input: Mercury (0). Costs array updated to [20, 13, 5, 25, 20, 17, 8, 7]"""		
		user_input = "0"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [20, 13, 5, 25, 20, 17, 8, 7])
		
	def test_venus_costs(self):
		""" Input: Venus (1). Costs array updated to [18, 15, 5, 25, 20, 17, 8, 7]"""		
		user_input = "1"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 15, 5, 25, 20, 17, 8, 7])

	def test_earth_costs(self):
		""" Input: Earth (2). Costs array updated to [18, 13, 7, 25, 20, 17, 8, 7]"""		
		user_input = "2"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 7, 25, 20, 17, 8, 7])
				
	def test_mars_costs(self):
		""" Input: Mars (3). Costs array updated to [18, 13, 5, 27, 20, 17, 8, 7]"""		
		user_input = "3"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 5, 27, 20, 17, 8, 7])
				
	def test_jupiter_costs(self):
		""" Input: Jupiter (4). Costs array updated to [18, 13, 5, 25, 22, 17, 8, 7]"""		
		user_input = "4"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 5, 25, 22, 17, 8, 7])
				
	def test_Saturn_costs(self):
		""" Input: Saturn (5). Costs array updated to [18, 13, 5, 25, 20, 19, 8, 7]"""		
		user_input = "5"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 5, 25, 20, 19, 8, 7])
				
	def test_uranus_costs(self):
		""" Input: Uranus (6). Costs array updated to [18, 13, 5, 25, 20, 17, 10, 7]"""		
		user_input = "6"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 5, 25, 20, 17, 10, 7])
				
	def test_neptune_costs(self):
		""" Input: Neptune (7). Costs array updated to [18, 13, 5, 25, 20, 17, 8, 9]"""		
		user_input = "7"
		with patch("builtins.input", return_value=user_input) as input_call:
			with patch("sys.stdout", new=StringIO()) as output:
				import attempt
				self.assertEqual(attempt.costs.tolist(), [18, 13, 5, 25, 20, 17, 8, 9])

	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
