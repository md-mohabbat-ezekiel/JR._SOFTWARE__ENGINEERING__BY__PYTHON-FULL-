-- Query -find
-- 1.select
-- 2.perameter
-- 3.crosstab
-- 4.unmatch 
-- 5.Action



-- 1.select
in student TABLE
-- Selecting names and ages of all students
SELECT name, age
FROM Students;
-- Selecting all columns from the Students table
SELECT *
FROM Students;




-- 2.perameter
-- Define a stored procedure that uses parameters
CREATE PROCEDURE GetStudentsByAge(IN min_age INT, IN max_age INT)
BEGIN
    -- Select students within the specified age range
    SELECT name, age
    FROM Students
    WHERE age BETWEEN min_age AND max_age;
END;

-- Call the stored procedure with specific age range parameters
CALL GetStudentsByAge(18, 25);


 --min_age and max_age are input parameters to the stored procedure GetStudentsByAge. 
 --The IN keyword indicates that these parameters are input parameters. 
 --Inside the stored procedure, we use these parameters to dynamically filter the Students table based on the age range provided.

-- Python using the mysql-connector-python library:


import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

# Create a cursor object
cursor = conn.cursor()

# Define SQL query with parameters
sql = "SELECT name, age FROM Students WHERE age BETWEEN %s AND %s"

# Execute SQL query with parameters
min_age = 18
max_age = 25
cursor.execute(sql, (min_age, max_age))

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()


-- 3.crosstab
-- used to generate summary reports from a table of data
-- Crosstab query to pivot sales data
--  in SQL, you typically use aggregate functions along with conditional statements to pivot the data.
SELECT 
    Year,
    SUM(CASE WHEN Month = 'January' THEN Revenue ELSE 0 END) AS January,
    SUM(CASE WHEN Month = 'February' THEN Revenue ELSE 0 END) AS February,
    SUM(CASE WHEN Month = 'March' THEN Revenue ELSE 0 END) AS March,
    -- Add more columns for other months as needed
FROM 
    Sales
GROUP BY 
    Year;



-- 4.unmatch 
-- "Unmatch" is not a standard SQL term,
-- but using various techniques such as NOT IN, NOT EXISTS, or LEFT JOIN with NULL
SELECT c.CustomerID, c.CustomerName
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
);


-- 5.Action
-- "action query" typically refers to SQL queries that modify data in a database. This includes INSERT, UPDATE, DELETE, and sometimes REPLACE queries. 
INSERT INTO Employees (EmployeeID, FirstName, LastName, Position)
VALUES (101, 'John', 'Doe', 'Software Engineer');


-- creat a student table ,then  select , where , constraints , arithmetic , comparison , logical AND or OR DISTINCT , ORDER BY , LIMIT , OFFSET 

-- create a student 
CREATE TABLE Student (
    Id INT PRIMARY KEY UNIQUE,
    Name varchar(50) NOT NULL,
    Age INT,
    GPA DECIMAL(3,2)
);

--  ANOTHER TABLE 
CREATE TABLE Library
(
  BookName VARCHAR(50) PRIMARY KEY,
  Roll CHAR(4),
  FOREIGN KEY (Roll) REFERENCES Student(Id)
);

-- CONSTRAINT:PRIMARY KEY,FOREIGN KEY,REFERENCES,NOT NULL,UNIQUE,CHECK
SELECT DISTINCT ID,Name, Age + 1 AS NextAge
FROM Student
WHERE Age >= 20 AND GPA > 3.5 
-- WHERE MEANS CONDITIONS
ORDER BY Age DESC, FirstName ASC 
-- orded age in descend and ascending by name
LIMIT 10 OFFSET 0;
-- COLUMN until 10 and BETWEEN this colum no space meance OFFSET 0




-- functions,GROUPS functions, GROUP by ,ALTER table 
-- Create Student table
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT,
    GPA DECIMAL(3, 2)
);
-- Insert sample data into Student table
INSERT INTO Student (StudentID, FirstName, LastName, Age, GPA)
VALUES
    (1, 'John', 'Doe', 20, 3.75),
    (2, 'Alice', 'Smith', 22, 3.85),
    (3, 'Bob', 'Johnson', 21, 3.65),
    (4, 'Emma', 'Brown', 23, 3.95);

-- ALTER TABLE ADD the new COLUMN   
ALTER TABLE student
ADD COLUMN major VARCHAR(50); 
-- NEW COLUMNN ADD IN TABLE BY ALTER 

-- UPDATE major COLUMN for certains students
UPDATE student
SET major='CSE'
WHERE StudentID IN (1,3);

