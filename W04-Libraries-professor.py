import random


def main():
    score = 0
    chances = 3
    problems = problem_generator()
    for question in problems:
        for _ in range(chances):
            try:
                answer = input(f'{question} :').upper()
                if answer == problems[question]:
                    score += 1
                    break
                else:
                    if _ == 2:
                        print(f'{question} :{problems[question]}')
                    else:
                        print("EEE")

            except ValueError:
                pass

    print(f"Score: {score}")

    return 0

def problem_generator():
    level = get_level()
    problems = {}
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x+y

        key  = str(x).upper() + " + " + str(y).upper() + " ="
        value = str(z).upper()
        problems[key] = value

    return problems


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level Cannot Exceed 3")


if __name__ == "__main__":
    main()
