from random import randint

one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0

for num in range(100):
    number = randint(1,10)
    
    if number == 1:
        one += 1
    elif number == 2:
        two += 1

    elif number == 3:
        three += 1

    elif number == 4:
        four += 1

    elif number == 5:
        five += 1

    elif number == 6:
        six += 1

    elif number == 7:
        seven += 1

    elif number == 8:
        eight += 1

    elif number == 9:
        nine += 1

print('one: ' + str(one))
print('two: ' + str(two))
print('three: ' + str(three))
print('four: ' + str(four))
print('five: ' + str(five))
print('six: ' + str(six))
print('seven: ' + str(seven))
print('eight: ' + str(eight))
print('nine: ' + str(nine))