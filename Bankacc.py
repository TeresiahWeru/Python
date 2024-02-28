class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return amount

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def customer_details(self):
        print(f"""
Customer Name: {self.customer_name}
Account Number: {self.account_number}
Date of Opening: {self.date_of_opening}
Balance: ${self.balance:.2f}
""")
