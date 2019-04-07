from utils import cnn, sess
from flask import request, Blueprint
import json

tasks = Blueprint('task', __name__)

@tasks.route('/')
def tasks_set():
    reqh = request.headers
    res = {}
    res['code'] = 0
    sess_num = reqh.get('Session')

    if sess_num == None or sess.checkitem(sess_num) == False:
        res['status'] = 'Invalid Session!'
        return json.dumps(res)

    uid = sess[sess_num]
    taskcursor = cnn.cursor()
    taskcursor.execute("SELECT tid, taskname, type, introduction FROM tasks WHERE ispublic = 1")

    res['tasks'] = []

    for tid, taskname, tasktype, intro in taskcursor:
        res['tasks'].append({
            "tid": tid,
            "taskname": taskname,
            "type": tasktype,
            "intro": intro
        })
    #print(json.dumps(res))
    return json.dumps(res)
