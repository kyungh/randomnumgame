import random
       
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Welcome! Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, try again because that was too low.')
        elif guess > random_number:
            print('Sorry, try again because that was too high.')

    print(f'Congratulations! You won by guessing the number {random_number} correctly!')


def restart():
        playagain = input ('Would you like to play again (Yes or No)?')
        if playagain == "yes":
            guess(25)
        elif playagain == "":
            print('Sorry, please type Yes or No.')
            return mainrun()
        else:
            exit()


def mainrun(): 
    guess(25)

def mainrestart():
    restart()
a = 1

while a==1:
    mainrun()
    mainrestart()