"""
three functions that collectively test implementation of value
"""

from bank import value

def test_greeting_start_with_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, David") == 0
    assert value("hello, world") == 0
    assert value("hello, 100.") == 0
    assert value("hEllO, #100") == 0

def test_greeting_start_with_h():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20
    assert value("Hey, David") == 20
    assert value("hey, world") == 20
    assert value("hey, 100.") == 20
    assert value("hEY, #100") == 20

def test_greeting_start_otherwise():
    assert value("goodmorning") == 100
    assert value("100") == 100
    assert value("see, you") == 100
    assert value("goodmorning , hello") == 100
    assert value("goodnight, hey") == 100
    assert value("The sun is shining") == 100
    assert value("What's up") == 100
