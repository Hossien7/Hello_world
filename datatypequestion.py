name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
fcolor = input("Enter your favorite color: ")
fcar = input("Enter your favorite car: ")
fhobby = input("Enter your hobby: ")
fchannel = input("Enter your favorite channel: ")
fartist = input("Enter your favorite artist: ")

Ali_dictionary = {
    'name': name,
    'last_name': last_name,
    'age': age,
    'weight': weight,
    'favorite_color': fcolor,
    'favorite_car': fcar,
    'favorite_hobby': fhobby,
    'favorite_channel': fchannel,
    'favorite_artist': fartist,
}

end = f'My name is {Ali_dictionary['name']} {Ali_dictionary['last_name']},\
    I am {Ali_dictionary['age']} years old,\
    my weight is {Ali_dictionary['weight']} kg,\
    my favorite color is {Ali_dictionary['favorite_color']},\
    my favorite car is {Ali_dictionary['favorite_car']}, my hobby is {Ali_dictionary['favorite_hobby']},\
    my favorite channel is {Ali_dictionary['favorite_channel']},\
    and my favorite artist is {Ali_dictionary['favorite_artist']}.'

print(end)
