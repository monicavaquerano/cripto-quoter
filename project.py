import json
import requests
import sys
from tabulate import tabulate, SEPARATING_LINE


def main():
    while True:
        """Call to API"""
        while True:
            print(
                "-------------------------------\nWelcome to CS50's Cripto Price Quoter\n-------------------------------"
            )
            obj = callAPI(input("Criptocoin Name: "))
            if obj:
                break
            else:
                print("Coin not found. Try again.")

        """ Amount be to quoted in USD"""
        while True:
            n = unit_number(input("Amount be to quoted in USD: "))
            if n:
                break
            else:
                print("Invalid value, try again.")

        """ Attributes """
        symbol = get_symbol(obj)
        name = get_name(obj)
        cp = get_current_price(obj)
        value = get_value(obj, n)
        last_update = get_last_update(obj)

        """ Table """
        header = ["CS50's Cripto Quoter", ""]
        table = [
            ["Symbol", symbol],
            ["Name", name],
            SEPARATING_LINE,
            ["Current price per unit", cp],
            [f"Price per {n} unit(s)", value],
            SEPARATING_LINE,
            ["Last updated", last_update],
            SEPARATING_LINE,
        ]
        """ Printing the table """
        print_table(table, header)

        """ Continue or quitting the program"""
        print("<--- Looking for other criptos? --->")
        while True:
            s = input("Continue 1)\nExit     2)  ")
            match s:
                case "1":
                    break
                case "2":
                    sys.exit("--- Bye! ---")
                case _:
                    print("Please enter 1 or 2")


def callAPI(cripto: str) -> dict:
    """
    Queries the Coingecko API and returns information for a particular criptocurrency.

    :param str: The name of the criptocurrency
    :type str: string
    :return: A dictionary object or False
    :rtype: dic or boolean
    """

    try:
        if cripto.isdigit():
            return False
        else:
            cripto = cripto.lower().strip()
            response = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{cripto}", timeout=30
            )
            obj = response.json()
            if "error" in obj.keys():
                return False
            else:
                return obj
    except:
        sys.exit("Request timed out, unexpected Error. Try again later.")


def unit_number(n: float) -> float:
    """
    Takes the amount of criptocurrency to be quoted and returns it as a float.

    :param n: The number of units to be quoted
    :type n: n
    :return: A float number or False
    :rtype: float or boolean
    """
    try:
        n = float(n)
        if n < 0:
            return False
        else:
            return n
    except ValueError:
        return False


def get_name(obj: dict) -> str:
    """
    Returns the value of "name" key of a dict object.

    :param dict: The name of the object
    :type dict: dict object
    :raise KeyError: If "name" key is not found
    :return: The dict "name" key value string
    :rtype: str
    """
    try:
        return obj["name"]
    except KeyError:
        return False


def get_symbol(obj: dict) -> str:
    """
    Returns the upper value of "symbol" key of a dict object.

    :param dict: The symbol of the object
    :type dict: dict object
    :raise KeyError: If "symbol" key is not found
    :return: The dict "symbol" key value string in uppercases
    :rtype: str
    """
    symbol = obj["symbol"]
    return symbol.upper()


def get_current_price(obj: dict) -> str:
    """
    Returns the dict object's current price in USD in a formatted string.

    :param dict: The current price of the object in USD
    :type dict: dict object
    :raise KeyError: If "symbol" key is not found
    :return: The dict object's current price in USD in a formatted string.
    :rtype: str
    """
    current_price = obj["market_data"]["current_price"]["usd"]
    return f"${current_price:10.4f} USD"


def get_value(obj: dict, n: float) -> str:
    """
    Returns the dict object's current price in USD multiplied by n times in a formatted string.

    :param dict, n: The current price of the object and number of units to multiply
    :type dict, float: dict object and a float
    :raise KeyError: If "current price" key is not found
    :return: the dict object's current price in USD multiplied by n times in a formatted string.
    :rtype: str
    """
    value = n * obj["market_data"]["current_price"]["usd"]
    return f"${value:10.4f} USD"


def get_last_update(obj: dict) -> str:
    """
    Returns the dict object's last updated date in a string.

    :param dict: The current price of the object
    :type dict: dict object
    :raise KeyError: If "last_updated" key is not found
    :return: the dict object's last updated date in string.
    :rtype: str
    """
    last_update = obj["last_updated"]
    return last_update


def print_table(table: list, header: list):
    """
    Prints a table with all the values inside the "table" and "header" variables.

    :param table, header: the table and header information
    :type list, list: lists
    :return: a formatted string with all the information
    :rtype: str
    """
    print("\n" + tabulate(table, header, colalign=("left", "decimal")))


if __name__ == "__main__":
    main()
