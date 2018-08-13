
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
		""" Input: Mercury. Expected Output: 18 13, Excellent choice! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "18 13\nExcellent choice!"
			self.assertEqual(output.getvalue().strip(), expected)
  
  
  def test_venus_out(self):
		""" Input: Venus. Expected Output: 18 13 5, Excellent choice! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "18 13 5\nExcellent choice!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_earth_out(self):
		""" Input: Earth. Expected Output: 13 5 25, A popular destination! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "13 5 25\nA popular destination!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_mars_out(self):
		""" Input: Mercury. Expected Output: 5 25 20, Excellent choice! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "5 25 20\nExcellent choice!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_jupiter_out(self):
		""" Input: Jupiter. Expected Output: 25 20 17, Excelent choice! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "25 20 17\nExcellent choice!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_saturn_out(self):
		""" Input: Saturn. Output: 20 17 8, Excellent choice! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "20 17 8\nExcellent choice!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_uranus_out(self):
		""" Input: Uranus. Output: 17 8 7, A popular destination! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "17 8 7\nA popular destination!"
			self.assertEqual(output.getvalue().strip(), expected)
      
  def test_neptune_out(self):
		""" Input: Neptune. Output: 8 7, A popular destination! """
		with patch("sys.stdout", new=StringIO()) as output:
			import attempt
			expected = "8 7\nA popular destination!"
			self.assertEqual(output.getvalue().strip(), expected)
	
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
