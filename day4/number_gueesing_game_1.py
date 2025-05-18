import random


def guessing_game():
    # Computer selects a random number between 1 and 20
    computer_number = random.randint(1, 20)

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 20.")

    # Loop until the player guesses correctly
    while True:
        try:
            # Player inputs their guess
            player_guess = int(input("What's your guess? "))

            if player_guess < 1 or player_guess > 20:
                print("Please guess a number between 1 and 20.")
                continue

            # Compare the player's guess to the computer's number
            if player_guess < computer_number:
                print("The number is bigger.")
            elif player_guess > computer_number:
                print("The number is smaller.")
            else:
                print(f"Congratulations! You've guessed the number {computer_number}.")
                break  # End the game if the guess is correct
        except ValueError:
            print("Please enter a valid number.")


# Start the game
guessing_game()