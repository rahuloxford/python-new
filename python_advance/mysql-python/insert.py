from mysql.connector import connect

mydb = connect(
    host='localhost',
    user='root',
    password='root',
    database='library',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

insertion = 'INSERT INTO books(book_id, title, price) VALUES(%s, %s, %s)'

data = (1001, "The Housemaid", 38.7)

cursor.execute(insertion, data)

mydb.commit()