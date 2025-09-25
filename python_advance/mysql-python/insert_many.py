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

datas = [
    (1002, "Hunger Games", 57.8),
    (1003, "Animal Farm", 63.1),
    (1004, "A Little Life", 45.2),
]

cursor.executemany(insertion, datas)

mydb.commit()