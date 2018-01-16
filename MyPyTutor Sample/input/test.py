
from visitor import TutorialNodeVisitor
from analyser import CodeAnalyser

# TODO: does this problem need any static analysis? probably not.

class InputAnalyser(CodeAnalyser):
    def _analyse(self):
        pass

ANALYSER = InputAnalyser(TutorialNodeVisitor)

from cases import StudentTestCase

import random
from string import ascii_lowercase as letters


class Test1(StudentTestCase):
    DESCRIPTION = "'reap', 'pear' -> 'reappear'"
    MAIN_TEST = 'test_main'

    def test_main(self):
        def _get_results():
            _function_under_test()
        self.run_in_student_context(_get_results, input_text='reap\npear\n')
        expected = 'reappear\n'
        self.assertEqual(self.standard_output, expected)

    def test_alternate(self):
        # randomness is the best way to test
        word1 = ''.join(random.choice(letters) for i in range(5))
        word2 = ''.join(random.choice(letters) for i in range(7))
        input_text = word1 + '\n' + word2 + '\n'
        expected = word1 + word2 + '\n'

        def _get_results():
            _function_under_test()

        self.run_in_student_context(_get_results, input_text=input_text)
        self.assertEqual(self.standard_output, expected)


class Test2(StudentTestCase):
    DESCRIPTION = "'Cat', 'Dog' -> 'CatDog'"
    MAIN_TEST = 'test_main'

    def test_main(self):
        def _get_results():
            _function_under_test()
        self.run_in_student_context(_get_results, input_text='Cat\nDog\n')
        expected = 'CatDog\n'
        self.assertEqual(self.standard_output, expected)

    def test_alternate(self):
        def _get_results():
            _function_under_test()
        self.run_in_student_context(_get_results, input_text='Bumble\nBee\n')
        expected = 'BumbleBee\n'
        self.assertEqual(self.standard_output, expected)


class Test3(StudentTestCase):
    DESCRIPTION = "'a', '' -> 'a'"
    MAIN_TEST = 'test_main'

    def test_main(self):
        def _get_results():
            _function_under_test()
        self.run_in_student_context(_get_results, input_text='a\n\n')
        expected = 'a\n'
        self.assertEqual(self.standard_output, expected)

    def test_alternate(self):
        def _get_results():
            _function_under_test()
        self.run_in_student_context(_get_results, input_text='\nb\n')
        expected = 'b\n'
        self.assertEqual(self.standard_output, expected)


TEST_CLASSES = [
    Test1,
    Test2,
    Test3
]
## GENERATED TEST CODE
from tester import TutorialTester
from results import TutorialTestResult
from inspect import getmembers, isclass
from sys import modules, exit
from os import getcwd, path, devnull
from json import dumps
from contextlib import redirect_stdout

def generate_test_result(test_result):
    return {
        "name": test_result.description,
        "correct": test_result.status == TutorialTestResult.PASS,
        "output": test_result.message
    }

attempt_file = path.join(path.dirname(__file__), "attempt.py")

with open(attempt_file, "r") as script:
    # Where do we get the locals from?
    t = TutorialTester(TEST_CLASSES, {})
    # True will wrap the tests
    with redirect_stdout(devnull):
        t.run(script.read(), True)

    json_results = []

    failed = False
    for result in t.results:
        if result.status != "PASS":
            failed = True
        json_results.append(generate_test_result(result))

    print(dumps(json_results))

    if failed:
        exit(1)
