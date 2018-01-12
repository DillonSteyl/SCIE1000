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

class InheritanceTests(PythonTestCase):

    def test_out(self):
        s = f.getvalue()
        self.assertEqual("I like python yaa!\n", s)

    def test_worker_defined(self):
        """ Tests that the Worker class is defined """
        self.assertClassDefined(attempt, "Worker")

    def test_worker_inheritance(self):
        """ Checks that worker inherits from employee """
        self.assertIsSubclass(attempt.Worker, attempt.Employee)

    def test_worker_init(self):
        """ Checks that the init method for worker is correct """

        self.assertMethodDefined(attempt.Worker, "__init__", 4)

        boss = attempt.Employee("Mr. Burns", 1000000)
        worker = attempt.Worker("Waylon Smithers", 2500, boss)

    def test_worker_get_manager(self):
        """ Tests the get_manager method """
        self.assertMethodDefined(attempt.Worker, "get_manager", 1)

        boss = attempt.Employee("Mr. Burns", 1000000)
        worker = attempt.Worker("Waylon Smithers", 2500, boss)

        self.assertEqual(worker.get_manager(), boss)

    def test_executive_defined(self):
        """ Tests that the Executive class is defined """
        self.assertClassDefined(attempt, "Executive")

    def test_executive_inheritance(self):
        """ Tests that the Executive inherits from Employee """
        self.assertIsSubclass(attempt.Executive, attempt.Employee)

    def test_executive_init(self):
        """ Tests that the Executive has a correct __init__ method """
        self.assertMethodDefined(attempt.Executive, "__init__", 4)

        executive = attempt.Executive("Joseph Bloggs", 25000, 10000)

    @patch("attempt.Employee.wage")
    def test_executive_wage(self, emp_wage):
        """ Test that the Executive's wage function is correct """

        emp_wage.return_value = 25000/26

        executive = attempt.Executive("Joseph Bloggs", 25000, 10000)

        expected_wage = 25000/26 + 10000/26

        self.assertEqual(executive.wage(), expected_wage)
        self.assertCalled(emp_wage, "super().wage()")

if __name__ == "__main__":
    run_tests(InheritanceTests)
