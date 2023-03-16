number1 = {
    'first_name': 'Chen',
    'last_name': 'Yan',
    'age': '24',
    'city': 'Suzhou'}

number2 = {
    'first_name': 'Chen',
    'last_name': 'Huachun',
    'age': '24',
    'city': 'Suzhou'}

number3 = {
    'first_name': 'Cao',
    'last_name': 'Jiejun',
    'age': '24',
    'city': 'Suzhou'}

people = [number3, number2, number1]

for person in people:
    full_name = person['first_name'] + person['last_name']
    print(full_name + " is " + person['age'] + " living in " + person['city'])

