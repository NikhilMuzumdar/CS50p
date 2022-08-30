from validator_collection import validators, checkers, errors

def main():
    email = input("What's your email address? ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    try:
        validators.email(email)
        return True

    except errors.EmptyValueError:
        return False

    except errors.InvalidEmailError:
        return False

if __name__ == "__main__":
    main()