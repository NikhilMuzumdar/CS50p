import sys, csv
from pyfiglet import Figlet
import random

uargs = sys.argv

# with open("fonts.csv", mode="r") as file:
#     data = csv.reader(file)
#     for lines in data:
#         fonts.append(lines[0])

fonts = ['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block', 'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer', 'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy', 'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 'weird']

if len(uargs) == 3:
    if uargs[1] in ["-f", "-font"]:
        if uargs[2] in fonts:
            font = uargs[2]
            text = input("Input: ")
            f = Figlet(font=font)
            print(f.renderText(text))
        else:
            sys.exit("Invalid usage!")
    else:
        sys.exit("Invalid Command")

elif len(uargs) == 1:
    font = random.choice(fonts)
    text = input("Input: ")
    f = Figlet(font=font)
    print(f.renderText(text))

else:
    sys.exit("Invalid Usage")

