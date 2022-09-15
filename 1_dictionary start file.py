import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))
print(phonebook['Chris'])
print()

for name in phonebook:
    print(name, ':',  phonebook[name])

print()
x = dict(m=1, n=2)
print(x)

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()


if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not found in phonebook")

print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-4433'
phonebook['Joe'] = '555-4444'
print(phonebook)


print()
print('*****  end section 3 ********')
print()




print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

# del phonebook['Chris']
# print(phonebook)


print()
print('*****  end section 4 ********')
print()



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

# Get Keys + Values -- you can also use dict.keys()
for key in phonebook:
    print(key)
    print(phonebook[key])
print()

for value in phonebook.values():
    print(value)
print()

# Get Items

for key, value in phonebook.items():
    print(f'Key: {key}, Value: {value}')
print()

for tuple in phonebook.items():
    print(tuple)

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get("Chris", "no key found")
print(phone)

# phonebook.clear()
# print(phonebook)

print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


a = phonebook.pop('Chris', 'not found')
print(a)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)


print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()


print(random.choice(list(phonebook)), phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()








