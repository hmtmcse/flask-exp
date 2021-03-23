import datetime
import json

from flask import Flask
from zk import ZK, const

app = Flask(__name__)


def get_all_attendance_from_device(ip, port=4370, timeout=30, device_id=None, clear_from_device_on_fetch=False):
    #  Sample Attendance Logs [{'punch': 255, 'user_id': '22', 'uid': 12349, 'status': 1, 'timestamp': datetime.datetime(2019, 2, 26, 20, 31, 29)},{'punch': 255, 'user_id': '7', 'uid': 7, 'status': 1, 'timestamp': datetime.datetime(2019, 2, 26, 20, 31, 36)}]
    zk = ZK(ip, port=port, timeout=timeout)
    conn = None
    attendances = []
    try:
        conn = zk.connect()
        x = conn.disable_device()
        # device is disabled when fetching data
        attendances = conn.get_attendance()
        if len(attendances):
            # keeping a backup before clearing data incase the programs fails.
            # if everything goes well then this file is removed automatically at the end.
            dump_file_name = './' + device_id + "_" + ip.replace('.', '_') + '_last_fetch_dump.json'
            with open(dump_file_name, 'w+') as f:
                f.write(json.dumps(list(map(lambda x: x.__dict__, attendances)), default=datetime.datetime.timestamp))
            if clear_from_device_on_fetch:
                x = conn.clear_attendance()
        x = conn.enable_device()
    except:
        raise Exception('Device fetch failed.')
    finally:
        if conn:
            conn.disconnect()
    return list(map(lambda x: x.__dict__, attendances))


def enrole(ip, port=4370, timeout=30):
    zk = ZK(ip, port=port, timeout=timeout)
    conn = zk.connect()
    conn.set_user(uid=6, name='Hasina', privilege=const.USER_DEFAULT, password='12345678', group_id='', user_id='6', card=0)
    zk.enroll_user(uid=6)
    return ""

@app.route('/')
def bismillah():
    out = get_all_attendance_from_device(ip="192.168.2.201", device_id="device1")
    return {"response": out}

@app.route('/enrole')
def enrolement():
    out = enrole(ip="192.168.2.201")
    return {"response": out}


if __name__ == '__main__':
    app.run()