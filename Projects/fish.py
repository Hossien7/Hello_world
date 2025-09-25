import random
reward = ['Rope', 'Fishing Rod', 'Bait', 'Boat', 'Net']
POUND = 0.45359237

def pound2kg(p):
    return p*POUND 

def kg2price(kg):
    price = 1.0
    if kg > 50:
        price = 0.5
        prince = price * kg
        return prince + random.choice(reward)
    elif kg > 20:
        price = 1.5
        prince = price * kg
        return prince

    elif kg > 10:
        price = 2.0
        return kg * price
    else:
        return kg * price

def main():
    print("Welcome to the Fishing Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start fishing.")
    total_kg = int(input("Enter the total weight of fish caught (in pounds): "))
    total_kg = pound2kg(total_kg)
    total_price = kg2price(total_kg)
    print(f"we buy your fish at ${total_price} per kg or reward.")

if __name__ == "__main__":
    main()