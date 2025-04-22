import random


number = random.randint(1, 10)
guess = int(input("Guess the number: "))
if guess == number:
    print("Correct!")
else:
    print("Wrong!")