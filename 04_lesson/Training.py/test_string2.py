import pytest
from string_processor import StringProcessor

# Более явное указание тестовых случаев
positive_test_cases = [
    ("hello", "Hello."),
    ("Hello", "Hello."),
    ("hello world", "Hello world."),
    ("HELLO", "HELLO."),
    ("hello.", "Hello."),
]

negative_test_cases = [
    ("", "."),
    ("    ", "    ."),
    ("a", "A."),
    ("123", "123."),
]


@pytest.mark.parametrize("input_text, expected_output", positive_test_cases)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", negative_test_cases)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
