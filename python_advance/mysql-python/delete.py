from mysql.connector import connect

mydb = connect(
    host='localhost',
    user='root',
    password='root',
    database='library',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

delete_query = "DELETE FROM books WHERE price > 50"

cursor.execute(delete_query)

mydb.commit()