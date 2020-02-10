# shop.py
from pprint import pprint
import datetime


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

total_price = 0
id_inputs = []
tax = 0.06 #tax rate info taken from: https://smartasset.com/taxes/district-of-columbia-tax-calculator

print()
print("Welcome to Dreyger's Market")
print()

while True:
    id_input = input("Please input a product identifier, or 'DONE' if there are no more items: ") #this is for a string or word "DONE"
    if id_input == "DONE":
        break
    else:
        id_inputs.append(id_input)

#--------------------------------------------------------------------
#Reciept

print()
print("----------------------------------------")
print("DREYGER'S MARKET")
print("----------------------------------------")
print("WEBSITE: www.dreygersmarket.com")
print("PHONE NUMBER: 713-832-4740")


#date and time 
today = datetime.datetime.today()
print("CHECKOUT TIME: ", today.strftime("%m/%d/%Y %I:%M %p"))
print("----------------------------------------")


#shopping cart items 
print("SELECTED ITEMS: ")
print()

for id_input in id_inputs:
     matching_products = [p for p in products if str(p["id"]) == str(id_input)] #need to compare values of like data types
     matching_product = matching_products[0]
     total_price = total_price + matching_product["price"]
     formatted_total_price = "${0:.2f}".format(matching_product["price"]) #created a variable to format the prices from the products list 
     print(matching_product["name"] + " " + "(" + formatted_total_price + ")")

print()
print("----------------------------------------")

#calculations
sales_tax = total_price * tax 
final_total = total_price + sales_tax

#subtotal
total_price = "${0:.2f}".format(total_price)
print("SUBTOTAL: ", str(total_price)) 

#sales tax 
sales_tax = "${0:.2f}".format(sales_tax)
print("SALES TAX (6.00%): ", sales_tax)

#final total  
final_total = "${0:.2f}".format(final_total)
print("TOTAL: ", str(final_total))

#thank you message 
print("----------------------------------------")
print()
print("Thank you for doing business with us! Please come again soon.")
print()
print("----------------------------------------")

#--------------------------------------------------------------------------------------------


#TODO 
# Friendly error message when ID is not in 1-20 range or any string other than 'DONE' 