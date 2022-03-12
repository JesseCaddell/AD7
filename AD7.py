import sqlite3
from AD7_employee import Employee

#assign connection and cursor
conn = sqlite3.connect('employee.db')
c = conn.cursor()

#employees to be added
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Mary', 'Schafer', 60000)
emp_4 = Employee('Jerry', 'Schafer', 40000)

#create table function
def create_table():
    c.execute(""" CREATE TABLE employees (
                    first text,
                    last text,
                    pay integer
                    )""")


def insert_employee(emp):
    emp = emp
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first,'last': emp.last,'pay': emp.pay})
    conn.commit()

def query_search():
    c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
    print(c.fetchall())

def delete_value():
    conn.execute("DELETE FROM employees WHERE last=:last", {'last': 'Doe'})

def commit_close():
    conn.commit()
    conn.close()




create_table()
insert_employee(emp_1)
insert_employee(emp_2)
insert_employee(emp_3)
insert_employee(emp_4)

#search for last name Doe
query_search()

#delete row with last name Doe
delete_value()

#search to see if deleted
query_search()
commit_close()