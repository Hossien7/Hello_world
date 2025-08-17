lst = [1, 4, 32, 5, 4, 234, 5, 1, 5]

def smallest_num(lst):  # 2 Done
    lst = [10, 4, 32, 5, 4, 234, 5, 1, 5]
    head = 0
    small = lst[head]
    while head < len(lst):
        if small > lst[head]:
            small = lst[head]
        head += 1
    return small

print(f'smallest num in your list is: {smallest_num(lst=lst)}')


def triangle(num):  # 3
    pass


def number_game():  # 8 Done
    flag = True
    target = 5
    while flag:
        user_name = input("Enter your name: ")
        user_num = int(input("Please Enter your unumber: "))
        if user_num == target:
            print(f"good hand{user_name}....\nyou did it!!!!!!!!!!")
            break
        elif user_num > target:
            print("your choice is biger than target.")
        elif user_num < target:
            print("your choice is smaller than target")

