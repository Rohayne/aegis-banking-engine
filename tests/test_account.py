import pytest
from account import Account
from decimal import Decimal

def test_positive_deposit():
    account = Account("Rohayne", "1001", 1000)

    account.deposit(500)

    # I expect this statement to be true. If true then PASS, if false then FAIL.
    assert account.balance == 1500

def test_zero_deposit():
    account = Account("Rohayne", "1001", 1000)

    # I expect this to raise a ValueError. If raises error then PASS else FAIL.
    with pytest.raises(ValueError):
        account.deposit(0)

def test_negative_deposit():
    account = Account("Rohayne", "1001", 1000)

    # I expect this to raise a ValueError. If raises error then PASS else FAIL.
    with pytest.raises(ValueError):
        account.deposit(-500)

# Withdrawals Test cases

# Test Case 1: Positive Withdrawal
def test_positive_withdrawal():
    account = Account("Rohayne", "1001", 1000)
    account.withdraw(500)

    assert account.balance == 500

# Test Case 2: Zero Withdrawal
def test_zero_withdrawal():
    account = Account("Rohayne", "1001", 1000)

    with pytest.raises(ValueError):
        account.withdraw(0)

# Test Case 3: Negative Withdrawal
def test_negative_withdrawal():
    account = Account("Rohayne", "1001", 1000)

    with pytest.raises(ValueError):
        account.withdraw(-500)

# Test Case 4: Full Balance Withdrawal
def test_full_balance_withdrawal():
    account = Account("Rohayne", "1001", 1000)
    account.withdraw(1000)

    assert account.balance == 0

# Test Case 5: Withdrawing more than Account Balance
def test_insufficient_funds():
    account = Account("Rohayne", "1001", 1000)

    with pytest.raises(ValueError):
        account.withdraw(1500)

    assert account.balance == 1000

# Test Case 6: Deposit Precision, using decimals
def test_deposit_precision():
    account = Account("Rohayne", "1001", "10.10")
    account.deposit("20.20")

    assert account.balance == Decimal("30.30")

# Test Case 7: Withdrawal Precision, with decimals
def test_withdraw_precision():
    account = Account("Rohayne", "1001", "50.50")
    account.withdraw("20.20")

    assert account.balance == Decimal("30.30")

# Test Case 8: Depositing money with more than 2 decimal places
def test_deposit_money_three_decimals():
    account = Account("Rohayne", "1001", "100.00")

    with pytest.raises(ValueError):
        account.deposit("10.123")

    assert account.balance == Decimal("100.00")

# Test Case 9: Withdrawing money with more than 2 decimal places
def test_withdraw_money_three_decimals():
    account = Account("Rohayne", "1001", "100.00")

    with pytest.raises(ValueError):
        account.withdraw("10.123")

    assert account.balance == Decimal("100.00")
