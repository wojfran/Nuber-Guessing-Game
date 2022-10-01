import random

r = random.randint(1, 1001)
print('Guess what number I have in mind :p\nIt is between 1 and 1000, including both\n')
guess = 1001
while guess != r:
    guess = input('Please enter a number: \n')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Enter a number you dummy')
        continue

    if guess > r:
        print('\nTry lower :)')
    elif guess < r:
        print('\nTry higher :)')

print(f'\nCongrats!!! You guessed that the number I imagined was {r}')
