from decimal import Decimal

from account import Account
from transaction import Transaction
from ledger_entry import LedgerEntry
from ledger_repository import LedgerRepository

# Test Case 1: Saving both sides of one £20 transfer into ledger repository
def test_ledger_repository_for_two_accounts_of_same_transfer():
    source_account = Account("Rohayne", "1001", "100")
    destination_account = Account("Dani", "1002", "50")

    transaction = Transaction(source_account, destination_account, "20.00", "TRANSFER")

    source_entry = LedgerEntry(source_account, transaction, Decimal("-20.00"))
    destination_entry = LedgerEntry(destination_account, transaction, Decimal("20.00"))
    ledger_repository = LedgerRepository()

    ledger_repository.save(source_entry)
    ledger_repository.save(destination_entry)

    assert source_entry in ledger_repository.entries
    assert destination_entry in ledger_repository.entries
    assert len(ledger_repository.entries) == 2