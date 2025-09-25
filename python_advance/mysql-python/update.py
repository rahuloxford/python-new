from mysql.connector import connect

mydb = connect(
    host='localhost',
    user='root',
    password='root',
    database='library',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

update_query = "UPDATE books SET price=price + (price * 0.25) WHERE price < 40"

cursor.execute(update_query)

mydb.commit()