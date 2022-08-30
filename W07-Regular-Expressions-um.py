import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    data = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    # \b -> r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
    return len(data)


if __name__ == "__main__":
    main()