import pytest

from account import Account
from payment_service import PaymentService

# Implementation: Pytest fixture to set up source_account, destination_account and payment_service = PaymentService().
# Purpose: Pytest fixture creates fresh accounts and a payment service for each test.
@pytest.fixture
def transfer_setup():
    source_account = Account("Rohayne", "1001", 1000)
    destination_account = Account("Dani", "1002", 500)
    payment_service = PaymentService()

    return source_account, destination_account, payment_service

# Test Case 1: Positive Transfer
def test_positive_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup
    payment_service.transfer(source_account, destination_account, 300)

    assert source_account.balance == 700
    assert destination_account.balance == 800

# Test Case 2: Zero Transfer
def test_zero_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup

    with pytest.raises(ValueError):
        payment_service.transfer(source_account, destination_account, 0)

    assert source_account.balance == 1000
    assert destination_account.balance == 500

# Test Case 3: Negative Transfer
def test_negative_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup

    with pytest.raises(ValueError):
        payment_service.transfer(source_account, destination_account, -100)

    assert source_account.balance == 1000
    assert destination_account.balance == 500

# Test Case 4: Insufficient Funds Transfer
def test_insufficient_funds_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup

    with pytest.raises(ValueError):
        payment_service.transfer(source_account, destination_account, 1200)

    assert source_account.balance == 1000
    assert destination_account.balance == 500

# Test Case 5: Full Balance Transfer
def test_full_balance_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup
    payment_service.transfer(source_account, destination_account, 1000)

    assert source_account.balance == 0
    assert destination_account.balance == 1500

# Test Case 6: Returned Transaction
def test_return_transaction_transfer(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup
    transaction = payment_service.transfer(source_account, destination_account, 300)

    assert transaction.source_account is source_account
    assert transaction.destination_account is destination_account
    assert transaction.amount == 300
    assert transaction.transaction_type == "TRANSFER"
    assert transaction.transaction_id is not None

# Test Case 7: Two transactions should generate unique Transaction IDs
def test_transactions_have_unique_ids(transfer_setup):
    source_account, destination_account, payment_service = transfer_setup

    transaction1 = payment_service.transfer(source_account, destination_account, 300)
    transaction2 = payment_service.transfer(source_account, destination_account, 300)

    assert transaction1.transaction_id != transaction2.transaction_id
