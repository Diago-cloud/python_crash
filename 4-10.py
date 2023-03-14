my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_food)

print("The first teree items in the list are: " + str(my_foods[:3]))
print("Three items from the middle of the list are: " + str(friend_food[-3:]))
print("Three items from the middle of the list are: " + str(my_foods[-3:]))