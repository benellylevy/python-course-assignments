import random

# Initial stars
stars = 10

# Intro explanation (once)
print("🎲 Welcome to the Number Group Game!")
print("You start with 10 stars.")
print("Each round, the computer picks a number between 2 and 12.")
print("You choose one of three groups:")
print("  1️⃣ Group 1: Numbers 2 to 6 (win = 2x stars)")
print("  2️⃣ Group 2: Number 7 only (win = 3x stars)")
print("  3️⃣ Group 3: Numbers 8 to 12 (win = 2x stars)")
print("If your group matches the number, you win!\n")

# Game loop
while stars > 0:
    print(f"\n⭐ You have {stars} stars.")

    # Choose group
    group = input("Choose a group (1, 2, or 3): ").strip()
    if group not in ['1', '2', '3']:
        print("⚠️ Invalid group. Try again.")
        continue

    # Bet amount
    bet = input("How many stars do you want to bet? ").strip()
    if not bet.isdigit() or int(bet) <= 0 or int(bet) > stars:
        print("⚠️ Invalid number of stars.")
        continue
    bet = int(bet)

    # Random number between 2–12
    number = random.randint(2, 12)
    print(f"\n🎯 The number is: {number}")

    # Check for win
    win = False
    reward = 0

    if group == '1' and 2 <= number <= 6:
        win = True
        reward = bet * 2
    elif group == '2' and number == 7:
        win = True
        reward = bet * 3
    elif group == '3' and 8 <= number <= 12:
        win = True
        reward = bet * 2

    # Result
    if win:
        stars += reward
        print(f"🏆 You won! You gain {reward} stars.")
    else:
        stars -= bet
        print("😢 You lost this round.")

    if stars <= 0:
        print("\n💀 You have no more stars. Game over.")
        break

    # Continue?
    again = input("Play another round? (y/n): ").strip().lower()
    if again != 'y':
        print("🎉 Thanks for playing!")
        break