from fuel import convert, gauge
import pytest

# Test guage function
def test_guage_full_99():
    assert gauge(99) == "F"

def test_guage_full_100():
    assert gauge(100) == "F"

def test_guage_empty_0():
    assert gauge(0) == "E"

def test_guage_empty_1():
    assert gauge(1) == "E"

def test_guage_half():
    assert gauge(50) == "50%"


# test convert function
def test_convert_normal_v1():
    assert convert("1 / 2") == 50

def test_convert_normal_v2():
    assert convert("1/4") == 25

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("3/2")

if __name__ == "__main__":
    main()