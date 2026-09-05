# Handling activities between more than one account.

class PaymentService:
    def transfer(self, source_account, destination_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0")
        elif amount > source_account.balance:
            raise ValueError("Transfer amount exceeds source's account balance")
        else:
            source_account.withdraw(amount)
            destination_account.deposit(amount)
