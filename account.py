# creating a blueprint for bank accounts. i.e Account("Rohayne", "1001", 1000)
# means owner = Rohayne, account_number = 1001 and balance = 1000.

from decimal import Decimal

class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = Decimal(str(balance))

    def _validate_amount(self, amount):
        amount = Decimal(str(amount))

        if amount.as_tuple().exponent < -2:
            raise ValueError("Amount cannot have more than 2 decimal places")

        return amount

    def deposit(self, amount):
        amount = self._validate_amount(amount)

        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be more than 0")

    def withdraw(self, amount):
        amount = self._validate_amount(amount)

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount