from mysql.connector import connect

mydb = connect(
    host='localhost',
    user='root',
    password='root',
    database='library',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE books(book_id INT, title VARCHAR(50), price DECIMAL(5, 2))")
