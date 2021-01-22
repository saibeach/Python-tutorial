import random

def guessyournumber(x):
    low = 1
    high = x
    guess = 0
    while guess != 'C':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ')
        

        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            break
        print(low, high)

    print(f'Yeah, I got your number {guess}')
guessyournumber(10)