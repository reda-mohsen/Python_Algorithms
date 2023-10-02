from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("1/1") == 100
    assert convert("0/1") == 0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/cat")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
