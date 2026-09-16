class LedgerEntry:
    def __init__(self, account, transaction, amount):
        self.account = account
        self.transaction = transaction
        self.amount = amount