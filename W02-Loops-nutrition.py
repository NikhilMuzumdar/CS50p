# import csv

# Import Website into google sheet and generate a csv file
# Use csv reader in python to convert the required data into a dict (named database)

# database = {}
# with open("Nutrition.csv", mode="r") as file:
#     data = csv.reader(file)
#     for row in data:
#         # database[row[0].split("\n")[0]] = database[row[1].split("\n")[0]]
#         database[row[0].split("\n")[0].lower()] = row[1].split("\n")[0]

database = {
        'apple': '130',
        'avocado': '50',
        'banana': '110',
        'cantaloupe': '50',
        'grapefruit': '60',
        'grapes': '90',
        'honeydew': '50',
        'kiwifruit': '90',
        'lemon': '15',
        'lime': '20',
        'nectarine': '60',
        'orange': '80',
        'peach': '60',
        'pear': '100',
        'pineapple': '50',
        'plums': '70',
        'strawberries': '50',
        'sweet cherries': '100',
        'tangerine': '50',
        'watermelon': '80'
        }

item = input("Item: ").lower()
if item in database.keys():
    output = database[item]
    print(f"Output: {output}")

