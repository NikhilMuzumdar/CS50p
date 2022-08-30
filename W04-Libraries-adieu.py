import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

mylist = p.join(names)
start_string = "Adieu, adieu, to "
print(start_string+mylist)
