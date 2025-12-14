import random

def spin_row():
    return [random.choice(["🍋", "⚽", "🔔", "🍒"]) for _ in range(3)]

def print_row(row):
    print("***********************************************")
    print(" | ".join(row))
    print("***********************************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍋":
            return bet * 5
        elif row[0] == "⚽":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 15
        elif row[0] == "🍒":
            return bet * 20
    return 0

def main():
    print("***********************************************")
    print("               SLOT MACHINE GAME               ")
    print("***********************************************")
    print("                You ready to spin              ")
    print("***********************************************")
    print("                 🍋 ⚽ 🔔 🍒                  ")
    print("***********************************************")
    balance = 100
    print(f"Your current balance: ${balance:.2f}")
    while balance > 0:
        bet = input("Enter the amount you wanna bet: ")
        if not bet.isdigit():
            print("Please enter a valid bet amount")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient fund to bet")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue
        balance -= bet
        rows = spin_row()
        print("Spinning...........\n")
        print_row(rows)

        payout = get_payout(rows, bet)
        if payout > 0:
            print(f"You won ${payout}! 🎊")
        else:
            print("Sorry you lost this round ☹️")

        balance += payout
        while True:
            play_again = input("Do you wanna spin again? (Y/N): ")
            if play_again.upper() in ("Y", "N"):
                break
            print("Invalid selection! Select again!")

        if play_again.upper() == "N":
            print("***********************************************")
            print(f"    GAME OVER! Your total is {balance:.2f}    ")
            print("***********************************************")
            break


if __name__ == "__main__":
    main()