#names = ['admin', 'afds', 'asdsfawef','awertg','agraew']

names = []

if names:
    for name in names:
        if name == 'admin':
            print("Hello " + name +",would you like to see a status report?")
        else:
            print("Hello " + name + ",thak you for logging in again.")
else:
    print("We need to find some users!")
            