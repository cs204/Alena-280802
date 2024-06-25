import pytest
from jar import Jar

def test_create_jar_with_valid_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_create_jar_with_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar(3.14)

def test_deposit_cookies():
    jar = Jar(10)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    assert jar.size == 5

def test_deposit_exceeding_capacity():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw_cookies():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪"
    assert jar.size == 4

def test_withdraw_more_than_available():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)
