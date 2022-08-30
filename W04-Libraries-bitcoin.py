import requests, sys

def main():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()
    usd_rate = float(data['bpi']['USD']['rate'].replace(",",""))

    if len(sys.argv) == 2:
        try:
            qty = float(sys.argv[1])
            print(f"${qty*usd_rate:,.4f}")
            return
        except ValueError:
            sys.exit("Command-line argument is not a number")

    else:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()