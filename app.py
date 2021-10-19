from flask import Flask, render_template, request, redirect
import cx_Oracle
app = Flask(__name__)

DB_USER = "system"
DB_PASSWORD = "system"
Host = "localhost"
PORT = 1521
DNS = "XE"

def getConnection():
    connection = cx_Oracle.connect("system/system@localhost:1521/XE")
    # connection = cx_Oracle.connect("{0}/{1}@{2}:{3}/{4}".format(DB_USER,DB_PASSWORD,Host,PORT,DNS))
    return connection

def fetchData():
    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_data = "select * from Emp"
    cursor.execute(sql_fetch_data)
    res = ""
    strList = []
    for result in cursor:
        strList.append(result)
    connection.commit()
    cursor.close()
    connection.close()
    return strList  # list of tuples having data

class Emp:
    def __init__(self, empid, empname, emptitle, deptname, salary):
        self.empid = empid
        self.empname = empname
        self.emptitle = emptitle
        self.deptname = deptname
        self.salary = salary

def listToEmp(l):  # it returns a list of emp objects
    emplist = []
    for records in l:
        p, q, r, s, t = records
        a = Emp(p, q, r, s, t)
        # a = Emp(records[0],records[1],records[2], records[3], records[4])
        emplist.append(a)
    return emplist

def insertDB(u_emp):
    # todo: Can't use string as empid, change it to interger when implementing real app
    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_empids = "select empid from Emp ORDER BY empid"
    cursor.execute(sql_fetch_empids)
    a = [0,1]
    for row in cursor:
        for r in row:
            a.append(int(r))
    strng = str(a[-1])  # last element of the list
    s = int(strng)
    s += 1
    sql_insert_query = "INSERT INTO Emp (Empid, empname, emptitle, deptname, salary) VALUES ('{0}','{1}', '{2}', '{3}', '{4}')".format(s, u_emp.empname, u_emp.emptitle, u_emp.deptname, u_emp.salary)
    cursor.execute(sql_insert_query)
    connection.commit()
    cursor.close()
    connection.close()

def createAndInsert():
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("""CREATE TABLE Emp
        (Empid number(10) PRIMARY KEY, 
        Empname varchar2(25) NOT NULL, 
        Emptitle varchar2(30) NOT NULL, 
        deptname varchar2(35) NOT NULL, 
        salary number(38) NOT NULL)""")
    except:
        pass
    try:
        cursor.execute("INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)VALUES ('11001', 'Shubham', 'CEO', 'Executives', 500000)")
    except: 
        pass
    try: 
        cursor.execute("INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)VALUES ('11002', 'Abhiram', 'CTO', 'Executives', 410000)")
    except: 
        pass
    try: 
        cursor.execute("INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)VALUES ('11003', 'Bhargav', 'Software Developer', 'IT', 350000)")
    except: 
        pass
    try: 
        cursor.execute("INSERT INTO emp (EmpID, EmpName, emptitle, deptname, salary)VALUES ('11004', 'Sivesh', 'Software Tester', 'IT', 300000)")
    except: 
        pass
    connection.commit()
    cursor.close()
    connection.close()

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    # createAndInsert()
    if request.method == 'POST':
        name = request.form['u_empname']
        title = request.form['u_emptitle']
        dept = request.form['u_deptname']
        sal = request.form['u_salary']
        u_emp = Emp(id, name, title, dept, sal)
        insertDB(u_emp)
        return redirect("/")
    db_res = fetchData()
    pass_to_html = listToEmp(db_res)
    return render_template('index.html', emplist=pass_to_html)


def updateDB(empid, u_emp):
    connection = getConnection()
    cursor = connection.cursor()
    sql_update_query = "UPDATE Emp SET EmpName = '{0}', EmpTitle = '{1}', DeptName = '{2}', Salary = '{3}' WHERE Empid = '{4}'".format(u_emp.empname, u_emp.emptitle, u_emp.deptname, u_emp.salary, empid)
    cursor.execute(sql_update_query)
    connection.commit()
    cursor.close()
    connection.close()


@app.route('/update/<string:empid>', methods=['GET', 'POST'])
def update(empid):
    if request.method == 'POST':
        name = request.form['u_empname']
        title = request.form['u_emptitle']
        dept = request.form['u_deptname']
        sal = request.form['u_salary']
        u_emp = Emp(id, name, title, dept, sal)
        updateDB(empid, u_emp)
        return redirect("/")

    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_emp_query = "SELECT * FROM Emp WHERE Empid = '{0}'".format(empid)
    cursor.execute(sql_fetch_emp_query)
    for row in cursor:
        r = row
    connection.commit()
    cursor.close()
    connection.close()
    emp_To_update = Emp(r[0], r[1], r[2], r[3], r[4])
    return render_template('update.html', e=emp_To_update)


@app.route('/delete/<string:empid>')
def delete(empid):
    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_emp_query = "SELECT * FROM Emp WHERE Empid = '{0}'".format(empid)
    cursor.execute(sql_fetch_emp_query)
    for row in cursor:
        r = row
    emp_To_delete = Emp(r[0], r[1], r[2], r[3], r[4])
    sql_delete_emp_query = "DELETE FROM Emp WHERE Empid = '{0}'".format(empid)
    cursor.execute(sql_delete_emp_query)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
