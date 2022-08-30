def main():
    time = input("What time is it?: ").strip()
    t = convert(time)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    hrs = int(time.split(":")[0])
    min = float(time.split(":")[-1])/60
    return hrs + min

if __name__ == "__main__":
    main()