from working import convert
import sys
import pytest

def main():
    test_convert_valid_1()
    test_convert_valid_2()
    test_convert_valid_3()
    test_convert_valid_4()

    test_convert_invalid_5()
    test_convert_invalid_6()
    test_convert_invalid_7()
    test_convert_invalid_8()
    test_convert_invalid_9()

    sys.exit()


def test_convert_valid_1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_convert_valid_2():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_convert_valid_3():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'

def test_convert_valid_4():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_convert_invalid_5():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_convert_invalid_6():
    with pytest.raises(ValueError):
        convert('9AM - 5 PM')

def test_convert_invalid_7():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

def test_convert_invalid_8():
    with pytest.raises(ValueError):
        convert('')

def test_convert_invalid_9():
    with pytest.raises(ValueError):
        convert('1 PM to 0 AM')


if __name__ == "__main__":
    main()