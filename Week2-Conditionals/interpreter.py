expression = input("Expression: ").strip().split(" ")
(x, y, z) = (float(expression[0]), expression[1], float(expression[2]))

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)
else:
    print("Invalid input!")

