# test class jar

from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity ==12
    assert jar.size == 0
    jar = Jar(5)
    assert jar.capacity ==5
    assert jar.size == 0
    jar = Jar(15)
    assert jar.capacity ==15
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(-10)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    assert jar.size == 0
    jar.deposit(1)
    assert str(jar) == "🍪"
    assert jar.size == 1
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar.size == 12
    jar.withdraw(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    assert jar.size == 6

def test_deposit():
    jar = Jar(5)
    assert str(jar) == ""
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1)
    jar = Jar(10)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    assert jar.size == 0
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(2)
    assert jar.size == 6
    jar.withdraw(5)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)