import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.findall(r'(?=src)src=\"(?P<src>[^\"]+)', s)
    if match:
        emb_url = match[0]
        if "youtube" in emb_url:
            id = emb_url.split('embed/')[-1]
            start_text = 'https://youtu.be/'
            return start_text+id
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()