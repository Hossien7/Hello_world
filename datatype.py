name = 'Ali'
last_name = 'Tajary'
age = 12
weight = 52.23

Ali_dictionary = {
    'name': name,
    'last_name': last_name,
    'age': age,
    'weight': weight,
}
data_list = [Ali_dictionary]


print(type(name))
print(type(last_name))
print(type(age))
print(type(weight))
print(type(Ali_dictionary))
print(type(data_list))
print(Ali_dictionary)
print(data_list)
print(f"Name: {name}, Last Name: {last_name}, Age: {age}, Weight: {weight}")
print(f"Name: {Ali_dictionary['name']}, Last Name: {Ali_dictionary['last_name']}, Age: {Ali_dictionary['age']}, Weight: {Ali_dictionary['weight']}")
print(f"Name: {data_list[0]['name']}, Last Name: {data_list[0]['last_name']}, Age: {data_list[0]['age']}, Weight: {data_list[0]['weight']}")

