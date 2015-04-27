# Task: Test the BankAccount

from task_bank_account import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):

    def test_init(self):
        my_account = BankAccount("Rado", 1000, "$")
        self.assertEqual(my_account.name, "Rado")
        self.assertEqual(my_account.balance, 1000)
        self.assertEqual(my_account.currency, "$")

    def test_str(self):
        my_account = BankAccount("Rado", 1000, "$")
        needed_result = "Bank account for Rado with balance 1000$"
        self.assertEqual(str(my_account), needed_result)

    def test_int(self):
        my_account = BankAccount("Rado", 1000, "$")
        self.assertEqual(int(my_account.balance),1000)

    def test_deposit(self):
        my_account = BankAccount("Rado", 1000, "$")
        result = my_account.deposit(500)
        self.assertEqual(my_account.balance, result)

    def test_if_the_balance_is_right(self):
        my_account = BankAccount("Rado", 1000, "$")

        result = my_account.get_balance()
        self.assertEqual(my_account.get_balance(), result)

    def test_withdraw_money_from_account(self):
        my_account = BankAccount("Rado", 1000, "$")
        result = "Error"
        self.assertTrue(my_account.withdraw(400))
        self.assertEqual(my_account.balance, 600)
        self.assertEqual(my_account.withdraw(1100), result)

    def test_negative_deposit(self):
        my_account = BankAccount("Rado", 1000, "$")
        with self.assertRaises(ValueError):
            my_account.deposit(-500)


    def test_transfer_to_diferent_currency(self):
        my_account = BankAccount("Rado", 1000, "$")
        second_account = BankAccount("Filip", 500, "#")

        with self.assertRaises(ValueError):
            my_account.transfer_to(second_account, 200)
            self.assertEqual(my_account.balance, 1000)
            self.assertEqual(second_account.balance, 500)

    def test_transfer_to_more_money_thah_we_have(self):
        my_account = BankAccount("Rado", 1000, "$")
        second_account = BankAccount("Filip", 500, "$")

        with self.assertRaises(ValueError):
            self.assertFalse(my_account.transfer_to(second_account, 1100))
            self.assertEqual(my_account, 1000)
            self.assertEqual(second_account, 500)

        with self.assertRaises(ValueError):
            self.assertFalse(second_account.transfer_to(my_account, 600))
            self.assertEqual(my_account, 1000)
            self.assertEqual(second_account, 500)

    def test_transfer_to(self):
        second_account = BankAccount("Filip", 500, "$")
        my_account = BankAccount("Rado", 1000, "$")
        result = my_account.transfer_to(second_account, 200)
        self.assertEqual(my_account.balance, 1000 - 200)
        self.assertEqual(second_account.balance, 500 + 200)
        self.assertTrue(result)

    def test_history(self):
        my_account = BankAccount("Filip", 1000, "$")
        my_account.deposit(1000)
        my_account.get_balance()
        str(my_account)
        int(my_account)
        result = ['Account was created', 'Deposited 1000$', 'Balance check -> 2000$', '__int__ check -> 2000$']
        self.assertEqual(my_account.history(), result)
        my_account.withdraw(500)
        result = ['Account was created', 'Deposited 1000$', 'Balance check -> 2000$', '__int__ check -> 2000$',
        '500$ was withdrawed']
        self.assertEqual(my_account.history(), result)
        my_account.withdraw(2000)
        my_account.get_balance()
        result = ['Account was created', 'Deposited 1000$', 'Balance check -> 2000$', '__int__ check -> 2000$',
        '500$ was withdrawed', 'Withdraw for 2000$ failed', 'Balance check -> 1500$']
        self.assertEqual(my_account.history(), result)
        ivo = BankAccount("Ivo", 0, "$")
        my_account.transfer_to(ivo, 500)
        my_account.get_balance()
        ivo.get_balance()
        result = ['Account was created', 'Deposited 1000$', 'Balance check -> 2000$', '__int__ check -> 2000$',
        '500$ was withdrawed', 'Withdraw for 2000$ failed', 'Balance check -> 1500$', 'Transfer to Ivo for 500$', 'Balance check -> 1000$']
        result2 = ['Account was created','Transfer from Filip for 500$', 'Balance check -> 500$']
        self.assertEqual(my_account.history(), result)
        self.assertEqual(ivo.history(), result2)


if __name__ == "__main__":
    unittest.main()
