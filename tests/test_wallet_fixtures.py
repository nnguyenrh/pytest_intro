# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    ''' Returns a Wallet instance with zero balance '''
    return Wallet()

@pytest.fixture
def wallet():
    ''' Returns a wallet with instance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 110

def test_wallet_spend_cash(wallet): 
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)