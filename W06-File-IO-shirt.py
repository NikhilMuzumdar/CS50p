import PIL
from PIL import Image
import sys, os


def main():
    before = get_file_names()[0]
    after = get_file_names()[1]
    shirt = Image.open("shirt.png")

    man = Image.open(before)
    man = PIL.ImageOps.fit(man, (600,600))
    man.paste(shirt, mask=shirt)

    man.save(after)



def get_file_names():
    """Validates command line argument and returns name of the input image file and output image file"""
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1][-4:].lower() in ['.jpg', '.jpeg', '.png']:
        sys.exit("Input file is not an image file")

    elif not sys.argv[2][-4:].lower() in ['.jpg', '.jpeg', '.png']:
        sys.exit("Output file is not an image file")

    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")

    elif not sys.argv[1][-4:] == sys.argv[2][-4:]:
        sys.exit("Extension of input and output file has to be the same")

    else:
        return (sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()