# creating a blueprint for bank accounts. i.e Account("Rohayne", "1001", 1000)
# means owner = Rohayne, account_number = 1001 and balance = 1000.

class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance