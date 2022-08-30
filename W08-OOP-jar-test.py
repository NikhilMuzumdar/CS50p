import pytest
from jar import Jar

def test_init_valid():

    # Initiate the Jar with capacity 15
    myjar = Jar(15)
    # Add 11 cookies
    myjar.size = 11

    # Test capacity and size values
    assert myjar.capacity == 15
    assert myjar.size == 11

    # Deposit 4 cookies and check if the new balance is 15
    myjar.deposit(4)
    assert myjar.size == 15

    # Withdraw 5 cookies and check if the new balance is 10
    myjar.withdraw(5)
    assert myjar.size == 10

def test_init_invalid():
    # Initiate jar with capacity 15
    yjar = Jar(15)
    yjar.size = 7

    # Check if invalied size raises value error
    with pytest.raises(ValueError):
        yjar.size = 20

    with pytest.raises(ValueError):
        yjar.withdraw(20)

    with pytest.raises(ValueError):
        yjar.deposit(17)

def test_str():
    sjar = Jar(10)
    sjar.deposit(5)
    assert str(sjar) == "🍪🍪🍪🍪🍪"

def test_init_negative():
    with pytest.raises(ValueError):
        Jar(-1)