months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_nos = list(range(1,13))
month_dict = dict(zip(months, month_nos))

while True:
    try:
        string = input("Date: ").strip()

    except EOFError:
        break

    else:
        if " " in string and "," in string:
            string = string.split(" ")
            if string[0] in months:
                year = string[-1]
                month = month_dict[string[0]]
                day = int(string[1].replace(",",""))

                if day > 31:
                    continue
                else:
                    date = year + "-" + f"{month:02d}" + "-" + f'{day:02d}'
                    print(date)
                    break

        elif "/" in string and len(string.split("/")[0]) < 3:
            string = string.split("/")
            year = string[-1]
            month = int(string[0])
            day = int(string[1])

            if month > 12 or day > 31:
                continue

            else:
                date = year + "-" + f'{month:02d}' + "-" + f"{day:02d}"
                print(date)
                break