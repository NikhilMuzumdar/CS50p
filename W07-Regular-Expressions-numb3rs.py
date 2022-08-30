import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Chek if "." exists in ip
    if not "." in ip:
        return False

    # remove the dots and check if there are nondigits in the ip
    for l in ip.replace(".",""):
        if not l.isdigit():
            return False

    # check if numbers are less than 256
    for d in ip.split("."):
        if not 0 <= int(d) <=255:
            return False

    return True


if __name__ == "__main__":
    main()