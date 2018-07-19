import random


def roll_dice():
    dice = random.randint(1, 6)
    print(dice)
    answer = input('Would you like another roll?')
    if answer.lower() == 'yes':
        roll_dice()
    else:
        print('Hope you enjoyed that :p')


def roll_two_dice():
    dice = random.randint(1, 6)
    dice2 = random.randint(1,6)
    print(dice)
    print(dice2)
    answer = input('Would you like another roll?')
    if answer.lower() == 'yes':
        roll_two_dice()
    else:
        print('Hope you enjoyed that!')


if __name__ == '__main__':
    roll_two_dice()