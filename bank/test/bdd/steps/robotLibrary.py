from bank.bank.bank import Bank
from bank.bank.account import Account
from nose.tools import assert_equal, assert_in


class robotLibrary(object):

    def __init__(self):
        self.browser = None
        self.response = None
        self.form_response = None

    def Create_Account(self, account_number, balance):
        self.a = Account(account_number, balance)
        Bank.add_account(self.a)

    def Print_Testing(self):
        print('I am testing printing')
