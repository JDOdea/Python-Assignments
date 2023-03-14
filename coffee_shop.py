def setup_shop():
    shop_name = input("What's the name of the coffee shop?\n")

    print("\033[H\033[J")
    print("\n---------------------------------")
    print(shop_name + " Ordering System")
    print("---------------------------------\n")

def get_customer_name():
    customer_name = input("Name: ")
    while customer_name == "":
        customer_name = input("Please enter your name: ")
    print("\nOrder is for " + customer_name + "\n")
    return customer_name

def get_drink_menu():
    #Show Available Drinks
    drink_menu = [
        "Espresso",
        "Macchiato",
        "Latte",
        "Cappuccino",
        "Mocha Frap",
        "Americano",
        "Hot Chocolate",
        "Water"
    ]
    print("Drink Menu\n-----------")
    for drink in drink_menu:
        print(drink)

    return drink_menu

def take_order(drink_menu, customer_name):
    #Take and Print Customers Order
    print("\nTaking Order\n------------")
    drink_order = input("What would you like?\n")
    while drink_order not in drink_menu:
        drink_order = input("Please order from the menu:\n")
    print("\n" + customer_name + " has ordered a " + drink_order + "\n")


def main():
    setup_shop()
    customer_name = get_customer_name()
    menu = get_drink_menu()
    take_order(menu, customer_name)

main()
