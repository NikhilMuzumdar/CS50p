import sys, os

def main():
    file  = get_file_name()
    count = 0

    if file != None:
        with open(file, mode="r") as content:
            for line in content.readlines():
                if len(line.strip()) != 0 and line.lstrip()[0] != "#":
                    count += 1
    print(count)

def get_file_name():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1][-3:] != '.py':
        sys.exit("Not a pyhton file")

    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")

    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()