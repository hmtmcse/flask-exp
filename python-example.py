
num = int(input())
sum = 0
while (num > 0):
    r = num % 10
    sum = sum * 10 + r
    num = num // 10

print("The number in reverse order is: " + str(sum))
