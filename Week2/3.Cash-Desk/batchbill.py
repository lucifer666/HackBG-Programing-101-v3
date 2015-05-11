# Task2: The BatchBill class
from bill import Bill

class BatchBill:

    def __init__(self, Bills):
        self.Bills = Bills

    def __len__(self):
        return  len(self.Bills)

    def total(self):
        total_sum = 0
        for bill in self.Bills:
            total_sum += int(bill)
        return total_sum

    def __getitem__(self, index):  # позволява ни да итерираме класа
        return self.Bills[index]

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

for bill in batch:
     print(bill)
print(batch.total())
