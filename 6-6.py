favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
inviters = {
    'jen',
    'sarah',
    'phil',
}

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")
#
# for name in favorite_languages.keys():
#     print(name.title())
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi  " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

for inviter in favorite_languages.keys():
    if inviter in inviters:
        print("Thank you for participating in the survey, " + inviter)
    else:
        print("Please participate in the survey " + inviter)
