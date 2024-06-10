import uuid
import string
import random


def get_random():
    uuid_str = str(uuid.uuid1())
    print(f"{uuid_str} {uuid_str[:8]}")


def five_digit():
    n = 5
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
    print(str(res))
    return res


digit_list = []
for _ in range(100000):
    digit = five_digit()
    if digit not in digit_list:
        digit_list.append(digit)
    else:
        print(f"Duplicate: {digit}")
