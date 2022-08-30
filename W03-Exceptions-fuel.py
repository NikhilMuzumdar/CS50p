def main():
    fuel = get_fraction()

    # Check if the fule is over 99%
    if fuel/100 >= 0.99:
        print("F")
    # Check if the fuel is less than 1%
    elif fuel/100 <= 0.01:
        print("E")
    else:
        print(f"{round(fuel)}%")

def get_fraction():
    while True:
        user_input = input("Fraction: ")
        try:
            numerator = int(user_input.split("/")[0])
            denominator = int(user_input.split("/")[1])
            if numerator <= denominator and denominator !=0:
                return 100 * numerator / denominator
        except ValueError:
            pass
        else:
            pass

main()