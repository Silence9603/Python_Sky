import pytest
from string_processor import StringProcessor
    
@pytest.mark.parametrize( 
    "input_text, expected_output", 
    [
        ("hello world", "Hello world."),
        ("Python is awesome", "Python is awesome."),
        ("already has dot.", "Already has dot."),
        ("multiple sentences. here", "Multiple sentences. here."),
        ("UPPERCASE STRING", "UPPERCASE STRING."),
        ("mixed CASE string", "Mixed CASE string.")
    ]
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
        
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("", "."),
        ("a", "A."),
        ("z", "Z."),
        ("123 test", "123 test."),
        ("!special string", "!special string."),
        ("   ", "   ."),
        (".dot at start", ".dot at start."),
        ("already has dot at end.", "Already has dot at end."),
        ("one", "One."),
        ("already has punctuation!", "Already has punctuation!.")
    ]
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

