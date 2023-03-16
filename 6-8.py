dog = {
    'author': 'A',
    'class_belonging': 'B',
}

cat = {
    'author': 'C',
    'class_belonging': 'D',
}

bird = {
    'author': 'E',
    'class_belonging': 'F',
}

lion = {
    'author': 'G',
    'class_belonging': 'H',
}

pets = [dog, cat, bird, lion]

for pet in pets:
    print(pet['author'] + pet['class_belonging'])

