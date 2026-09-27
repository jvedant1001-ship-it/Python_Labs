import json
import os
from datetime import datetime

class Account:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self._pin = pin
        self.balance = balance
        self.transactions = []

    def verify_pin(self, pin):
        return self._pin == pin

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        self.balance += amount
        self.add_transaction("Deposit", amount, self.balance)

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Current Balance: ₹{self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount
        self.add_transaction("Withdrawal", amount, self.balance)

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Current Balance: ₹{self.balance:.2f}")
        return True

    def add_transaction(self, transaction_type, amount, balance):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": balance,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)

    def show_transactions(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\nTRANSACTION HISTORY")
        print("-" * 65)

        for transaction in self.transactions:
            print(
                f"{transaction['date']} | "
                f"{transaction['type']:<20} | "
                f"₹{transaction['amount']:<10.2f} | "
                f"Balance: ₹{transaction['balance']:.2f}"
            )

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            print("Incorrect old PIN.")
            return False

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must contain exactly 4 digits.")
            return False

        self._pin = new_pin
        print("PIN changed successfully.")
        return True

    def show_details(self):
        print("\nACCOUNT DETAILS")
        print("-" * 40)
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Balance        : ₹{self.balance:.2f}")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "pin": self._pin,
            "balance": self.balance,
            "transactions": self.transactions
        }


class SavingsAccount(Account):
    def __init__(self, account_number, name, pin, balance=0, interest_rate=4):
        super().__init__(account_number, name, pin, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100

        print("\nINTEREST CALCULATION")
        print("-" * 40)
        print(f"Current Balance : ₹{self.balance:.2f}")
        print(f"Interest Rate   : {self.interest_rate}%")
        print(f"Interest        : ₹{interest:.2f}")

        return interest

    def to_dict(self):
        data = super().to_dict()
        data["account_type"] = "Savings"
        data["interest_rate"] = self.interest_rate
        return data


class CurrentAccount(Account):
    def __init__(
        self,
        account_number,
        name,
        pin,
        balance=0,
        minimum_balance=1000
    ):
        super().__init__(account_number, name, pin, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        if self.balance - amount < self.minimum_balance:
            print(
                f"Withdrawal failed.\n"
                f"Minimum balance of ₹{self.minimum_balance:.2f} "
                f"must be maintained."
            )
            return False

        self.balance -= amount
        self.add_transaction("Withdrawal", amount, self.balance)

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Current Balance: ₹{self.balance:.2f}")
        return True

    def to_dict(self):
        data = super().to_dict()
        data["account_type"] = "Current"
        data["minimum_balance"] = self.minimum_balance
        return data


class Bank:
    DATA_FILE = "bank_data.json"

    def __init__(self):
        self.accounts = {}
        self.load_data()

    def generate_account_number(self):
        if not self.accounts:
            return "100001"

        numbers = [
            int(account_number)
            for account_number in self.accounts.keys()
        ]

        return str(max(numbers) + 1)

    def create_account(self):
        print("\nCREATE NEW ACCOUNT")

        name = input("Enter account holder name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        pin = input("Create a 4-digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        print("\nChoose account type:")
        print("1. Savings Account")
        print("2. Current Account")

        account_type = input("Enter choice: ")

        try:
            initial_deposit = float(
                input("Enter initial deposit: ")
            )

            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return

        account_number = self.generate_account_number()

        if account_type == "1":
            account = SavingsAccount(
                account_number,
                name,
                pin,
                initial_deposit
            )
        elif account_type == "2":
            if initial_deposit < 1000:
                print(
                    "Current Account requires "
                    "minimum ₹1000 initial deposit."
                )
                return

            account = CurrentAccount(
                account_number,
                name,
                pin,
                initial_deposit
            )
        else:
            print("Invalid account type.")
            return

        if initial_deposit > 0:
            account.add_transaction(
                "Initial Deposit",
                initial_deposit,
                initial_deposit
            )

        self.accounts[account_number] = account
        self.save_data()

        print("\nAccount created successfully!")
        print(f"Your Account Number is: {account_number}")

    def login(self):
        print("\nACCOUNT LOGIN")

        account_number = input(
            "Enter account number: "
        ).strip()

        pin = input("Enter PIN: ")

        account = self.accounts.get(account_number)

        if account is None:
            print("Account not found.")
            return None

        if not account.verify_pin(pin):
            print("Incorrect PIN.")
            return None

        print(f"\nWelcome, {account.name}!")
        return account

    def transfer_money(self, sender):
        print("\nMONEY TRANSFER")

        receiver_number = input(
            "Enter receiver account number: "
        ).strip()

        if receiver_number == sender.account_number:
            print("You cannot transfer money to yourself.")
            return

        receiver = self.accounts.get(receiver_number)

        if receiver is None:
            print("Receiver account not found.")
            return

        try:
            amount = float(
                input("Enter transfer amount: ")
            )
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > sender.balance:
            print("Insufficient balance.")
            return

        sender.balance -= amount

        sender.add_transaction(
            f"Transfer to {receiver.account_number}",
            amount,
            sender.balance
        )

        receiver.balance += amount

        receiver.add_transaction(
            f"Transfer from {sender.account_number}",
            amount,
            receiver.balance
        )

        self.save_data()

        print("\nTransfer successful!")
        print(
            f"₹{amount:.2f} transferred to "
            f"{receiver.name}."
        )
        print(
            f"Your remaining balance: "
            f"₹{sender.balance:.2f}"
        )

    def save_data(self):
        data = {}

        for account_number, account in self.accounts.items():
            data[account_number] = account.to_dict()

        try:
            with open(
                self.DATA_FILE,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(data, file, indent=4)

        except IOError:
            print("Error saving bank data.")

    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            return

        try:
            with open(
                self.DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            for account_number, details in data.items():
                account_type = details.get(
                    "account_type",
                    "Savings"
                )

                if account_type == "Current":
                    account = CurrentAccount(
                        details["account_number"],
                        details["name"],
                        details["pin"],
                        details["balance"],
                        details.get(
                            "minimum_balance",
                            1000
                        )
                    )
                else:
                    account = SavingsAccount(
                        details["account_number"],
                        details["name"],
                        details["pin"],
                        details["balance"],
                        details.get(
                            "interest_rate",
                            4
                        )
                    )

                account.transactions = details.get(
                    "transactions",
                    []
                )

                self.accounts[account_number] = account

        except (
            IOError,
            json.JSONDecodeError,
            KeyError
        ):
            print("Unable to load existing bank data.")


def account_menu(bank, account):
    while True:
        print(f"\nWelcome, {account.name}")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Account Details")
        print("7. Change PIN")
        print("8. Calculate Interest")
        print("9. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(
                f"\nCurrent Balance: "
                f"₹{account.balance:.2f}"
            )

        elif choice == "2":
            try:
                amount = float(
                    input("Enter deposit amount: ")
                )

                if account.deposit(amount):
                    bank.save_data()

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            try:
                amount = float(
                    input("Enter withdrawal amount: ")
                )

                if account.withdraw(amount):
                    bank.save_data()

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "4":
            bank.transfer_money(account)

        elif choice == "5":
            account.show_transactions()

        elif choice == "6":
            account.show_details()

        elif choice == "7":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new 4-digit PIN: ")

            if account.change_pin(old_pin, new_pin):
                bank.save_data()

        elif choice == "8":
            if isinstance(account, SavingsAccount):
                account.calculate_interest()
            else:
                print(
                    "Interest calculation is "
                    "available only for Savings Accounts."
                )

        elif choice == "9":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    bank = Bank()

    while True:
        print("\nBANKING MANAGEMENT SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            account = bank.login()

            if account:
                account_menu(bank, account)

        elif choice == "3":
            bank.save_data()
            print(
                "\nThank you for using "
                "the Banking Management System."
            )
            break

        else:
            print(
                "Invalid choice. "
                "Please select 1, 2, or 3."
            )


if __name__ == "__main__":
    main()
