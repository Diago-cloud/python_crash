pizzas = ['xiangchang', 'fanqie', 'boluo']
friend_pizza = pizzas[:]

pizzas.append('carrot')
friend_pizza.append('caijiao')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are: ")
for pizza_f in friend_pizza:
    print(pizza_f)