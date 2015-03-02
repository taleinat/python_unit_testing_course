import sys

from unittest import defaultTestLoader, TestResult

from test_helper import failed, passed, import_file


def abort_tests(message="Critical failure; aborting tests."):
    print(message)
    sys.exit(0)


def reload_module(module):
    # if sys.version_info < (3,):
    #     reload(module)
    # else:
    #     import importlib
    #     importlib.reload(module)
    del sys.modules[module.__name__]
    return module.__loader__.load_module(module.__name__)


def run_module_tests(module):
    test_suite = defaultTestLoader.loadTestsFromModule(module)
    test_result = TestResult()
    test_suite.run(test_result)
    return test_result


def check_tests_pass(module, error_text="Some tests failed! Fix your code..."):
    test_result = run_module_tests(module)

    if test_result.wasSuccessful():
        passed()
    else:
        failed(error_text)


def check_tests_fail(module, error_text="All tests passed on a bad implementation! Improve your tests..."):
    test_result = run_module_tests(module)

    if test_result.wasSuccessful():
        failed(error_text)
    else:
        passed()
