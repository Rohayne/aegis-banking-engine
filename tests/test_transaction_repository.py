from account import Account
from transaction import Transaction
from transaction_repository import TransactionRepository

# Test Case 1: Checking if TransactionRepository.save() works
def test_save():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 500)

    transaction1 = Transaction(source_account, destination_account, 300, "TRANSFER")

    repository = TransactionRepository()
    repository.save(transaction1)

    assert transaction1 in repository.transactions

# Test Case 2: Checking if we can store multiple transactions
def test_save_multiple_transactions():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 1000)

    transaction1 = Transaction(source_account, destination_account, 300, "TRANSFER")
    transaction2 = Transaction(source_account, destination_account, 200, "TRANSFER")

    repository = TransactionRepository()
    repository.save(transaction1)
    repository.save(transaction2)

    assert transaction1 in repository.transactions
    assert transaction2 in repository.transactions
    assert len(repository.transactions) == 2

# Test Case 3: Searching for account
def test_search_for_an_account():
    account1 = Account("Rohayne", "1001", 1000)
    account2 = Account("Dani", "1002", 500)
    account3 = Account("Arryan", "1003", 800)

    transaction1 = Transaction(account1, account2, 300, "TRANSFER")
    transaction2 = Transaction(account2, account1, 100, "TRANSFER")
    transaction3 = Transaction(account2, account3, 50, "TRANSFER")

    repository = TransactionRepository()
    repository.save(transaction1)
    repository.save(transaction2)
    repository.save(transaction3)

    rohayne_transactions = repository.find_by_account(account1)

    assert transaction1 in rohayne_transactions
    assert transaction2 in rohayne_transactions
    assert transaction3 not in rohayne_transactions
    assert len(rohayne_transactions) == 2

# Test Case 4: Searching for an account not involved in a transaction
def test_search_for_an_account_not_involved_in_transaction():
    account1 = Account("Rohayne", "1001", 1000)
    account2 = Account("Dani", "1002", 500)
    account3 = Account("Arryan", "1003", 800)

    transaction1 = Transaction(account1, account2, 300, "TRANSFER")
    transaction2 = Transaction(account2, account1, 100, "TRANSFER")

    repository = TransactionRepository()
    repository.save(transaction1)
    repository.save(transaction2)

    arryan_transactions = repository.find_by_account(account3)

    assert transaction1 not in arryan_transactions
    assert transaction2 not in arryan_transactions
    assert len(arryan_transactions) == 0