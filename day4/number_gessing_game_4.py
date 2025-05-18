import random

def guessing_game():
    # Computer selects a random number between 1 and 20
    computer_number = random.randint(1, 20)
    debug_mode = False  # To track whether debug mode is on

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 20.")
    print("If you want to quit the game, type 'x'.")
    print("If you want to toggle debug mode, type 'd'.")
    # Loop until the player guesses correctly or chooses to exit
    while True:
        # If debug mode is on, show the current number
        if debug_mode:
            print(f"Debug Mode: The current number is {computer_number}.")

        # Player inputs their guess
        player_guess = input("What's your guess? ")

        # Check if the player wants to quit
        if player_guess.lower() == 'x':
            print("You've chosen to quit the game. Goodbye!")
            break

        # Check if the player wants to cheat
        if player_guess.lower() == 's':
            print(f"Cheat: The number is {computer_number}.")
            continue
        # Toggle debug mode if the player presses 'd'
        if player_guess.lower() == 'd':
            debug_mode = not debug_mode
            if debug_mode:
                print("Debug mode enabled.")
            else:
                print("Debug mode disabled.")
            continue


        try:
            # Convert the player's input to an integer
            player_guess = int(player_guess)

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
            print("Please enter a valid number, 'x' to quit, or 'd' to toggle debug mode.")
# Start the game
guessing_game()