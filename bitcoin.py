"""
Expects the user to specify as a command-line argument the number of Bitcoins,
, that they would like to buy. If that argument cannot be converted to a float,
the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions,
"""

import requests
import sys
import json

try:
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
         if not sys.argv[1].isalpha():
              response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
              #print (json.dumps(response, indent = 2))
              one_bitcoin = float(response["bpi"]["USD"]["rate_float"])
              bitcoin = '{:,}'.format(one_bitcoin * float(sys.argv[1]))
              print(f"${bitcoin}")
         else:
              sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Much command-line argument")
except requests.RequestException:
    sys.exit("Error")
except ValueError:
    sys.exit("Error")
except KeyError:
    sys.exit("Error")
