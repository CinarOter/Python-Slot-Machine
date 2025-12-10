
import random

def spin_row():
    symbols = ["🍒","🍉","🍆","🍋","⭐"]
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍆':
            return bet * 1
        elif row[0] == '🍋':
            return bet * 2
        elif row[0] == '⭐':
            return bet * 10
    return 0


def main():
    balance = 100

    print("-" * 25)
    print("Welcome to Python Slots")
    print("Symbols: 🍒🍉🍆🍋⭐")
    print("-" * 25)
    while balance > 0:
        print(f"Current balance is £{balance}")
        print("-" * 25)

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            print("-" * 25)
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            print("-" * 25)
            continue

        balance -= bet
        print("-" * 25)

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won: £{payout}")
        else:
            print("Sorry you lost!")

        balance += payout

        if balance == 0:
            print("-" * 25)
            print("You have no money left to play!")
        elif balance > 0:
            play_again = input("Do you want to spin again?: (Y/N) ").upper()
            if play_again != 'Y':
                break



if __name__ == '__main__':
    main()
