import string

camelCase = input("camelCase: ")
snake_case = ""

upper = string.ascii_uppercase

for l in camelCase:
    if l in upper:
        snake_case += "_" + l.lower()
    else:
        snake_case += l

print(snake_case)