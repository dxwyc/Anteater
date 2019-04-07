import mysql.connector as myconn

config = {
        'host': 'cd-cdb-hxo372tm.sql.tencentcdb.com',
        'user': 'root',
        'port': 63166,
        'password': 'ruen_W2k_13edDM',
        'database': 'nlplabeler',
        'charset': 'utf8'
}

try:
    cnn = myconn.connect(**config)
except myconn.Error as e:
    print('Connect fails!{}'.format(e))

cursor = cnn.cursor()

try:
    sql_query = 'select uid, username, is_expert from users;'
    cursor.execute(sql_query)
    print("Enter!")
    for uid, usern, isexp in cursor:
        print(uid, usern, ' => ', isexp)
except myconn.Error as e:
    print('Query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
