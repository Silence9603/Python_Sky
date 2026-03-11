import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello world", "Hello world"),
        ('sKYPRO', 'SKYPRO'),
        ('HELL', 'HELL'),
        (" my lord", ' My lord'),
        ("!helloo", '!Helloo'),
        ('123a', '123A')
    ]
)
def test_capitalize_positive(input_text, expected_output):
    test1 = StringUtils()
    assert test1.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        (' ', ' ')
    ]
)
def test_capitalize_negative(input_text, expected_output):
    test1 = StringUtils()
    assert test1.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" world", "world"),
        ('   skypro', 'skypro'),
        ('      0     1', '0     1'),
        ('  WOODO', 'WOODO'),
        (' ', ''),
        ('test', 'test'),
        ('          "   Спасибо!"', '"   Спасибо!"'),
        ('\tboo', '\tboo'),
        ('\ntoo', '\ntoo')
    ]
)
def test_trim_positive(input_text, expected_output):
    test2 = StringUtils()
    assert test2.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_string, input_symbol, expected_output",
    [
        ("hello world", "l", True),
        ('sKYPRO', 'O', True),
        ('      ', ' ', True),
        (" my lord", 'p', False),
        ("hello world", "L", False),
        ('Hey!', '!', True)
    ]
)
def test_contains_positive(input_string, input_symbol, expected_output):
    test3 = StringUtils()
    assert test3.contains(input_string, input_symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, input_symbol, expected_output",
    [
        ("hello world", "ll", True),
        ("hello world", "e, o", False),
        ("hello world", "o w", True)
    ]
)
def test_contains_negative(input_string, input_symbol, expected_output):
    test3 = StringUtils()
    assert test3.contains(input_string, input_symbol) == expected_output


@pytest.mark.parametrize(
    "input_string, delete_symbol, expected_output",
    [
        ("hello world", "l", 'heo word'),
        ('sKYPRO', 'O', 'sKYPR'),
        ('      ', ' ', ''),
        (' my lord', 'p', ' my lord'),
        ("hello world", "L", 'hello world'),
        ('opa-opa-opa', 'opa', '--'),
        ('Mom', 'non', 'Mom'),
        ('MOM', 'mom', 'MOM')
    ]
)
def test_delete_symbol_positive(input_string, delete_symbol, expected_output):
    test4 = StringUtils()
    assert test4.delete_symbol(input_string, delete_symbol) == expected_output
