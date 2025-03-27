import random
import string


def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


# Generate multiple codes
codes = [generate_code() for _ in range(10)]
print(codes)


def generate_unique_codes(count):
    codes = set()
    while len(codes) < count:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        codes.add(code)
    return list(codes)


# Generate 10 unique codes
unique_codes = generate_unique_codes(10)
print(unique_codes)

print(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))


def generate_alphanumeric_code(length: int = 4):
    code = ''.join(random.choices(f"{string.ascii_uppercase}{string.digits}", k=length))
    return code


for _ in range(10):
    print(generate_alphanumeric_code())
