from bank import value

def test_hello_s():
    assert value("hello Mr So and So") == 0

def test_hello_c():
    assert value("Hello Mr So and So") == 0

def test_h_s():
    assert value("hi Mr So and So") == 20

def test_h_c():
    assert value("Hi Mr So and So") == 20

def test_other():
    assert value("This is CS50") == 100

def test_blank():
    assert value("") == 100

if __name__ == "__main__":
    main()