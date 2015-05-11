# Task: The CashDesk classs
from bill import Bill
from batchbill import BatchBill
import operator

class CashDesk:

    def __init__(self):
        self.vault = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.vault.append(int(money))
        if isinstance(money, BatchBill):
            for m in money:
                self.vault.append(m)

    def total(self):
        total_money = 0
        for money in self.vault:
            total_money += int(money)
        return total_money

    def inspect(self):

        different_bills = ""
        money_holder = {}
        list_keys = []
        list_values = []
        result = ""
        for money in self.vault:
            count_different_bills = self.vault.count(money)
            key = money
            if key not in list_keys:
                list_keys.append(key)
                list_values.append(count_different_bills)
        for keys in list_keys:
            different_bills = "%s$ bills" % keys
            res = list_values.pop(0)
            result += different_bills + " - " + str(res) + "\n"
        return result

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batchbill = BatchBill(values)
bill = Bill(10)
desk = CashDesk()

desk.take_money(batchbill)
desk.take_money(bill)

print(desk.total())
print(desk.inspect())

