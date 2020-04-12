# shop.py

from pprint import pprint
from datetime import datetime


# functions for price and date/time to be used in script
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes. 
    
    Param: my_price (int or float) like 20.2222

    Example: to usd(20.2222)
    Returns: $20.22
    """
    return f"${my_price:,.2f}"

def human_friendly(my_datetime):
    """
    Converts a date time object into a human-friendly string
    Param: my_datetime (datetime.datetime object)
    """
    formatted_datestring = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Checkout at: {formatted_datestring}"


# define variables to be used in script
total_price = 0
id_inputs = []
tax = 0.0875 #NY City sales tax rate from: https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#info inputs

print("Welcome to Dreyger's Market")

valid_inputs = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

if __name__ == "__main__":
    while True:
        id_input = input("Please input a product identifier, or 'DONE' if there are no more items: ") #this is for a string or word "DONE"
        if id_input == "DONE":
            break
        elif id_input in valid_inputs:
            id_inputs.append(id_input)
        else: 
            print("Please enter a valid product ID")

#-------------------------------------------------------------------------------------------------------------------------------------------

#Print Reciept 

reciept = ""

for id_input in id_inputs:
     matching_products = [p for p in products if str(p["id"]) == str(id_input)] #need to compare values of like data types
     matching_product = matching_products[0]
     total_price = total_price + matching_product["price"] 
     reciept += matching_product["name"] + "   " + to_usd(matching_product["price"])

reciept += "\n----------------------------------------"
reciept += "\nDREYGER'S MARKET"
reciept += "\n----------------------------------------"
reciept += "\nWEBSITE: www.dreygersmarket.com"
reciept += "\nPHONE NUMBER: 713-832-4740"
if __name__ == "__main__":
    reciept += "\n" + human_friendly(datetime.now()) 
reciept += "\n----------------------------------------"
reciept += "\nSELECTED ITEMS: "
reciept += "\n----------------------------------------"
reciept += f"\nSUBTOTAL: {to_usd(total_price)}"
reciept += f"\nSALES TAX: {to_usd(total_price * tax)}" 
reciept += f"\nTOTAL: {to_usd(total_price + (total_price * tax))}"
reciept += "\n----------------------------------------"
reciept += "\nThank you for doing business with us! Please come again soon."
reciept += "\n----------------------------------------"

print(reciept)
