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
    sess_num = int(sess_num)

    if sess_num == None or sess.checkitem(sess_num) == False:
        res['status'] = 'Invalid Session!'
        return json.dumps(res)

    uid, group = sess[sess_num]

    taskcursor = cnn.cursor()
    taskcursor.execute("SELECT tid, taskname, type, introduction FROM tasks WHERE ispublic = {}".format(int(group in ['ADMIN', 'SUPER'])))

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

@tasks.route('/task')
def task_page():
    reqh = request.headers
    res = {}
    res['code'] = 0
    sess_num = reqh.get('Session')
    sess_num = int(sess_num)

    if sess_num == None or sess.checkitem(sess_num) == False:
        res['status'] = 'Invalid Session!'
        return json.dumps(res)

    uid, group = sess[sess_num]
    taskcursor = cnn.cursor()

    tid = request.args.get('tid', '--unk')
    if tid == '--unk':
        raise Exception('Not valid task id!')

    taskcursor.execute("SELECT entry_id, source, labels FROM datasets WHERE tid={TID} and is_annotated=0".format(tid=TID))

    res['entry'] = []

    for entry_id, source, labels in taskcursor:
        res['entry'].append({
            "entry_id": entry_id,
            "source": source,
            "labels": labels
        })

    return res

