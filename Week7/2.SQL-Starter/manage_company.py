import sqlite3
from create_company import Database

class ManageDatabase:

    def __init__(self):
        self.conn = sqlite3.connect("create_company.db")
        self.cursor = self.conn.cursor()


    def list_employees(self):
        result = self.cursor.execute("SELECT name, position FROM company")
        return result

    def monthly_spending(self):
        result = self.cursor.execute("SELECT monthly_salary From company")
        return result

    def yearly_spending(self):
        result = self.cursor.execute("SELECT sum(yearly_bonus) From company")
        return result

    def add_employee(self):
        db = Database()
        db.insert_data()

    def delete_employee(self):
        employee_id = input("Enter the id of the employee, which you want to delete: ")
        deleted_employee = ""
        delete = self.cursor.execute("SELECT name FROM company  WHERE id=?", employee_id)
        for name in delete:
            deleted_employee = name[0]
        self.cursor.execute("DELETE FROM company WHERE id = ?", employee_id)
        self.conn.commit()
        print("{} was deleted!".format(deleted_employee))

    def update_employee(self):
        employee_id = input("Enter the id of the employee, which you want to update: ")
        name = input("Enter firstname and lastname: ")
        monthly_salary = int(input("Enter monthly_salary: "))
        yearly_bonus = int(input("Enter yearly_bonus: "))
        position = input("Enter position: ")
        self.cursor.execute("UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?",(name, monthly_salary,
            yearly_bonus, position, employee_id))
        self.conn.commit()


    def return_all_employees(self):
        all_employees = self.cursor.execute("SELECT * FROM company")
        employees_list = []
        for employee in all_employees:
            employees_list.append(employee)
        return employees_list


