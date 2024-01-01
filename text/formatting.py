number = 1
print("{:04d}".format(number))


def format_number(number, leading_zero: str = "2"):
    return format(number, f"0{leading_zero}d")


print(format_number(9, "2"))
print(format_number(9, "3"))
print(format_number(9, "4"))
print(format_number(9, "5"))
print(format_number(900, "1"))
