is_running = True
balance = 0
def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        return amount
    else:
        print(f"Invalid amount to deposit.")
        return 0

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if balance < 0:
        print("===========================================")
        print(f"  Withdrawal amount can't be in negative  ")
        print("===========================================")
        return 0
    elif balance <= amount:
        print("===========================================")
        print(f"          Insufficient funds              ")
        print("===========================================")
        return 0
    else:
        return amount

while is_running:
    print("===========================================")
    print("              BANKING PROGRAM              ")
    print("===========================================")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    selection = input("Select an option from above: ")
    if selection.isdigit() and 0 < int(selection) < 5:
        match selection:
            case '1':
                show_balance()
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw()
            case '4':
                is_running = False
    else:
        print(f"Invalid option - {selection}. Choose again!")