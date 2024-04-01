AM_10_to_11 = "10 AM - 11 AM"
split_data = AM_10_to_11.split("-")
print(len(split_data))
if len(split_data) == 2:
    print(split_data[1].strip())
