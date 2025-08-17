flag = True
target = 5
while flag:
    user_num = int(input("Please Enter your unumber: "))
    if user_num == target:
        print("good hand....\nyou did it!!!!!!!!!!")
        break
    elif user_num > target:
        print("your choice is biger than target.")
    elif user_num < target:
        print("your choice is smaller than target")
