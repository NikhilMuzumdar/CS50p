from datetime import datetime, date
import sys
import inflect

def main():
    dob = get_date(input("Date of Birth: "))
    delta = get_delta(dob)
    minutes = in_words(delta*24*60)
    print(minutes, "minutes")

def get_delta(dob):
    today = date.today()
    dob = date(dob.year, dob.month, dob.day)
    delta = today - dob
    return int(delta.days)

def get_date(dob):
    try:
        time = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid Date")
    return time

def in_words(time_delta):
    p = inflect.engine()
    return p.number_to_words(time_delta, andword="").capitalize()

if __name__ == "__main__":
    main()