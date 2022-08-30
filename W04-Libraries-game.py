import random

def main():
    n = get_number()
    key = random.randint(1, n+1)
    guess_number(key)

def get_number():
    while True:
        try:
            number = int(input("Level: "))
            if number > 0:
                return number
        except ValueError:
            continue

def guess_number(key):
    while True:
        try:
            number = int(input("Guess: "))
            if number == key:
                print("Just right!")
                return
            elif number > key:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            continue
        
if __name__ == "__main__":
    main()