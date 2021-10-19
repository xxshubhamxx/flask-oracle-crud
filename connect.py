import cx_Oracle

def getConnection():
    connection = cx_Oracle.connect("system/system@localhost:1521/XE")
    return connection 

def fetchData():
    connection = getConnection()
    cursor = connection.cursor()
    sql_fetch_data="select * from tab"
    cursor.execute(sql_fetch_data)
    for result in cursor:
        print(result)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    fetchData()