lst = [1, 4, 32, 5, 4, 234, 5, 1, 5]

def sum_of_even_and_odd(lst):  # 1 Done
    numbers = lst
    even_sum = 0
    odd_sum = 0
    index = 0

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            even_sum += numbers[index]
        else:
            odd_sum += numbers[index]
        index += 1

    print("Sum of Even Numbers:", even_sum)
    print("Sum of Odd Numbers:", odd_sum)


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


def triangle(num=10):  # 3 Done
    i = 0
    while i < num:
        print("*" * (i + 1))
        i += 1


def reverse_string(string):  # 4 Done
    string = 'iran'
    tail = -1
    while tail >= -len(string):
        print(string[tail])
        tail -= 1

def fact(num):  # 5 Done
    factorial = 1
    counter = 1
    while counter <= num:
        factorial *= counter
        counter += 1

    print("Factorial of", num, "is", factorial)

def check_prime(num):  # 6 Done
    is_prime = False
    if num < 2:
        return is_prime
    else:
        i = 2
        is_prime = True
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        return is_prime

def fibo(n):  # 7 Done
    a, b = 0, 1
    counter = 0

    while counter < n:
        print(f'{a} ,', end=' ')
        nth = a + b
        a = b
        b = nth
        counter += 1


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







def numbers(n): # 9 Done
    number = n
    multiplier = 1
    while multiplier <= 10:
        print(number, "x", multiplier, "=", number * multiplier)
        multiplier += 1
# numbers(10)

def sum_of_digit(lst):  # 10 Done
    sum = 0
    head = 0
    while head < len(lst):
        if type(lst[head]) == int:
            sum += lst[head]
        head += 1
    print(sum)
print(sum_of_even_and_odd(lst=lst))
# print(fibo(10))