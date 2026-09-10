# Handling activities between more than one account.

from transaction import Transaction

class PaymentService:
    def __init__(self, transaction_repository):
        self.transaction_repository = transaction_repository

    def transfer(self, source_account, destination_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0")
        elif amount > source_account.balance:
            raise ValueError("Transfer amount exceeds source's account balance")
        else:
            source_account.withdraw(amount)
            destination_account.deposit(amount)
            transaction = Transaction(source_account, destination_account, amount, "TRANSFER")
            self.transaction_repository.save(transaction)
            return transaction # Sends the Transaction object back to whoever called transfer().
