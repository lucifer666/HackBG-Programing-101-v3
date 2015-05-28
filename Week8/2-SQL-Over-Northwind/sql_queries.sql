#1. List all employees with their first name, last name and title.
SELECT FirstName || " " || LastName AS fullName, Title FROM employees;

#2. List all employees from Seattle.
SELECT * FROM employees WHERE City="Seattle";

#3. List all employees from London.
SELECT * FROM employees WHERE City="London";

#4. List all employees that work in the Sales department.
SELECT * FROM employees WHERE Title LIKE "%Sales%";

#5. List all females employees that work in the Sales department.
SELECT * FROM employees WHERE Title LIKE "%Sales%" AND TitleOfCourtesy = "Ms." OR TitleOfCourtesy = "Mrs.";

#6. List the 5 oldest employees.
SELECT * FROM employees ORDER BY BirthDate LIMIT 5;

#7. List the first 5 hires of the company.
SELECT * FROM employees ORDER BY HireDate LIMIT 5;

#8.List the employee who reports to no one (the boss)
SELECT * FROM employees WHERE ReportsTo IS NULL;

"""
#9.List all employes by their first and last name, and the first and last name of the employees that they report to.
SELECT FirstName || " " || LastName AS fullName,
"""
#10. Count all female employees.
SELECT  COUNT(EmployeeID) FROM employees WHERE TitleOfCourtesy IN ("Ms.", "Mrs.");

#11. Count all male employees.
SELECT COUNT(EmployeeID) FROM employees WHERE TitleOfCourtesy = "Mr.";

"""
#12. Count how many employees are there from the different cities. For example, there are 4 employees from London.
"""

#13. List all OrderIDs and the employees (by first and last name) that have created them.
SELECT Firstname || " " || LastName AS fullName, OrderID FROM employees JOIN orders ON
employees.EmployeeID = orders.EmployeeID;

"""
#14. List all OrderIDs and the shipper name that the order is going to be shipped via.
"""

#15. List all contries and the total number of orders that are going to be shipped there.


