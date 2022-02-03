# wallet.py

class InsufficientAmount(Exception):
    pass

class Wallet(object): 
    def __init__(self, i_amt=0):
        self.balance = i_amt
    
    def spend_cash(self, amt):
        if self.balance < amt:
            raise InsufficientAmount('Not enough available to spend {}'.format(amt))
        self.balance -= amt

    def add_cash(self, amt): 
        self.balance += amt