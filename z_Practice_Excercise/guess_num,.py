import random

def random_game():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too Low!!")
        elif guess > number:
            print("Too High!!")
        else:
            print("You Guessed It!!!!")
    

random_game()