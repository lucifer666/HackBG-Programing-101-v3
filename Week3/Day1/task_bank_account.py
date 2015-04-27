# Task: A Bank Account, the TDD way

class BankAccount(object):


    def __init__(self, name, balance, currency):
        self.list_history = []
        self.name = name
        self.balance = balance
        self.currency = currency
        self.list_history.append("Account was created")

    def __str__(self):
         message = "Bank account for {} with balance {}{}"
         return message.format(self.name, self.balance, self.currency)

    def __int__(self):
        self.list_history.append("__int__ check -> {}$".format(self.balance))
        return self.balance

    def deposit(self, amount):
       if amount < 0:
            raise ValueError
       self.balance += amount
       self.list_history.append("Deposited {}$".format(amount))
       return self.balance


    def get_balance(self):
        if not self.balance:
            return False
        else:
            self.list_history.append("Balance check -> {}$".format(self.balance))
            return self.balance

    def withdraw(self, amount):
       if self.balance < amount:
             self.list_history.append("Withdraw for {}$ failed".format(amount))
             return "Error"
       else:
            self.balance -= amount
            self.list_history.append("{}$ was withdrawed".format(amount))
            return True

    def transfer_to(self, account, amount):

        if self.currency != account.currency:
            raise ValueError

        if self.balance < amount:
            raise ValueError

        self.balance -= amount
        self.list_history.append("Transfer to {} for {}{}".format(account.name, amount, self.currency))
        account.balance += amount
        account.list_history.append("Transfer from {} for {}{}".format(self.name, amount, self.currency))
        return True

    def history(self):
        return self.list_history





