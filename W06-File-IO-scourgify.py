import sys, os
import csv

def main():
    file_name = get_file_name()[0]
    output_file_name = get_file_name()[-1]
    data_list = read_into_list(file_name)
    write_into_file(data_list, output_file_name)


def read_into_list(file_name):
    name_list = []
    with open(file_name, mode="r") as file:
        data = csv.reader(file)

        for row in data:
            first_name = row[0].split(",")[-1].lstrip()
            last_name = row[0].split(",")[0]
            house = row[-1]
            name_list.append([first_name, last_name, house])

    name_list[0] = ['first', 'last', 'house']
    return name_list

def write_into_file(data_list, output_file_name):
    with open(output_file_name, mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(data_list)

def get_file_name():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1][-4:] != '.csv':
        sys.exit("Input file is not a csv file")

    elif sys.argv[2][-4:] != '.csv':
        sys.exit("Output file is not a csv file")

    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")

    else:
        return (sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
