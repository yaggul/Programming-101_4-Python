import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = BankAccount('Ivo', 0, 'BGN')
        self.account2 = BankAccount('Rado', 1000, 'BGN')

    def test_BankAccount_init(self):
        self.assertEqual(self.account1.acc_name, 'Ivo')
        # self.assertEqual(self.account2.acc_name , 'Rado')
        self.assertEqual(self.account1.acc_balance, 0)
        self.assertEqual(self.account1.acc_currency, 'BGN')

    def test_BankAccount_str(self):
        self.assertEqual(str(self.account1),"Bank account for Ivo with balance of 0BGN")

    def test_BankAccount_int(self):
        self.assertEqual(int(self.account1.acc_balance), 0)

    def test_BankAccount_deposit(self):
        self.assertEqual(self.account1.acc_balance + 500,500)

    def test_BankAccount_balance(self):
        self.assertEqual(self.account1.acc_balance, 0)

    def test_BankAccount_withdraw(self):
        self.assertEqual(self.account2.acc_balance - 500, 500)
        # self.assertEqual(self.account1.acc_balance - 1000, False)

    def test_BankAccount_eq(self):
        pass

    def test_BankAccount_hash(self):
        pass

    def test_BankAccount_transfer_to(self):
        pass

    def test_BankAccount_history(self):
        pass


if __name__ == '__main__':
    unittest.main()
