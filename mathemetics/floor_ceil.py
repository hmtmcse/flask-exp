import math

array = []
for n in range(1, 100):
    float_number = n / 100
    float_plus_number = n + float_number
    print(f"Float: {float_number}, Plus : {float_plus_number}, Ceil {math.ceil(float_plus_number)}, Floor {math.floor(float_plus_number)}")
