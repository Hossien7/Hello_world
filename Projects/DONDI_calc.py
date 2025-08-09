print("============================")
print("Welcome to the DONDI Calculator!")
print("============================")
print("1.kg to g calculator")   # ok
print("2.pounds to kg calculator")  # ok
print("3. km to m and cm calculator")   # ok
print("============================")
option = int(input("Please select an option:"))
if option == 1:
    print(f"KG is equal to {(float(input("Enter weight in kg: ")) * 1000)} g.")
elif option == 2:
    print(f"Pound is equal to {(float(input("Enter weight in pound: ")) * 0.453592)} KG.")
elif option == 3:
    print(f"KM is equal to {(float(input('Enter distance in KM for convert to m: ')) * 1000)} m and {(float(
        input('Enter distance in KM for convert to cm: ')) * 100000)} cm.")
else: 
    print("Invalid option selected. Please try again.")
print("Thank you for using the DONDI Calculator!")
