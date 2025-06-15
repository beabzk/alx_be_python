class BankAccount:
    """
    A simple bank account class that encapsulates banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the bank account.

        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")