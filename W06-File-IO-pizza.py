from tabulate import tabulate
import sys, os

def main():
    name = get_file_name()
    print_table(name)


def print_table(name):
    table = []
    with open(name, mode="r") as file:
        for line in file.readlines():
            table.append(line.rstrip().split(","))

    print(tabulate(table, headers='firstrow', tablefmt="grid"))


def get_file_name():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1][-4:] != '.csv':
        sys.exit("Not a csv file")

    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")

    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()