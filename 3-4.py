invite = ['Chen', 'Jack', 'Steven', 'Diago']

print(invite)

messsage = 'I\'m sorry ' + 'that ' + invite[3] + 'can not appear'
print(messsage)

invite[3] = 'Talyor'
print(invite)

messsage_invite = 'Would like to appear ' + 'tonight\'s dinner, '+ invite[0] + ',' + invite[1] + ',' 
print(messsage_invite + invite[2] + ',' + invite[3])


print("I have found a bigger table")

invite.insert(0,'Wang')
invite.insert(3,'Li')
invite.append('Sui')
messsage_invite = 'Would like to appear ' + 'tonight\'s dinner, '+ invite[0] + ',' + invite[1] + ',' + invite[2] + ',' + invite[3]
messsage_invite = messsage_invite + ',' + invite[4] + ',' + invite[5] + ',' + invite[6] 
print(messsage_invite)

print("I\'m sorry that I just can only invite two of yours.")

invite_1 = invite.pop()
print("I\'m sorry," + invite_1)
invite_2 = invite.pop()
print("I\'m sorry," + invite_2)
invite_3 = invite.pop()
print("I\'m sorry," + invite_3)
invite_4 = invite.pop()
print("I\'m sorry," + invite_4)
invite_5 = invite.pop()
print("I\'m sorry," + invite_5)
print(invite)

print("You are in the list," + invite[0])
print("You are in the list," + invite[1])

del invite[0]
print(invite)

del invite[0]
print(invite)

print(len(invite))