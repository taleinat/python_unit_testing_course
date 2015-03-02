from custom_test_helpers import check_tests_pass, import_answers_module
from test_helper import run_common_tests, test_answer_placeholders_text_deleted


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    module = import_answers_module()
    check_tests_pass(module)
