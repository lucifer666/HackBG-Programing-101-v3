from manage_company import ManageDatabase
from show_data import ShowData
from create_company import Database


def main():

        database = Database()
        managedb = ManageDatabase()
        showdata = ShowData()
        database.create_database()
        database.insert_data()

        showdata.show_list_of_employees()
        print(showdata.show_monthly_spending())
        print(showdata.show_yearly_spending())
        managedb.add_employee()
        showdata.show_list_of_employees()
        managedb.delete_employee()
        showdata.show_list_of_employees()
        print(showdata.show_monthly_spending())
        print(showdata.show_yearly_spending())
        managedb.update_employee()
        showdata.show_all_employees()

if __name__ == "__main__":
    main()
