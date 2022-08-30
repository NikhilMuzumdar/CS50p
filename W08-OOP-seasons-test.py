import pytest
from seasons import get_date, in_words, get_delta
from datetime import datetime as dt

def test_get_date_na_1():
    with pytest.raises(SystemExit):
        get_date("2002-01-75")

def test_get_date_na_2():
    with pytest.raises(SystemExit):
        get_date("1998-Jan-12")

def test_in_words():
    assert in_words(5) == 'Five'

def test_in_words_na():
    with pytest.raises(NameError):
        in_words(kk)

if __name__ == "__main__":
    main()