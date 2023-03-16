pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following tooppings:")

for topping in pizza['topping']:
    print("\t" + topping)
