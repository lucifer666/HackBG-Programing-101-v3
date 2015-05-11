import sqlite3
from manage_company import ManageDatabase


class ShowData:

    def __init__(self):
        self.database = ManageDatabase()

    def show_list_of_employees(self):
        result = self.database.list_employees()
        for data in result:
          print("{} - {}".format(data[0], data[1]))

    def show_monthly_spending(self):
        result = self.database.monthly_spending()
        total_sum = 0
        for money in result:
            total_sum += int(money[0])
        return ("The company is spending {}$ every month!".format(total_sum))

    def show_yearly_spending(self):
        total_bonus = 0
        total_salary = 0
        total_sum = 0
        for bonus in self.database.yearly_spending():
            total_bonus = int(bonus[0])
        for salary in self.database.monthly_spending():
            total_salary += int(salary[0])

        total_sum = total_bonus + 12*total_salary
        return ("The company is spending {}$ every year!".format(total_sum))

    def show_all_employees(self):
        employees_list = self.database.return_all_employees()
        for employee in employees_list:
            print("{} | {} | {} | {} | {}".format(employee[0], employee[1], employee[2], employee[3], employee[4]))

