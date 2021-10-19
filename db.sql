CREATE TABLE Emp
(Empid number(10) PRIMARY KEY,
Empname varchar2(25) NOT NULL,
Emptitle varchar2(30) NOT NULL,
deptname varchar2(35) NOT NULL,
salary number(38) NOT NULL);

INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)
VALUES ('11001', 'Shubham', 'CEO', 'Executives', 500000);

INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)
VALUES ('11002', 'Abhiram', 'CTO', 'Executives', 410000);       

INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)
VALUES ('11003', 'Bhargav', 'Software Developer', 'IT', 350000);

INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)
VALUES ('11004', 'Sivesh', 'Software Tester', 'IT', 300000) ;