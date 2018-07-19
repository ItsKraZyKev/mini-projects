import random

highest_num = 100  # int(input('What would you like the maximum number to be?'))
answer = random.randint(1, highest_num)

guess = int(input('Guess the number: '))
attempts_taken = 0

while guess != answer:
    if guess == 0:
        print('Quitter')
        break
    elif guess < answer:  # guess too low
        print('You guessed too low!')
        attempts_taken +=1
        guess = int(input('Try again cupcake: '))
    elif guess > answer:  # guess too high
        print('You guess too high!')
        guess = int(input('Try again cupcake: '))
        attempts_taken += 1
    elif guess == answer:  # guess is right
        print('Way to go, you got it right!')
        attempts_taken += 1



print(f'It took you {attempts_taken} guesses!')
