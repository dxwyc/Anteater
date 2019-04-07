from flask import Flask, request, redirect
import mysql.connector as mycnn

config = {
        'host': 'cd-cdb-hxo372tm.sql.tencentcdb.com',
        'user': 'root',
        'port': 63166,
        'password': 'ruen_W2k_13edDM',
        'database': 'nlplabeler',
        'charset': 'utf8'
}

app = Flask(__name__)

try:
    cnn = mycnn.connect(**config)
except myconn.Error as e:
    print('Connect fails!{}'.format(e))

import views
