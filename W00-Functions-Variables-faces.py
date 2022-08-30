def main():
    user_input = input("Enter the desired string :")
    print(f"{convert(user_input)}")

def convert(string):
    string = string.replace(":)","🙂")
    string = string.replace(":(","🙁")
    return string

main()