import random
true = True
choice = ['ROCK', 'PAPER', 'SCISSORS']
aleatorio = random.choice(choice)
play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
while true == True:
    if play == aleatorio:
        print('Draw!\n IA chose {} and you {}'.format(aleatorio, aleatorio))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y': 
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'PAPER' and aleatorio == 'ROCK':
        print('You won!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y':
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'PAPER' and aleatorio == 'SCISSORS':
        print('You lost!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y':
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'ROCK' and aleatorio == 'SCISSORS':
        print('You won!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y':
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'ROCK' and aleatorio == 'PAPER':
        print('You lost!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y': 
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'SCISSORS' and aleatorio == 'PAPER':
        print('You won!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y': 
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()
    elif play == 'SCISSORS' and aleatorio == 'ROCK':
        print('You lost!\n IA chose {} and you {}'.format(aleatorio, play))
        again = str(input('Try again?[Y / N] ')).upper()
        if again == 'N':
            true = False
        elif again == 'Y':
            aleatorio = random.choice(choice)
            play = str(input('ROCK, PAPER, SCISSORS? ')).upper()