print("\n---------------------------------")
print("Sterberks Coffee Ordering System")
print("---------------------------------\n")


#Get and Show Customer Name
customer_name = input("Name: ")
while customer_name == "":
    customer_name = input("Please enter your name: ")
print("\nOrder is for " + customer_name + "\n")


#Show Available Drinks
drink_menu = [
    "Espresso",
    "Macchiato",
    "Latte",
    "Cappuccino",
    "Americano",
    "Hot Chocolate"
]
print("Drink Menu\n-----------")
for drink in drink_menu:
    print(drink)


#Take and Print Customers Order
print("\nTaking Order\n------------")
drink_order = input("What would you like?\n")
while drink_order not in drink_menu:
    drink_order = input("Please enter your order.\n")
print("\n" + customer_name + " has ordered a " + drink_order + "\n")