"""
test implementation of is_valid
"""

from plates import is_valid

def test_beginning_alphabetical():
    assert is_valid("AA") == True

def test_length():
    assert is_valid(" 2") == False
    assert is_valid("2") == False
    assert is_valid("a") == False

def test_number_placement():
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("A2") == False
    assert is_valid("A22") == False
    assert is_valid("A2A") == False
    assert is_valid("2AA") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_zero_placement():
    assert is_valid("A0") == False
    assert is_valid("0A") == False
    assert is_valid("00") == False
    assert is_valid("AA0") == False

def test_alphanumeric_characters():
    assert is_valid("AA 2") == False
    assert is_valid("AA.2") == False
    assert is_valid("AA2.") == False
