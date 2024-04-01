-- 1.Numeric Data Types:
-- INT: Used for storing integers.
-- DECIMAL: Used for storing fixed-point numbers.
-- FLOAT: Used for storing floating-point numbers.
-- DOUBLE: Used for storing double-precision floating-point numbers.
CREATE TABLE Students (
    StudentID INT,
    GPA DECIMAL(3, 2),
    Height FLOAT,
    Weight DOUBLE
);

-- 2.String Data Types:
-- VARCHAR: Used for variable-length character strings.  #varchar(4) u can take len(1 or 2 or 3 or 4 or 5) 
-- CHAR: Used for fixed-length character strings. #char(4) u can only len(4)
-- TEXT: Used for large text values.
CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address TEXT
);


-- 3.Date and Time Data Types:
-- DATE: Used for storing dates in 'YYYY-MM-DD' format.
-- TIME: Used for storing times in 'HH:MM:SS' format.
-- DATETIME: Used for storing both date and time values.
-- TIMESTAMP: Used for storing the timestamp of when a row was last updated.
CREATE TABLE Orders (
    OrderID INT,
    OrderDate DATE,
    OrderTime TIME,
    LastUpdated TIMESTAMP
);


-- 4.Boolean Data Type:
-- BOOLEAN or BOOL: Used for storing boolean values (TRUE/FALSE or 1/0).
CREATE TABLE Students (
    StudentID INT,
    IsGraduated BOOLEAN
);


-- 5.Binary Data Types:
-- BLOB: Used for storing large binary objects such as images or documents.
-- BIT: Used for storing bit-field values.

CREATE TABLE Images (
    ImageID INT,
    ImageData BLOB
);


-- 6.Enumerated and Set Data Types:
-- ENUM: Used for storing one of a predefined set of values.
-- SET: Used for storing a set of predefined values.
CREATE TABLE Colors (
    ColorID INT,
    Color ENUM('Red', 'Green', 'Blue')
);


-- #table :creat,insert,update,delete,drop
CREATE TABLE Students(
    studentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT
);

INSERT INTO Students (studentID, FirstName, LastName, Age)
VALUES(1,"John","Doe",20)

UPDATE Students
SET Age= 21
WHERE StudentID=1;

DELETE FROM Students 
WHERE StudentID=1;

DROP TABLE Students;



