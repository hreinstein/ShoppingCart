#shop_test.py 
import pytest
from app.shop import to_usd, tax_rate, find_product


def test_to_usd():
    # apply USD formatting
    assert to_usd(22.22) == "$22.22"

    # display 2 decimal places
    assert to_usd(22.2) == "$22.20"

    # round to two decimal places 
    assert to_usd(22.5555555) == "$22.56"

    # display thousands seperators
    assert to_usd(1234567890.2222222222222222) == "$1,234,567,890.22"


def test_tax_rate():
    assert(tax_rate) == 0.0875



def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)