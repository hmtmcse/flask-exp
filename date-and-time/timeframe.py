from datetime import datetime, timedelta

# Current Date time
current_date_time = datetime.now()

# Current Time
current_time = current_date_time.time()

# Human read-able format
formatted_time = current_time.strftime("%H:%M")

# Parse time from string
string_time = "8:30"
datetime_object = datetime.strptime(string_time, "%H:%M")

# Time deviation
added_time = datetime_object + timedelta(minutes=40)


start_time = "13:30"
total_class = 4
each_class_time = 45
break_time = 20
class_before_break = 2

parsed_start_time = datetime.strptime(start_time, "%H:%M")
last_period = parsed_start_time
print(f"Class Duration : {each_class_time}")
print(f"Total Class : {total_class}")
print(f"Class Start From : {start_time}")
print(f"Break Time : {break_time}")
for period in range(1, total_class + 1):
    formatted_start_time = last_period.strftime("%H:%M")
    last_period = class_duration = last_period + timedelta(minutes=each_class_time)
    formatted_end_time = class_duration.strftime("%H:%M")
    print(f"{period} -- {formatted_start_time} -- {formatted_end_time}")

    if period == class_before_break:
        print(f"Break -- {break_time}")
        last_period = last_period + timedelta(minutes=break_time)

