from twttr import shorten

def test_a(): # Tests a
    assert shorten("Mang") == "Mng"

def test_e(): # Tests e
    assert shorten("Meng") == "Mng"

def test_i(): # Tests i
    assert shorten("Ming") == "Mng"

def test_o(): # Tests o
    assert shorten("Mong") == "Mng"

def test_u(): # Tests u
    assert shorten("Mung") == "Mng"

def test_nv(): # Tests non vovel
    assert shorten("Mbng") == "Mbng"

def test_cv(): # Tests Capital Vovel
    assert shorten("MAng") == "Mng"

def test_num_v(): # Tests numbers
    assert shorten("M1ng") == "M1ng"

def test_sv(): # Tests symbol
    assert shorten("M!ng") == "M!ng"

if __name__ == "__main__":
    main()