from plates import is_valid

def test_valid_4(): # 4 digit valid plate
    assert is_valid('CS50') == True

def test_valid_an(): # 2 digit valid plate
    assert is_valid('C1') == False

def test_valid_na(): # 2 digit valid plate
    assert is_valid('7C') == False

def test_valid_6(): # 6 digit valid plate
    assert is_valid('ECTO88') == True

def test_valid_4_all_alpha(): # 6 digit valid plate with all alphabets
    assert is_valid('NRVOUS') == True

def test_valid_4_zero_start(): # Invalid plate, number starts with zero
    assert is_valid('CS05') == False

def test_valid_4_sandwich(): # Invalid plate, alphabets sandwiched in between
    assert is_valid('CS50P2') == False

def test_valid_short_plate(): # Invalid chars
    assert is_valid('H') == False

def test_valid_long_plate(): # Invalid chars
    assert is_valid('OTTATIME') == False

def test_valid_numstart(): # Starts with a number
    assert is_valid('1TTATY') == False

def test_valid_non_alphanumeric(): # Non alphanumeric
    assert is_valid('AA**@@') == False

if __name__ == "__main__":
    main()