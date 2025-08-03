from tabulate import tabulate


member = 3
total = 0
ice_cream = [
    {"Item": "Chocolate", "Price (USD)": 2},
    {"Item": "Vanilla", "Price (USD)": 5},
    {"Item": "Strawberry", "Price (USD)": 3},
    {"Item": "banana", "Price (USD)": 7},
    {"Item": "cantaloupe", "Price (USD)": 10},
]


def show_table(data):
    print("Welcome to the DONDI Ice Cream Shop!")
    print("Here are our available flavors and their prices:")
    print("========================================")
    print(tabulate(data, headers="keys", tablefmt="grid", numalign="center"))
    print("========================================")
    print(f"Total flavors available: {len(data)}")


def check_price(data, item):
    """This function use for check price from data

    Args:
        item (str): The name of the ice cream flavor to check.
        data (dict): 
        ice_cream = [
        {"Item": "Chocolate",
         "Price (USD)": 2},]
    """
    for flavor in data:
        if flavor["Item"].lower() == item.lower():
            print(f"The price of {item} is ${flavor['Price (USD)']}.")
            return flavor['Price (USD)']
    print(f"Sorry, we don't have {item} in our menu.")

    return 0
if __name__ == "__main__":
    show_table(ice_cream)
    for _ in range(member):
        item = input("Enter the ice cream flavor do you want to buy!: ")
        if item.lower() == "exit":
            print("Thank you for visiting the DONDI Ice Cream Shop!")
            break
        else:
            price = check_price(ice_cream, item)
            total += price
            print(f"Added {item} to your order. Current total: ${total}")
