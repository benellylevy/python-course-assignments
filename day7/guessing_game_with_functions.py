import random

def print_welcome():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 20.")
    print("If you want to quit the game, type 'x'.")
    print("If you want to toggle debug mode, type 'd'.")
    print("If you want to toggle move mode, type 'm'.")
    print("If you want to start a new game at any time, type 'n'.")

def get_random_number():
    return random.randint(1, 20)

def print_debug(computer_number):
    print(f"Debug Mode: The current number is {computer_number}.")

def handle_move_mode(computer_number):
    move = random.choice([-2, -1, 0, 1, 2])
    # Make sure the number stays in bounds
    return max(1, min(20, computer_number + move))

def get_player_input():
    return input("What's your guess? ")

def handle_guess(player_guess, computer_number):
    if player_guess < computer_number:
        print("The number is bigger.")
        return False
    elif player_guess > computer_number:
        print("The number is smaller.")
        return False
    else:
        print(f"Congratulations! You've guessed the number {computer_number}.")
        return True

def play_single_game():
    computer_number = get_random_number()
    debug_mode = False
    move_mode = False
    print_welcome()

    while True:
        if debug_mode:
            print_debug(computer_number)
        player_input = get_player_input().strip().lower()

        if player_input == 'x':
            print("You've chosen to quit the game. Goodbye!")
            return False  # Don't start new game

        if player_input == 's':
            print(f"Cheat: The number is {computer_number}.")
            continue

        if player_input == 'd':
            debug_mode = not debug_mode
            print("Debug mode enabled." if debug_mode else "Debug mode disabled.")
            continue

        if player_input == 'm':
            move_mode = not move_mode
            print("Move mode enabled." if move_mode else "Move mode disabled.")
            continue

        if player_input == 'n':
            print("Starting a new game...")
            return True  # Start new game

        try:
            player_guess = int(player_input)
            if player_guess < 1 or player_guess > 20:
                print("Please guess a number between 1 and 20.")
                continue
            guessed_correctly = handle_guess(player_guess, computer_number)
            if guessed_correctly:
                break
            if move_mode:
                computer_number = handle_move_mode(computer_number)
        except ValueError:
            print("Please enter a valid number, 'x' to quit, 'd' to toggle debug mode, or 'm' to toggle move mode.")

    return ask_for_new_game()

def ask_for_new_game():
    answer = input("Play again? (y/n): ").strip().lower()
    return answer == 'y'

def main():
    play_again = True
    while play_again:
        play_again = play_single_game()

if __name__ == "__main__":
    main()
