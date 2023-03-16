# # aline_o = {'color': 'green', 'points': 5}
# # aline_1 = {'color': 'yellow', 'points': 10}
# # aline_2 = {'color': 'red', 'points': 15}
# #
# # alines = [aline_2, aline_1, aline_o]
# #
# # for alien in alines:
# #     print(alien)
#
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
#     aliens.append(new_alien)
#
# for aline in aliens[:5]:
#     print(aline)
# print("^^^^^^^^")
#
# print("Total number of aliens: "+ str((len(aliens))))

aliens = []

for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)
print("^^^^")






