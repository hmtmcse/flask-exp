from datetime import datetime, timedelta
import time

# Parse time from string
string_time = "12:30"
datetime_object = datetime.strptime(string_time, "%H:%M")

print(datetime_object)

time_string = "3:30"
result = time.strptime(time_string, "%H:%M")

print(result)

time_delta = timedelta(hours=1000)
print(str(time_delta))

gm_time = time.gmtime(60*60*200)
print(time.gmtime(60*60*200))
