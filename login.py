from utils import cnn
from flask import request, Blueprint
import json

login = Blueprint('login', __name__)

@login.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        username = request.args.get('username', '--unfound')
        password = request.args.get('password', '--unk')

    print('[Information]', username, ' , ', password)

    logincursor = cnn.cursor()
    logincursor.execute("SELECT uid, username, pwd FROM \
            users WHERE username='{usrname}'".format(usrname=username))

    record = logincursor.fetchone()

    res = {}
    status = ''
    code = 0

    if record == None:
        status = "The user entered doesn't exist!"
    elif record[2] != password:
        status = 'Password doesn\'t match!'
    else:
        status = 'Successful login!'
        code = 1

    res['SID'] = 32938
    res['code'] = code
    res['status'] = status

    return json.dumps(res)
