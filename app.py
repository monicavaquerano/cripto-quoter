# Contents of app.py to generate a simple connection string
DEFAULT_CONFIG = {
    "symbol": "btc",
    "name": "Bitcoin",
    "market_data": {"current_price": {"usd": 24012}},
    "last_updated": "2023-03-13T17:08:08.125Z",
}


def create_connection_string(config=None):
    """Creates a connection string from input or defaults."""
    config = config or DEFAULT_CONFIG
    return f"Symbol = {config['symbol']}; Name = {config['name']}; Current price = {config['market_data']['current_price']['usd']}; last_update: {config['last_updated']}"


"""
TESTING RESULT

                       CS50's Cripto Index
----------------------  ------------------------
Symbol                  BTC
Name                    Bitcoin
----------------------  ------------------------
Current price per unit  $24012.0000 USD
Price per 2.0 unit(s)   $48024.0000 USD
----------------------  ------------------------
Last updated            2023-03-13T17:08:08.125Z
----------------------  ------------------------
"""
