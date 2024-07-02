# wallet.py

class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
