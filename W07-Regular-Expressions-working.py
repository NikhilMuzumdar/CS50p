import re
import sys

def main():
    print(convert(input("Hours: ")))
    sys.exit()

def convert(s):
    time = useRegex(s)
    start = time.split(" to ")[0]
    end = time.split(" to ")[-1]

    try:
        p_start = process_time(start)
        p_end = process_time(end)

    except:
        raise ValueError

    return f"{p_start} to {p_end}"

def useRegex(input):
    time = re.match(r"((?:[0-9][0-2]*):*(?:[0-5][0-9])* (?:[A-P]M)) to ((?:[0-9][0-2]*):*(?:[0-5][0-9])* (?:[A-P]M))", input)
    if time:
        return time.group(0)
    else:
        raise ValueError

def process_time(time):
    if 'AM' in time:
        time = time.replace(" AM", "")
        if ":" in time:
            hr = int(time.split(":")[0])
            if hr == 0:
                raise ValueError
            else:
                hr = hr % 12
            mn = int(time.split(":")[1])
        else:
            hr = int(time)
            if hr == 0:
                raise ValueError
            else:
                hr = hr % 12
            mn = 0
    else:
        time = time.replace(" PM", "")
        if ":" in time:
            hr = int(time.split(":")[0])
            if not hr == 12:
                hr = (int(time.split(":")[0]) + 12) % 24
            mn = int(time.split(":")[1])

        else:
            hr = int(time)
            if not hr == 12:
                hr = (int(time) + 12 ) % 24
            mn = 0

    return f"{hr:02}:{mn:02}"

if __name__ == "__main__":
    main()