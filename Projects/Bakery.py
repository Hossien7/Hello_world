bread = [('Barbary', 5000), ('Lavash', 2000), ('Sangak', 15000), ('Taftoon', 5000), ('Konjedi', 12000)]
sum = 0
while True:
    print('Welcom to DONDI Bakery!')
    answer_of_user = input('Do You Want Bread? y/n: ')
    if answer_of_user == 'y':
        print(f'1.{bread[0][0]}\n2.{bread[1][0]}\n3.{bread[2][0]}\n4.{bread[3][0]}\n5.{bread[4][0]}')
        user_bread = input('Enter your Bread index: ')
        if int(user_bread):
            couser_bread = int(user_bread)
            sum += bread[(couser_bread - 1)][1]
    else:
        break

print(f'Sum of your bread cost: {sum}')
