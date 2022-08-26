greeting = input("Say your greetings: ")
greeting = greeting.strip().split()[0].lower()

if greeting[:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")