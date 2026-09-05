import uuid

class Transaction:
    # __init__ is used when an object needs to be created with state/data that it should remember.
    def __init__(self, source_account, destination_account, amount, transaction_type):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_id = str(uuid.uuid4())