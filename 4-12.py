my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

for my_food in my_foods:
    print(my_food)
    
for my_friend_food in friend_food:
    print(my_friend_food)