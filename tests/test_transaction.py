import pytest
from account import Account
from transaction import Transaction


# Test Case 1: Source Account Outgoing transaction
def test_source_account_transaction_perspective():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 500)


    transaction = Transaction(source_account, destination_account, 300, "TRANSFER")

    assert transaction.get_direction_for(source_account) == "Outgoing transaction"

# Test Case 2: Destination Account Incoming transaction
def test_destination_account_transaction_perspective():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 500)

    transaction = Transaction(source_account, destination_account, 300, "TRANSFER")

    assert transaction.get_direction_for(destination_account) == "Incoming transaction"

# Test Case 3: Unknown Account Unknown transaction
def test_unknown_account_transaction_perspective():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 500)
    unknown_account = Account("Arryan", "1003", 800)

    transaction = Transaction(source_account, destination_account, 300, "TRANSFER")

    with pytest.raises(ValueError):
        transaction.get_direction_for(unknown_account)