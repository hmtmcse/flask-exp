import os
import pathlib
import datetime
from time import sleep

file_name = "start-track"
if os.path.exists(file_name):
    os.remove(file_name)
track_file = open(file_name, "x")
track_file.close()

for i in range(10):
    path = pathlib.Path(file_name)
    current_timestamp = path.stat().st_ctime
    c_time = datetime.datetime.fromtimestamp(current_timestamp)
    current_time = datetime.datetime.now()
    diff = current_time - c_time
    print(c_time)
    print(diff.seconds)
    sleep(1)


class Example:
    @staticmethod
    def is_created(file_name, diff_in_second):
        pass
