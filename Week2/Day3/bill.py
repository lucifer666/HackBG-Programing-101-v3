# Task1: The Bill class

class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A %s$ bill" % self.amount

    def __repr__(self):
        return "A %s$ bill" % self.amount

    def __eq__(self, other_amount):
        return self.amount == other_amount.amount

    def __hash__(self):
        return self.amount

a = Bill(10)
b = Bill(5)
c = Bill(10)

print (int(a))
print (str(a))
print (repr(a))
print (a == b)
print (a == c)
print (hash(a))

money_holder = {}
money_holder[a] = 1
if c in money_holder:
    money_holder[c] += 1
print (money_holder)

