import unittest
import unittest.mock

from custom_test_helpers import inspect_assertions, run_test_case_tests
from test_helper import run_common_tests, test_answer_placeholders_text_deleted, import_task_file, passed, failed, \
    get_answer_placeholders


def check_integer_truthiness_tests():
    task_module = import_task_file()
    TestIntegerTruthiness = inspect_assertions(task_module.TestIntegerTruthiness)
    test_result = run_test_case_tests(TestIntegerTruthiness)

    if not test_result.wasSuccessful():
        failed("Some of the TestIntegerTruthiness tests failed!")

    placeholder_windows = get_answer_placeholders()[0:3]
    test_zero_window, test_one_window, test_other_value_window = placeholder_windows

    # check test_zero
    if TestIntegerTruthiness.get_test_method_total_call_count("test_zero") > 1:
        failed(name="TestIntegerTruthiness.test_zero", message="must use only one assertion")
    elif TestIntegerTruthiness.get_test_method_total_call_count("test_zero") == 0:
        failed(name="TestIntegerTruthiness.test_zero", message="must use an assertion")
    elif unittest.mock.call(0) in TestIntegerTruthiness.per_method_counters["test_zero"]["assertFalse"].call_args_list:
        passed(name="TestIntegerTruthiness.test_zero")
    else:
        failed(name="TestIntegerTruthiness.test_zero")

    # check test_one
    if TestIntegerTruthiness.get_test_method_total_call_count("test_one") > 1:
        failed(name="TestIntegerTruthiness.test_one", message="must use only one assertion")
    elif TestIntegerTruthiness.get_test_method_total_call_count("test_one") == 0:
        failed(name="TestIntegerTruthiness.test_one", message="must use an assertion")
    elif unittest.mock.call(1) in TestIntegerTruthiness.per_method_counters["test_one"]["assertTrue"].call_args_list:
        passed(name="TestIntegerTruthiness.test_one")
    else:
        failed(name="TestIntegerTruthiness.test_one")

    # check test_other_value
    wrapped_assertTrue = TestIntegerTruthiness.per_method_counters["test_other_value"]["assertTrue"]
    if TestIntegerTruthiness.get_test_method_total_call_count("test_other_value") > 1:
        failed(name="TestIntegerTruthiness.test_other_value", message="must use only one assertion")
    elif TestIntegerTruthiness.get_test_method_total_call_count("test_other_value") == 0:
        failed(name="TestIntegerTruthiness.test_other_value", message="must use an assertion")
    elif (
            "self.assertTrue" in test_other_value_window and
            wrapped_assertTrue.call_count > 0 and
            isinstance(wrapped_assertTrue.call_args[0][0], int) and
            wrapped_assertTrue.call_args[0][0] not in {0, 1}
    ):
        passed(name="TestIntegerTruthiness.test_other_value")
    else:
        failed(name="TestIntegerTruthiness.test_other_value")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    check_integer_truthiness_tests()
