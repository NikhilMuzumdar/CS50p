import pytest
from um import count

def test_um_01():
    assert count("um") == 1

def test_um_02():
    assert count(" um ") == 1

def test_um_03():
    assert count("album") == 0

def test_um_04():
    assert count("instrument") == 0

def test_um_05():
    assert count("..um..") == 1

def test_um_06():
    assert count("Um, This is the uM Way") == 2

if __name__ == "__main__":
    main()