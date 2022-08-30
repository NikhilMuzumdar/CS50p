import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #Check if the first 2 characters are letters
    for l in s[:2]:
        if l.lower() in string.ascii_lowercase:
            pass
        else:
            return False

    # Check length of characters
    if not 2 <= len(s) <= 6:
        return False

    # Check if the number does not start with 0
    if is_digit_valid(s):
        return True


def is_digit_valid(n):
    (digits, letters) = ("", "")

    # IF there are letters after numbers, return False
    # To keep a check, if the letter condition is entered when digit_loc is 1, the function returns false
    digit_loc = 0

    for l in n:
        if l.isdigit():
            digits += l
            digit_loc = 1
        else:
            if digit_loc == 1:
                return False
            else:
                letters += l

    if len(digits) > 0:
        if digits[0] == "0":
            return False

    return True

main()