grocery_list = {}
while True:
    try:
        name = input()

    except EOFError:
        break

    if not name.upper() in grocery_list.keys():
        grocery_list[name.upper()] = 1
    else:
        grocery_list[name.upper()] += 1

for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item}")