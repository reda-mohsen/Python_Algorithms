from seasons import convert
import pytest

def test_invalid_date():
    with pytest.raises(SystemExit):
        convert("January 1, 1999")
        convert("2000-12-40")
        convert("2000-22-10")
        convert("-5-12-04")
        convert("2000-10-9")

def test_convert():
    assert convert("2022-10-09") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-10-09") == "One million, fifty-one thousand, two hundred minutes"
    assert convert("2023-10-08") == "One thousand, four hundred forty minutes"