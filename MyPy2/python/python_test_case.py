"""
The test cases for Python 3

"""
import unittest
import sys
from json import dumps
from inspect import signature
from types import FunctionType, MethodType
from xmlrunner import XMLTestRunner
from glob import glob
from unittest.mock import patch
from os import devnull, path
from pprint import pprint
from contextlib import redirect_stdout

__author__ = "eLIPSE"

class PythonTestCase(unittest.TestCase):
    """Adds custom assertions that extend the default test case
    """

    def assertDefined(self, module, variable, var_type):
        """ Asserts that a variable is defined inside a module
        with the given type

        Raises an assertion error if it fails

        Parameters:
            module: The module or class
            variable (string): The name of the variable
            var_type (type): The type of the variable
        """

        if not hasattr(module, variable):
            raise AssertionError("'{}' is not defined correctly, check spelling".format(variable))

        var = getattr(module, variable)

        if type(var) != var_type:
            raise AssertionError("'{}' is type '{}', expected '{}'".format(variable, type(var), var_type))

    def assertClassDefined(self, module, class_name):
        """ Asserts that a class if defined by the given name

        Parameters:
            module: The module
            class_name (string): The class name
        """
        if not hasattr(module, class_name):
            raise AssertionError("class '{}' is not defined correctly, check spelling".format(class_name))

    def assertFunctionDefined(self, module, function_name, parameters):
        """ Asserts that a function is correctly defined with the correct number
        of parameters

        Parameters:
            module: The module
            function_name (string): The name of the function
            parameters (int): The number of parameters the function should take
        """

        raise NotImplementedError("use the assertMethodDefined function")
        # self.assertDefined(module, filename, FunctionType)

    def assertMethodDefined(self, class_instance, method_name, parameters):
        """ Asserts that a method (class function) is correctly defined with the correct number
        of parameters

        Parameters:
            class_instance: The class instance
            method_name (string): The name of the method
            parameters (int): The number of parameters the method should take
        """

        self.assertDefined(class_instance, method_name, FunctionType)

        sig = signature(getattr(class_instance, method_name))

        if len(sig.parameters) != parameters:
            raise AssertionError(
                    "'{}' does not have the correct number of parameters, expected {} found {}".format(
                        method_name, parameters, len(sig.parameters)
                        )
                    )

    def assertIsSubclass(self, sub_class, parent_class):
        """ Asserts that a class is a subclass of the parent class

        Parameters:
            sub_class: The subclass to check
            parent_class: The parent class
        """
        self.assertTrue(issubclass(sub_class, parent_class))

    def assertCalled(self, mock, function_name):
        """ Checks that a method was called

        Parameters:
            mock (Mock): The mocked function
            function_name (str): The name of the function, for printing of the error
        """

        self.assertTrue(mock.called, "Expected function '{}' to be called".format(function_name))

class MypyTestResult(unittest.TestResult):
    """ Inherits from TestResult, adding the json format functionality

    The json format is as follows::
        
        [{
            "name": "Name of the unit test",
            "correct": true,
            "output": "TypeError: X is not defined"
        }]

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ Sets up the test result object """

        # Stores a list of dictionary objects, which will later be converted to json
        self.tests = []

    def log_test(self, name, correct, output):
        """ Logs a test as complete or incomplete """
        self.tests.append({
            "name": name,
            "correct": correct,
            "output": output
        })

    def addSuccess(self, test):
        super().addSuccess(test)
        self.log_test(test.shortDescription(), True, "Correct")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.log_test(test.shortDescription(), False, ": ".join(err[1].args))

    def addError(self, test, err):
        super().addError(test, err)
        self.log_test(test.shortDescription(), False, ": ".join(err[1].args))

    def get_json(self):
        """ Returns the JSON result of the tests """
        return dumps(self.tests, indent=4)

def run_tests(test_case_class):
    """ Runs the unit tests """
    
    with open(devnull, 'w') as null_stream:
        with redirect_stdout(null_stream):
            # Redirect stdout
            runner = unittest.TextTestRunner(stream=null_stream, resultclass=MypyTestResult, buffer=null_stream)

            suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)

            result = runner.run(suite)


        print(result.get_json())

        if result.wasSuccessful():
            sys.exit(0)
        else:
            sys.exit(1)

