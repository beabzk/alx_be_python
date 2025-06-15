import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount> or python main-0.py display")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Handle the 'display' command which doesn't require an amount
    if sys.argv[1] == "display":
        command = "display"
        amount = None
    elif ':' in sys.argv[1]:
        try:
            command, param_str = sys.argv[1].split(':', 1)
            amount = float(param_str)
        except ValueError:
            print("Invalid amount format. Amount must be a number.")
            sys.exit(1)
        except Exception as e:
            print(f"Error parsing command: {e}")
            sys.exit(1)
    else:
        print("Invalid command format. Use <command>:<amount> or 'display'.")
        sys.exit(1)


    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Available commands: deposit, withdraw, display.")

if __name__ == "__main__":
    main()