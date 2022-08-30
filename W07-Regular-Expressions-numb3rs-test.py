from numb3rs import validate

# Test valid ip
def test_validate_valid():
    assert validate("127.0.0.1") == True

# Invalid ip with number > 255
def test_validate_limit_breach():
    assert validate("127.0.0.775") == False

# Contains small Alphabets
def test_validate_alpha():
    assert validate("127.a.0.775") == False

# Contains caps Alphabets
def test_validate_Alpha():
    assert validate("127.A.0.775") == False

# Contains symbols
def test_validate_symbols():
    assert validate("127.#.0.775") == False

# Contains no dots
def test_validate_limit_dot_error():
    assert validate("127,168,0,775") == False

# Contains a blank string
def test_validate_limit_blank():
    assert validate("") == False


if __name__ == "__main__":
    main()