from abc import ABC, abstractmethod
from datetime import datetime


# Base Class
class BankAccount(ABC):

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self._account_number = account_number
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self._balance += amount
        self._add_transaction("Deposit", amount)
        print("Amount deposited successfully!")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def _add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self._balance,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self._transactions.append(transaction)

    def show_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self._account_number)
        print("Account Balance:", self._balance)

    def transaction_history(self):
        if not self._transactions:
            print("No transactions available.")
            return

        print("\n--- TRANSACTION HISTORY ---")

        for transaction in self._transactions:
            print(transaction)


# Inherited Class
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            self._add_transaction("Withdrawal", amount)
            print("Withdrawal successful!")


# Inherited Class
class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            self._add_transaction("Withdrawal", amount)
            print("Withdrawal successful!")


# Banking System Class
class BankingSystem:

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self):
        name = input("Enter account holder name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Select account type: ")

        if choice == "1":
            account = SavingsAccount(
                name, self.next_account_number
            )
        elif choice == "2":
            account = CurrentAccount(
                name, self.next_account_number
            )
        else:
            print("Invalid account type.")
            return

        self.accounts[self.next_account_number] = account

        print("\nAccount created successfully!")
        print("Your Account Number:", self.next_account_number)

        self.next_account_number += 1

    def find_account(self):
        try:
            number = int(input("Enter account number: "))
            account = self.accounts.get(number)

            if account is None:
                print("Account not found.")

            return account

        except ValueError:
            print("Please enter a valid account number.")
            return None

    def deposit_money(self):
        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Enter a valid amount.")

    def withdraw_money(self):
        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Enter a valid amount.")

    def check_balance(self):
        account = self.find_account()

        if account:
            account.show_details()

    def show_history(self):
        account = self.find_account()

        if account:
            account.transaction_history()

    def run(self):
        while True:
            print("\n==============================")
            print("       PYTHON BANKING SYSTEM")
            print("==============================")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Account Details")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.create_account()

                elif choice == "2":
                    self.deposit_money()

                elif choice == "3":
                    self.withdraw_money()

                elif choice == "4":
                    self.check_balance()

                elif choice == "5":
                    self.show_history()

                elif choice == "6":
                    print("Thank you for using Python Banking System!")
                    break

                else:
                    print("Invalid choice. Try again.")

            except Exception as error:
                print("An error occurred:", error)


# Main Program
if __name__ == "__main__":
    bank = BankingSystem()
    bank.run()
          
