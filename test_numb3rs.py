"""
test validate function
"""

from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("127.0.05.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("-127.2.03.14") == False
    assert validate("127.-2.512.14") == False
    assert validate("127.0.255.512") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("cat.dog.bird.bear") == False

