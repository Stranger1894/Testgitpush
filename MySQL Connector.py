import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", passwd="Svthegreat2803",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "SHOW DATABASES"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))



