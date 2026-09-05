import pytest
from account import Account

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