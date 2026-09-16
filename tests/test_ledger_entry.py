from decimal import Decimal

from account import Account
from transaction import Transaction
from ledger_entry import LedgerEntry

# Test Case 1: Testing if Ledger entry for source account matches transaction
def test_ledger_entry():
    source_account = Account("Rohayne", "1001", "100")
    destination_account = Account("Dani", "1002", "50")

    transaction = Transaction(source_account, destination_account, "20.00", "TRANSFER")


    ledger_entry = LedgerEntry(source_account, transaction, Decimal("-20.00"))

    assert ledger_entry.account is source_account
    assert ledger_entry.transaction is transaction
    assert ledger_entry.amount == Decimal("-20.00")

# Test Case 2: Demonstrating double-entry accounting
def test_ledger_double_entry():
    source_account = Account("Rohayne", "1001", 100)
    destination_account = Account("Dani", "1002", 50)

    transaction = Transaction(source_account, destination_account, "20.00", "TRANSFER")

    source_entry = LedgerEntry(source_account, transaction, Decimal("-20.00"))
    destination_entry = LedgerEntry(destination_account, transaction, Decimal("20.00"))

    assert source_entry.amount + destination_entry.amount == Decimal("0.00")