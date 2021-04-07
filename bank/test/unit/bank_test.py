import unittest
from bank.bank.account import Account
from bank.bank.bank import Bank

class BankTest(unittest.TestCase):
    def test_bank_is_initially_empty(self):
        bank = Bank()
        self.assertDictEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts), 0)

    def test_add_account(self):
        bank = Bank()

        account_1 = Account(100, 50)
        account_2 = Account(200, 100)

        bank.add_account(account_1)
        bank.add_account(account_2)

        self.assertEqual(len(bank.accounts), 2)

    def test_get_account_balance(self):
        bank = Bank()

        account_1 = Account(100, 50)
        bank.add_account(account_1)

        self.assertEqual(bank.get_account_balance(100), 50)

    def test_deposit_updates_balance(self):
        bank = Bank()
        account_1 = Account(100, 50)
        bank.add_account(account_1)
        updated_balance = bank.deposit_updates_balance(100, 150)

        self.assertEqual(updated_balance, 200)


if __name__ == '__main__':
    unittest.main()