-- Select statement with GROUP functions and GROUP BY
SELECT major,AVG(GPA) AS AvgGPA, COUNT(*) AS NumSudents
FROM Student
GROUP by major;


-- # subquery
use dummydb;
-- employee details of the employees who get less salary than a certain employee
SELECT * FROM employees
WHERE salary < (
SELECT salary FROM employees WHERE employee_ID=144
);

-- who gets the highest salary
SELECT * FROM employees
WHERE salary = (
SELECT MAX(salary) FROM employees 
);

-- #advanced_subquery
use dummydb;
-- who gets second highest salary
SELECT * FROM employees
WHERE salary = (
    SELECT MAX(salary) FROM employees
    WHERE salary < (
    SELECT MAX(salary) 
    FROM employees
    )
);


-- which employees get more salary than their manager
SELECT * FROM employees as EMP
WHERE salary > (
SELECT salary FROM employees as MGR
WHERE EMP.ManagerID = MGR.Employee_ID
);

-- which employees is in the same job as their manager
SELECT * FROM employees as EMP
WHERE JOB_ID = (
SELECT JOB_ID from Employees as MGR
WHERE MGR.Employee_ID=EMP.Manager_ID
);


-- #common table expration
use dummydb;
with max_salary as (
SELECT max(salary) as salary FROM employees
WHERE DEPARTMENT_ID = 20
);

SELECT * FROM employees
WHERE salary=(
SELECT salary FROM max_salary
);
-- from slary come form befor max_salary by with function . not from table


-- join
-- join employees with departments:
SELECT Employees.first_name,Department.DEPARTMENT_NAME
FROM Employees
JOIN Departments ON Employees.DEPARTMENT_ID = Departments.DEPARTMENT_ID
-- JOIN Employees + Departments table base one both common COLUMN DEPARTMENT_ID THEN SOME QUERY FIND

-- Select all columns from Employees table:
SELECT * FROM Employees;

-- JOIN Employee name with Manager name:
SELECT e.first_name AS employee, m.first_name AS manager
FROM Employees As e 
JOIN Employees AS m on e.manager_id = m.employee_id
-- join two same table name Employees

-- show departments with no employees
SELECT Departments.DEPARTMENT_NAME
FROM Departments
LEFT JOIN Employees ON Employees.department_id = Departments.DEPARTMENT_ID
WHERE Employees.DEPARTMENT_ID IS NULL;
-- JOIN BY LEFT JOIN AND THEN SET CONDITIONS BY WHERE 

-- Show employee first name, salary, and salary less than department average:
SELECT Employee.first_name,Employees.salary,
(SELECT AVG(salary) FROM Employees WHERE department_id=Employees.DEPARTMENT_ID)- Employees.salary AS "less than average"
from Employees
JOIN Departments ON Employees.DEPARTMENT_ID = Departments.DEPARTMENT_ID;


-- Show name of departments where minimum salary is more than 5000:
SELECT Departments.DEPARTMENT_NAME, MIN(salary),AVG(salary)
FROM Departments
JOIN Employees ON Departments.DEPARTMENT_ID = Employees.DEPARTMENT_ID
GROUP BY DEPARTMENT_NAME
HAVING MIN(salary) > 5000


-- WITHOUT JOIN
use dummydb;
SELECT Employees.first_name,Departments.Departments_name
from employees,departments
where Employees.DEPARTMENT_ID = Departments.DEPARTMENT_ID

-- Set opertatinon 
-- UNION U=all ->OR
-- INTERSECT n=common ->AND

SELECT * FROM employees
WHERE salary > 10000
UNION
SELECT * FROM employees
WHERE department_id=100;

select * from employees
where salary > 10000
INTERSECT
select * from employees
where department_id = 100;


-- connection SQL with python
import mysql.connector

my_db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

print(my_db_connection)


db_name = "python_test_db"
mycursor = my_db_connection.cursor()

sql_query = f'create database {db_name};'
mycursor.execute(sql_query)

-- CREATE TABLE by python connector
import mysql.connector

db_name = "python_test_db"

my_db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database=db_name
)

mycursor = my_db_connection.cursor()

sql_query =  f"""
    create table Student(
        Roll char(4),
        Name varchar(50)
    );
"""
mycursor.execute(sql_query)

-- INSERT
import mysql.connnector
-- firt import python module
db_name="Python_test_db"
-- set detabase name
my_db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database=db_name
)
-- connect with DBM branch
my_cursor = my_db_connection.cursor()

sql_query=f"""
    insert into Student (Roll,Name) values('1010','Bruce');
"""
-- operation SQL like DBM shell branch
my_cursor.execute(sql_query)
-- push in DBM shell by cursor().execute
my_db_connection.commit()







