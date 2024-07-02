# test_wallet.py


from wallet import Wallet
import pytest


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a wallet instance with a balance of 20'''
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_deposit(wallet):
    wallet.deposit(80)
    assert wallet.balance == 100


def test_wallet_withdraw(wallet):
    wallet.withdraw(10)
    assert wallet.balance == 10
