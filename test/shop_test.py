#shop_test.py 

from app.shop import to_usd, tax_rate, human_friendly


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



