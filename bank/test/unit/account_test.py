import unittest
from bank.bank.account import Account


class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account("050", 27)

    def test_account_object_returns_current_balance(self):
        account = Account("001", 50)


if __name__ == '__main__':
    unittest.main()