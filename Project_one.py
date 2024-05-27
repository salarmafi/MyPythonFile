'This is the first project I have done in python!'

import random
print('A number between 1 - 10')
a_number = round(random.random() * 10)

while True:

    user_guess = int(input('Enter a guess between 0 - 10: '))
    if user_guess == a_number:
        print('Congrats!')
        break
    else:
        print('Sorry')
        user_guess = input('Continue? [Y / N] -> ')
        if user_guess.lower() == 'y':
            continue
        else:
            print('You quitted')
            break

