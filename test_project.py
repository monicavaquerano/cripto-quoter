import app
from project import (
    unit_number,
    get_name,
    get_symbol,
    get_current_price,
    get_value,
    get_last_update,
)


def main():
    test_connection()
    test_unit_number()
    test_get_symbol()
    test_get_name()
    test_get_current_price()
    test_get_value()
    test_get_last_update()


# app.py with the connection string function
def test_connection(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "symbol", "btc")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "name", "Bitcoin")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "usd", "24012")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "last_updated", "2023-03-13T17:08:08.125Z")

    # expected result based on the mocks
    expected = "Symbol = btc; Name = Bitcoin; Current price = 24012; last_update: 2023-03-13T17:08:08.125Z"

    # the test uses the monkeypatched dictionary settings
    result = app.create_connection_string()

    assert result == expected


def test_unit_number():
    assert unit_number(1) == 1.0
    assert unit_number(-5) == False
    assert unit_number("a") == False


def test_get_name(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "name", "Bitcoin")

    # expected result based on the mocks
    expected = "Bitcoin"

    # the test uses the monkeypatched dictionary settings
    result = get_name(app.DEFAULT_CONFIG)

    assert result == expected


def test_get_symbol(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "name", "btc")

    # expected result based on the mocks
    expected = "BTC"

    # the test uses the monkeypatched dictionary settings
    result = get_symbol(app.DEFAULT_CONFIG)

    assert result == expected


def test_get_current_price(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "usd", 24012)

    # expected result based on the mocks
    expected = "$24012.0000 USD"

    # the test uses the monkeypatched dictionary settings
    result = get_current_price(app.DEFAULT_CONFIG)

    assert result == expected


def test_get_value(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "usd", 24012)

    # expected result based on the mocks
    expected = "$48024.0000 USD"

    # the test uses the monkeypatched dictionary settings
    result = get_value(app.DEFAULT_CONFIG, 2)

    assert result == expected


def test_get_last_update(monkeypatch):
    # testing values only for this test.
    monkeypatch.setitem(app.DEFAULT_CONFIG, "last_updated", "2023-03-13T17:08:08.125Z")

    # expected result based on the mocks
    expected = "2023-03-13T17:08:08.125Z"

    # the test uses the monkeypatched dictionary settings
    result = get_last_update(app.DEFAULT_CONFIG)

    assert result == expected


if __name__ == "__main__":
    main()
