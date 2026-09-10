class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def save(self, transaction):
        self.transactions.append(transaction)

    def find_by_account(self, account):
        my_account_transactions = []
        for transaction in self.transactions:
            if transaction.source_account is account or transaction.destination_account is account:
                my_account_transactions.append(transaction)
        return my_account_transactions