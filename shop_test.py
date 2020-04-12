#shop_test.py 

from shop import to_usd

my_number = 22.2222

def test_to_usd():
    result = to_usd(my_number)
    assert result == f"${my_number:,.2f}"

print(to_usd(my_number))
